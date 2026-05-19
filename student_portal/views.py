import json
import re
from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from enrollment.models import Student, Course, Exam, ExamAttempt, CourseContent, InteractiveChallenge, ChallengeAttempt
from notificaciones.models import Notification, AdminNotification
from email_service.services import send_password_changed_email
from .models import LessonProgress, AssignmentSubmission, DiplomaRequest

def check_password_change(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'student') and request.user.student.generated_password:
            messages.warning(request, "PROTOCOLO DE SEGURIDAD: Debes actualizar tu contraseña inicial antes de continuar.")
            return redirect('student_change_password')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def check_student_status(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'student'):
            student = request.user.student
            if student.status == 'suspended':
                logout(request)
                messages.error(request, "Tu cuenta ha sido SUSPENDIDA hasta nuevo aviso por el administrador del sistema.")
                return redirect('student_login')
            elif student.status == 'rejected':
                logout(request)
                messages.error(request, "Tu cuenta ha sido RECHAZADA.")
                return redirect('student_login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def student_login(request):
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        student = request.user.student
        if student.status == 'suspended':
            logout(request)
            messages.error(request, 'Tu cuenta ha sido SUSPENDIDA hasta nuevo aviso por el administrador del sistema.')
            return render(request, 'student_portal/login.html')
        elif student.status == 'rejected':
            logout(request)
            messages.error(request, 'Tu cuenta ha sido RECHAZADA.')
            return render(request, 'student_portal/login.html')
        return redirect('student_dashboard')
        
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user and hasattr(user, 'student'):
            student = user.student
            if student.status == 'suspended':
                messages.error(request, 'Tu cuenta ha sido SUSPENDIDA hasta nuevo aviso por el administrador del sistema.')
                return render(request, 'student_portal/login.html')
            elif student.status == 'rejected':
                messages.error(request, 'Tu cuenta ha sido RECHAZADA.')
                return render(request, 'student_portal/login.html')
            login(request, user)
            return redirect('student_dashboard')
        messages.error(request, 'Identidad no reconocida en la red.')
    return render(request, 'student_portal/login.html')

def student_logout(request):
    logout(request)
    # Consumir y limpiar todos los mensajes pendientes para evitar que aparezcan en el login
    list(messages.get_messages(request))
    return redirect('student_login')

@login_required(login_url='student_login')
@check_student_status
@check_password_change
def student_dashboard(request):
    student = request.user.student
    courses = student.courses.all()
    notifications = student.notifications.all()[:30]
    return render(request, 'student_portal/dashboard.html', {
        'student': student,
        'courses': courses,
        'notifications': notifications
    })

@login_required(login_url='student_login')
@check_student_status
@check_password_change
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    contents_queryset = course.contents.all().order_by('order', 'id')
    contents = list(contents_queryset)
    
    # Obtener progreso del estudiante
    student = request.user.student
    completed_ids = set(LessonProgress.objects.filter(student=student, completed=True).values_list('lesson_id', flat=True))

    # Determinar si cada lección está desbloqueada
    for i, content in enumerate(contents):
        if i == 0:
            content.is_unlocked = True
        else:
            prev_content = contents[i - 1]
            content.is_unlocked = prev_content.id in completed_ids

    # Validar que el curso tenga contenido
    if not contents:
        messages.warning(request, "Este curso aún no tiene lecciones disponibles.")
        return redirect('student_dashboard')

    # Obtener el tema actual (por defecto el primero incompleto o el seleccionado)
    lesson_id = request.GET.get('lesson')
    if lesson_id:
        current_lesson = get_object_or_404(CourseContent, id=lesson_id, course=course)
        # Validar si está desbloqueada
        try:
            req_index = contents.index(current_lesson)
            if req_index > 0:
                prev_lesson = contents[req_index - 1]
                if prev_lesson.id not in completed_ids:
                    messages.warning(request, "ACCESO DENEGADO: Debes completar las lecciones anteriores secuencialmente para desbloquear este nodo.")
                    # Redirigir a la primera lección incompleta desbloqueada
                    first_incomplete = None
                    for c in contents:
                        if c.id not in completed_ids:
                            first_incomplete = c
                            break
                    if not first_incomplete:
                        first_incomplete = contents[0]
                    return redirect(reverse('student_course_detail', kwargs={'pk': pk}) + f"?lesson={first_incomplete.id}")
        except ValueError:
            current_lesson = contents[0]
    else:
        # Buscar la primera lección que NO esté completada
        current_lesson = None
        for c in contents:
            if c.id not in completed_ids:
                current_lesson = c
                break
        if not current_lesson:
            current_lesson = contents[0]
    
    # Registrar acceso/desbloqueo de la lección actual
    if current_lesson:
        LessonProgress.objects.get_or_create(student=student, lesson=current_lesson)
    
    # Marcar la lección actual como completada si se solicita (por ejemplo, al dar a "Siguiente")
    if request.GET.get('complete') == '1' and current_lesson:
        # Validar si el estudiante ya entregó la tarea/taller para esta lección
        has_submission = AssignmentSubmission.objects.filter(student=student, lesson=current_lesson).exists()
        if not has_submission:
            messages.error(request, "ACCESO RESTRINGIDO: Sube tu entregable (tarea o taller) antes de completar este tema.")
            return redirect(reverse('student_course_detail', kwargs={'pk': pk}) + f"?lesson={current_lesson.id}")
            
        LessonProgress.objects.update_or_create(
            student=student, lesson=current_lesson,
            defaults={'completed': True}
        )
        
        # Actualizamos completed_ids para calcular el redireccionamiento secuencial correcto
        completed_ids.add(current_lesson.id)
        
        # Buscar la siguiente lección en la lista ordenada
        next_lesson = None
        try:
            current_index = contents.index(current_lesson)
            if current_index + 1 < len(contents):
                next_lesson = contents[current_index + 1]
        except ValueError:
            pass
            
        if next_lesson:
            return redirect(reverse('student_course_detail', kwargs={'pk': pk}) + f"?lesson={next_lesson.id}")
        else:
            messages.success(request, "¡FELICITACIONES: Has completado todos los temas de este nodo de conocimiento!")
            return redirect('student_dashboard')

    # Manejar entregas de talleres/tareas
    if request.method == 'POST' and 'assignment_file' in request.FILES:
        file = request.FILES['assignment_file']
        AssignmentSubmission.objects.create(
            student=student,
            lesson=current_lesson,
            file=file
        )
        messages.success(request, "Sincronización de entregable exitosa. En espera de evaluación neural.")
        return redirect(reverse('student_course_detail', kwargs={'pk': pk}) + f"?lesson={current_lesson.id}")

    # Obtener envío si existe
    submission = AssignmentSubmission.objects.filter(student=student, lesson=current_lesson).last()
    if submission and submission.grade is not None:
        submission.grade_five = round((submission.grade / 100) * 5, 1)

    # Verificar si todas las lecciones están completadas para liberar el parcial
    total_lessons = len(contents)
    completed_count = LessonProgress.objects.filter(student=student, lesson__course=course, completed=True).count()
    all_completed = (completed_count >= total_lessons and total_lessons > 0)

    # Manejar subida de CSV para el examen final si está liberado
    if all_completed and request.method == 'POST' and 'final_csv' in request.FILES:
        file = request.FILES['final_csv']
        # Guardamos el archivo final asociado a la última lección o creamos un registro especial
        AssignmentSubmission.objects.create(
            student=student,
            lesson=contents.last(),
            file=file,
            grade=None # Pendiente de calificar por el admin
        )
        messages.success(request, "Archivo Final (CSV) recibido. Parcial en proceso de evaluación.")
        return redirect('student_course_detail', pk=pk)

    # Retos Interactivos
    challenges = current_lesson.challenges.all() if current_lesson else []
    solved_challenge_ids = set()
    if current_lesson:
        solved_challenge_ids = set(
            ChallengeAttempt.objects.filter(
                student=student, 
                challenge__content=current_lesson, 
                is_correct=True
            ).values_list('challenge_id', flat=True)
        )

    # Calculate Extra Credit (0.1 per perfect lesson - meaning all challenges in lesson solved)
    # Just passing the values or we can calculate it dynamically for the diploma
    
    return render(request, 'student_portal/curso.html', {
        'course': course,
        'contents': contents,
        'current_lesson': current_lesson,
        'completed_ids': completed_ids,
        'student': student,
        'submission': submission,
        'all_completed': all_completed,
        'challenges': challenges,
        'solved_challenge_ids': solved_challenge_ids,
    })

@login_required(login_url='student_login')
@check_student_status
def submit_challenge(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = json.loads(request.body)
        challenge_id = data.get('challenge_id')
        selected_index = data.get('selected_index')
        
        challenge = get_object_or_404(InteractiveChallenge, id=challenge_id)
        student = request.user.student
        
        is_correct = (selected_index == challenge.correct_index)
        
        attempt, created = ChallengeAttempt.objects.get_or_create(
            student=student,
            challenge=challenge,
            defaults={'is_correct': is_correct}
        )
        
        # If they already tried and it was false, update it if it's correct now
        if not attempt.is_correct and is_correct:
            attempt.is_correct = True
            attempt.save()

        return JsonResponse({
            'success': True,
            'is_correct': is_correct,
            'feedback': challenge.feedback if not is_correct else "¡Correcto! Respuesta asimilada en la red."
        })
    return JsonResponse({'success': False}, status=400)

@login_required(login_url='student_login')
@check_student_status
def student_diploma(request, pk):
    course = get_object_or_404(Course, pk=pk)
    student = request.user.student
    
    # Verify diploma has been approved by admin
    diploma_req = DiplomaRequest.objects.filter(student=student, course=course, status='approved').first()
    if not diploma_req:
        messages.error(request, "ACCESO DENEGADO: El diploma para este curso requiere autorización del Administrador.")
        return redirect('student_stats')

    # Verify course is fully completed
    contents = course.contents.all()
    total_lessons = contents.count()
    completed_count = LessonProgress.objects.filter(student=student, lesson__course=course, completed=True).count()
    
    if completed_count < total_lessons or total_lessons == 0:
        messages.error(request, "Aún no has completado todos los nodos para obtener tu diploma.")
        return redirect('student_stats')


    # Calculate extra credit
    # 0.1 for every lesson where ALL challenges are correctly solved
    extra_credit = 0.0
    for content in contents:
        lesson_challenges = content.challenges.count()
        if lesson_challenges > 0:
            solved = ChallengeAttempt.objects.filter(student=student, challenge__content=content, is_correct=True).count()
            if solved == lesson_challenges:
                extra_credit += 0.1
                
    # Format extra credit
    extra_credit = round(extra_credit, 1)

    return render(request, 'student_portal/diploma.html', {
        'student': student,
        'course': course,
        'extra_credit': extra_credit,
        'date': timezone.now()
    })

@login_required(login_url='student_login')
@check_student_status
def take_exam(request, pk):
    course = get_object_or_404(Course, pk=pk)
    exam = course.exams.first()
    
    if request.method == 'POST':
        correct_count = 0
        total_questions = exam.questions.count()
        
        for question in exam.questions.all():
            selected_option_id = request.POST.get(f'q_{question.id}')
            if selected_option_id:
                try:
                    option = question.options.get(id=selected_option_id)
                    if option.is_correct:
                        correct_count += 1
                except Exception:
                    pass
        
        passed = (correct_count / total_questions >= 0.6) if total_questions > 0 else False
        
        attempt = ExamAttempt.objects.create(
            student=request.user.student,
            exam=exam,
            score=correct_count,
            total=total_questions,
            passed=passed,
            completed_at=timezone.now()
        )
        return redirect('exam_result', pk=pk, attempt_pk=attempt.pk)
        
    return render(request, 'student_portal/examen.html', {'exam': exam, 'course': course})

@login_required(login_url='student_login')
def exam_result(request, pk, attempt_pk):
    attempt = get_object_or_404(ExamAttempt, pk=attempt_pk)
    return render(request, 'student_portal/resultado.html', {'attempt': attempt})

@login_required(login_url='student_login')
@check_student_status
@check_password_change
def student_update_profile(request):
    student = request.user.student
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')
        
        if name: student.name = name
        if phone is not None: student.phone = phone
        if address is not None: student.address = address
        if profile_picture: student.profile_picture = profile_picture
        
        student.save()
        messages.success(request, "Perfil actualizado exitosamente en la red.")
        return redirect('student_dashboard')
        
    return render(request, 'student_portal/profile_edit.html', {'student': student})

@login_required(login_url='student_login')
@check_student_status
def student_change_password(request):
    if request.method == 'POST':
        new_pass = request.POST.get('new_password')
        confirm_pass = request.POST.get('confirm_password')
        
        # Validaciones de seguridad
        if not new_pass or new_pass != confirm_pass:
            messages.error(request, "Las contraseñas no coinciden.")
        elif len(new_pass) < 10:
            messages.error(request, "La contraseña debe tener al menos 10 caracteres.")
        elif not re.search(r'[A-Z]', new_pass):
            messages.error(request, "La contraseña debe incluir al menos una letra mayúscula.")
        elif not re.search(r'[a-z]', new_pass):
            messages.error(request, "La contraseña debe incluir al menos una letra minúscula.")
        elif not re.search(r'\d', new_pass):
            messages.error(request, "La contraseña debe incluir al menos un número.")
        elif not re.search(r'[\W_]', new_pass):
            messages.error(request, "La contraseña debe incluir al menos un carácter especial (ej. @, #, $, *).")
        else:
            # Pasa todas las validaciones
            request.user.set_password(new_pass)
            request.user.save()
            update_session_auth_hash(request, request.user) # Mantener sesión
            
            student = request.user.student
            student.generated_password = ''
            student.save()
            
            # Enviar correo de notificación
            try:
                reset_url = request.build_absolute_uri(reverse('password_reset'))
                send_password_changed_email(student, reset_url)
            except Exception as e:
                # Si falla el correo no bloqueamos el flujo, pero lo anotamos (silenciosamente aquí)
                pass
            
            messages.success(request, "Contraseña actualizada exitosamente. Protocolos de seguridad restablecidos.")
            return redirect('student_dashboard')
            
    return render(request, 'student_portal/force_password_change.html')
def student_enroll_course(request): return redirect('student_dashboard')

@login_required(login_url='student_login')
def student_mark_read(request, pk):
    student = request.user.student
    notif = get_object_or_404(Notification, pk=pk, student=student)
    notif.is_read = True
    notif.save()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'unread_count': student.unread_notifications.count()})
    return redirect(request.META.get('HTTP_REFERER', 'student_dashboard'))

@login_required(login_url='student_login')
def student_mark_all_read(request):
    student = request.user.student
    student.notifications.filter(is_read=False).update(is_read=True)
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'unread_count': 0})
    return redirect(request.META.get('HTTP_REFERER', 'student_dashboard'))

@login_required(login_url='student_login')
def student_delete_notif(request, pk):
    student = request.user.student
    notif = get_object_or_404(Notification, pk=pk, student=student)
    notif.delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'unread_count': student.unread_notifications.count()})
    return redirect(request.META.get('HTTP_REFERER', 'student_dashboard'))

@login_required(login_url='student_login')
def student_delete_all_notifs(request):
    student = request.user.student
    student.notifications.all().delete()
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'unread_count': 0})
    return redirect(request.META.get('HTTP_REFERER', 'student_dashboard'))

@login_required(login_url='student_login')
def student_notifications_count(request):
    student = request.user.student
    count = student.unread_notifications.count()
    return JsonResponse({'count': count})

@login_required(login_url='student_login')
@check_student_status
def student_stats(request):
    student = request.user.student
    courses = student.courses.all()
    
    course_stats = []
    total_avg = 0
    
    for course in courses:
        total_lessons = course.contents.count()
        completed_lessons = LessonProgress.objects.filter(student=student, lesson__course=course, completed=True).count()
        progress_pct = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        
        submissions = AssignmentSubmission.objects.filter(student=student, lesson__course=course, grade__isnull=False)
        avg_grade = 0
        if submissions.exists():
            raw_avg = sum(s.grade for s in submissions) / submissions.count()
            avg_grade = round((raw_avg / 100) * 5, 1)
        
        status = "APROBADO" if avg_grade >= 3.0 else "EN PROCESO"
        if not submissions.exists(): status = "SIN NOTAS"

        exam = course.exams.first()
        exam_passed = False
        exam_grade = 0.0
        if exam:
            latest_attempt = ExamAttempt.objects.filter(student=student, exam=exam).order_by('-started_at').first()
            if latest_attempt and latest_attempt.total > 0:
                exam_grade = round((latest_attempt.score / latest_attempt.total) * 5.0, 1)
                if exam_grade >= 3.0:
                    exam_passed = True

        is_eligible = (int(progress_pct) == 100 and exam_passed)
        diploma_req = DiplomaRequest.objects.filter(student=student, course=course).first()
        diploma_status = diploma_req.status if diploma_req else ('eligible' if is_eligible else 'not_eligible')

        course_stats.append({
            'course': course,
            'progress': int(progress_pct),
            'pending': 100 - int(progress_pct),
            'avg_grade': avg_grade,
            'status': status,
            'diploma_status': diploma_status,
            'exam_grade': exam_grade,
            'exam_passed': exam_passed,
        })
        total_avg += avg_grade

    overall_avg = round(total_avg / courses.count(), 1) if courses.exists() else 0

    return render(request, 'student_portal/estadisticas.html', {
        'student': student,
        'course_stats': course_stats,
        'overall_avg': overall_avg
    })

@login_required(login_url='student_login')
@check_student_status
def student_request_diploma(request, pk):
    if request.method == 'POST':
        student = request.user.student
        course = get_object_or_404(Course, pk=pk)
        
        # Verify eligibility
        total_lessons = course.contents.count()
        completed_lessons = LessonProgress.objects.filter(student=student, lesson__course=course, completed=True).count()
        progress_pct = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        
        exam = course.exams.first()
        exam_passed = False
        exam_grade = 0.0
        if exam:
            latest_attempt = ExamAttempt.objects.filter(student=student, exam=exam).order_by('-started_at').first()
            if latest_attempt and latest_attempt.total > 0:
                exam_grade = round((latest_attempt.score / latest_attempt.total) * 5.0, 1)
                if exam_grade >= 3.0:
                    exam_passed = True
            
        if progress_pct == 100 and exam_passed:
            req, created = DiplomaRequest.objects.get_or_create(student=student, course=course)
            if created:
                # Create admin notification
                AdminNotification.objects.create(
                    title=f"Solicitud de Diploma: {student.name}",
                    message=f"El estudiante {student.name} ha solicitado el diploma para el curso '{course.title}'. Calificación examen final: {exam_grade}/5.0",
                    notif_type='diploma',
                    link='/admin/' # Let's link it to admin panel dashboard
                )
                messages.success(request, "Solicitud de diploma enviada exitosamente. En espera de autorización del administrador.")
            else:
                messages.info(request, "Ya existe una solicitud de diploma en curso para este nodo.")
        else:
            messages.error(request, "Aún no cumples con los requisitos (100% progreso y calificación de examen final >= 3.0) para solicitar el diploma.")
            
    return redirect('student_stats')

def get_unified_cognitive_response(message):
    msg_lower = message.lower()
    
    # 1. Swear words filter (sin groserias)
    profanities = [
        'mierda', 'puta', 'puto', 'carajo', 'pendejo', 'joder', 'cabron', 
        'marica', 'maricon', 'hijo de puta', 'malparido', 'mierd', 'culiao'
    ]
    for bad_word in profanities:
        if bad_word in msg_lower:
            return "**[COGNITUS-IA]**: ⚠️ *Protocolo de Convivencia:* Por favor, mantén un lenguaje respetuoso y libre de términos ofensivos dentro de la plataforma académica."
            
    # 2. Check pertinence (solo preguntas pertinentes)
    off_topic_words = [
        'pizza', 'receta', 'cocina', 'comida', 'hamburguesa', 'sushi', 'chiste', 'broma',
        'futbol', 'deporte', 'musica', 'cancion', 'juego', 'playstation', 'xbox', 'cine',
        'pelicula', 'politica', 'presidente', 'partido politico', 'baile', 'moda'
    ]
    for off_word in off_topic_words:
        if off_word in msg_lower:
            return (
                "**[COGNITUS-IA]**: ⚠️ *Filtro de Pertinencia:* Para mantener el enfoque académico del portal, "
                "por favor realiza consultas que sean pertinentes a tu formación o al funcionamiento de la plataforma."
            )
            
    # 3. Comprehensive Knowledge Base (All courses combined!)
    knowledge_base = {
        # Módulo 1: Fundamentos de IA
        'turing': (
            "**Alan Turing (Juego de la Imitación, 1950):** propuso evaluar la inteligencia artificial a través del conductismo lógico. "
            "Un evaluador ciego conversa por texto con una máquina y un humano. Si no logra distinguirlos tras 5 minutos, la máquina aprueba. "
            "John Searle criticó esto con su famoso experimento de la *Habitación China*, demostrando que la manipulación sintáctica "
            "de símbolos no equivale en ningún caso a comprensión semántica real."
        ),
        'difus': (
            "**Lógica Difusa (Lotfi Zadeh, 1965):** matematiza la incertidumbre lingüística. A diferencia de los conjuntos clásicos binarios (0 o 1), "
            "en los conjuntos difusos los elementos poseen un grado de pertenencia continuo $\\mu_A(x)$ acotado en el intervalo $[0, 1]$. "
            "Es fundamental para modelar sistemas con transiciones mecánicas suaves (como frenado automático o temperatura de calderas)."
        ),
        'percept': (
            "**Perceptrón de Frank Rosenblatt (1958):** es el modelo base de una neurona lineal. Calcula $z = \\mathbf{w}^T \\mathbf{x} + b$ "
            "y aplica una función escalón no lineal de Heaviside. Marvin Minsky y Seymour Papert sepultaron la investigación conexionista inicial en 1969 al "
            "demostrar matemáticamente que un perceptrón simple es incapaz de aprender compuertas no lineales simples como XOR."
        ),
        'neur': (
            "**Redes Neuronales y MLP (Perceptrón Multicapa):** apilan capas de perceptrones (entrada, ocultas y salida) "
            "para modelar no-linealidades complejas. El *Teorema de Aproximación Universal (Hornik, Cybenko)* demuestra matemáticamente que una "
            "sola capa oculta con suficientes neuronas y activaciones continuas no lineales puede aproximar cualquier función continua."
        ),
        'activac': (
            "**Funciones de Activación:** dotan a la red de capacidad representacional no lineal. "
            "La *Sigmoide* escala a $[0, 1]$ ($\\sigma(z) = \\frac{1}{1 + e^{-z}}$), ideal para probabilidad de salida. "
            "La *ReLU* ($f(z) = \\max(0, z)$) acelera el cómputo y previene el desvanecimiento de gradiente en redes profundas."
        ),
        'backprop': (
            "**Retropropagación (Backpropagation):** calcula de forma sumamente eficiente las derivadas parciales de la pérdida total "
            "con respecto a cada peso y sesgo de la red. Aplica recursivamente la *Regla de la Cadena* del cálculo diferencial desde la capa de salida "
            "hacia las ocultas, resolviendo la actualización de parámetros para redes complejas."
        ),
        'gradien': (
            "**Descenso del Gradiente (Gradient Descent):** algoritmo iterativo que desplaza los pesos del modelo en la dirección opuesta al gradiente "
            "de la función de pérdida para localizar el mínimo local: $\\mathbf{w} \\leftarrow \\mathbf{w} - \\eta \\nabla J(\\mathbf{w})$. "
            "La Tasa de Aprendizaje ($\\eta$) controla la longitud del paso en cada iteración."
        ),
        'convol': (
            "**Redes Convolucionales (CNN):** el estándar absoluto para visión artificial. Utilizan filtros o *kernels* locales que se deslizan sobre "
            "la imagen para extraer características espaciales invariantes (bordes, texturas) minimizando el número de parámetros por compartición de pesos."
        ),
        'nlp': (
            "**Procesamiento de Lenguaje Natural (NLP) y Transformers (2017):** revolucionó el campo al eliminar el procesamiento secuencial "
            "de las recurrentes (RNN). Usa el mecanismo de *Auto-Atención* para sopesar la relevancia contextual de todas las palabras de forma paralela."
        ),
        
        # Módulo 2: Regresión Lineal
        'covarian': (
            "**Covarianza Muestral ($s_{xy}$):** mide la dirección de la asociación lineal de dos variables conjuntas. "
            "El *Coeficiente de Pearson ($r$)* normaliza esta métrica dividiéndola por el producto de las desviaciones estándar, "
            "acotándose en el rango $[-1, 1]$ para indicar la fuerza absoluta de la relación lineal."
        ),
        'ols': (
            "**Mínimos Cuadrados Ordinarios (OLS):** minimiza analíticamente la Suma de Residuos al Cuadrado (SSR): "
            "$S = \\sum (y_i - (\\beta_0 + \\beta_1 x_i))^2$. Al derivar e igualar a cero, se deducen los coeficientes óptimos: "
            "pendiente $\\hat{\\beta}_1 = \\frac{Cov(X, Y)}{Var(X)}$ e intercepto $\\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1 \\bar{x}$."
        ),
        'error': (
            "**Métricas de Ajuste Continuo:** evaluamos la precisión del modelo predictivo. "
            "El *MSE* promedia los errores al cuadrado, penalizando desviaciones drásticas. "
            "El *RMSE* es la raíz del MSE, y el *$R^2$ (Coeficiente de Determinación)* nos indica el porcentaje de varianza explicada por la recta."
        ),
        'residua': (
            "**Análisis de Residuos ($e = y - \\hat{y}$):** obligatorio para certificar los supuestos de Gauss-Markov. "
            "Debemos verificar gráficamente la *Homocedasticidad* (varianza del error constante) y la normalidad mediante gráficos Q-Q."
        ),
        'dummy': (
            "**Variables Dummy (One-Hot Encoding):** codifica texto categórico en columnas binarias (0 o 1). "
            "Para evitar la trampa de la variable dummy (multicolinealidad perfecta que rompe el cálculo matricial), "
            "siempre debemos excluir una columna, la cual sirve de categoría de base referencial."
        ),
        'logístic': (
            "**Regresión Logística:** clasificador lineal binario. Mapea la combinación matemática de variables continuas al rango "
            "probabilístico $[0, 1]$ usando la función sigmoide: $p = \\frac{1}{1 + e^{-z}}$. El logaritmo de los momios (log-odds) se denomina enlace *Logit*."
        ),
        'confusi': (
            "**Matriz de Confusión:** tabla de contingencia de $2 \\times 2$ para evaluar clasificadores binarios. "
            "Tabula Verdaderos Positivos (TP), Verdaderos Negativos (TN), Falsos Positivos (FP) y Falsos Negativos (FN), permitiendo derivar "
            "métricas de *Accuracy*, *Precision*, *Recall* (Sensibilidad) y el valor armónico *F1-Score*."
        ),
        'multicolineal': (
            "**Multicolinealidad:** ocurre cuando las variables predictoras independientes están correlacionadas entre sí, "
            "inflando los errores estándar de los coeficientes. Se diagnostica con el *Factor de Inflación de la Varianza (VIF)*: "
            "$VIF_j = \\frac{1}{1 - R_j^2}$. Si $VIF \\ge 10$, se debe depurar el modelo."
        ),
        'regulariz': (
            "**Regularización:** previene el sobreajuste (overfitting) aplicando penalizaciones. "
            "*Ridge (L2)* suma los pesos al cuadrado ($\\lambda \\sum \\beta^2$) reduciendo los coeficientes suavemente. "
            "*Lasso (L1)* suma el valor absoluto de los pesos ($\\lambda \\sum |\\beta|$) encogiendo coeficientes a exactamente cero para selección de variables."
        ),
        
        # Módulo 3: Computación Evolutiva
        'darwin': (
            "**Darwinismo Digital (Holland, 1975):** imita los operadores evolutivos de la naturaleza. "
            "Una población de cromosomas (soluciones candidatas) evoluciona a través de generaciones compitiendo bajo presión selectiva, "
            "recombinación (cruce) y mutación aleatoria para converger hacia óptimos globales de paisajes sumamente difíciles."
        ),
        'gen': (
            "**Codificación del Genoma:** mapea las variables reales a estructuras digitales. "
            "El *Gen* es el parámetro unitario, el *Cromosoma* es la cadena indexada de genes (solución), el *Genotipo* "
            "es la estructura interna codificada (ej. binario) y el *Fenotipo* es la decodificación y expresión física real evaluable."
        ),
        'fitness': (
            "**Función de Aptitud (Fitness Function):** es la métrica de éxito evolutivo. Evalúa y cuantifica la adaptación de un fenotipo. "
            "En problemas de minimización de costes, se suele reformular la aptitud de manera inversa: $Fitness(x) = \\frac{1}{Coste(x) + \\epsilon}$."
        ),
        'paisaje': (
            "**Paisaje de Aptitud (Fitness Landscape):** representación geométrica donde las variables de genes forman la base "
            "y la altura representa el fitness. En paisajes rugosos repletos de óptimos locales, los operadores de cruce poblacionales "
            "permiten 'saltar' valles, superando a optimizadores locales puros."
        ),
        'selecci': (
            "**Operador de Selección:** determina qué individuos transmiten su material genético. "
            "La *Ruleta* otorga probabilidades proporcionales directas al fitness ($p_i = \\frac{F_i}{\\sum F_j}$). "
            "El *Torneo* confronta $k$ individuos al azar para que gane el más apto, controlando fácilmente la presión de selección."
        ),
        'crossover': (
            "**Cruce o Recombinación (Crossover):** modela la EXPLOTACIÓN. Combina material genético de dos padres buenos "
            "bajo una probabilidad $p_c$ (típicamente $80\\%$) para engendrar hijos que reúnan las virtudes de ambos. Puede ser de un punto, dos puntos o uniforme."
        ),
        'mutaci': (
            "**Operador de Mutación:** modela la EXPLORACIÓN. Introduce variaciones aleatorias e invierte bits con una tasa muy baja $p_m$ "
            "($\\approx \\frac{1}{Longitud}$), garantizando la diversidad del pool genético y permitiendo escapar de los valles del paisaje."
        ),
        'elitismo': (
            "**Elitismo:** clona y resguarda directamente a los mejores individuos de la generación actual a la siguiente "
            "antes de aplicar operadores destructivos, garantizando matemáticamente que la aptitud máxima sea una función estrictamente no decreciente."
        ),
        'viajero': (
            "**Problema del Viajero (TSP) y Cruce OX:** requiere codificación permutacional sin duplicados. El cruce estándar generaría rutas inviables. "
            "El *Cruce de Orden (OX)* resuelve esto copiando un segmento central y rellenando circularmente el resto preservando el orden relativo."
        ),
        'enjambre': (
            "**Optimización por Enjambre de Partículas (PSO):** modela el comportamiento de bandadas en vuelo continuo. "
            "Las partículas actualizan iterativamente su vector de velocidad agregando fuerza de inercia ($w$), memoria individual cognitiva ($c_1$) "
            "y socialización colectiva ($c_2$): $\\mathbf{v}^{(t+1)} = w \\mathbf{v}^{(t)} + c_1 r_1 (\\mathbf{p} - \\mathbf{x}) + c_2 r_2 (\\mathbf{g} - \\mathbf{x})$."
        ),
        
        # General Portal
        'nota': (
            "Tus tareas y talleres se califican de **0.0 a 5.0**. Si el docente ha revisado tu entrega, verás la nota y "
            "la retroalimentación correspondiente en el panel de la lección del curso respectivo. Los exámenes se auto-califican al instante."
        ),
        'calificac': (
            "Tus tareas y talleres se califican de **0.0 a 5.0**. Si el docente ha revisado tu entrega, verás la nota y "
            "la retroalimentación correspondiente en el panel de la lección del curso respectivo. Los exámenes se auto-califican al instante."
        ),
        'perfil': (
            "Puedes actualizar tus datos personales (Nombre, Apellido, Email) en la sección **'Editar Perfil'** desde el menú "
            "y gestionar tus credenciales de seguridad en **'Cambiar Contraseña'** para mantener tu cuenta resguardada."
        ),
        'password': (
            "Puedes actualizar tus datos personales (Nombre, Apellido, Email) en la sección **'Editar Perfil'** desde el menú "
            "y gestionar tus credenciales de seguridad en **'Cambiar Contraseña'** para mantener tu cuenta resguardada."
        ),
        'contrase': (
            "Puedes actualizar tus datos personales (Nombre, Apellido, Email) en la sección **'Editar Perfil'** desde el menú "
            "y gestionar tus credenciales de seguridad en **'Cambiar Contraseña'** para mantener tu cuenta resguardada."
        ),
        'soporte': (
            "Si tienes inconvenientes técnicos o administrativos, comunícate con la dirección académica del laboratorio a través del correo institucional."
        ),
        'ayuda': (
            "Como asistente general **COGNITUS-IA**, puedo explicarte el contenido de los cursos de la plataforma, "
            "ayudarte con el funcionamiento de la interfaz de tareas, calificaciones, edición de tu perfil o restablecimiento de credenciales."
        )
    }
    
    # Match keyword
    matched_response = None
    for kw, resp in knowledge_base.items():
        if kw in msg_lower:
            matched_response = resp
            break
            
    if matched_response:
        return f"**[COGNITUS-IA]**: {matched_response}"
        
    # Standard academic response for general non-matched queries (allow any pertinent query!)
    return (
        f"**[COGNITUS-IA]**: Hola. He procesado tu consulta de manera cognitiva. "
        f"Como asistente unificado de la plataforma, estoy capacitado para responder dudas sobre todos nuestros cursos. "
        f"¿Deseas profundizar sobre el **Test de Turing**, **Lógica Difusa**, **Perceptrones**, **Mínimos Cuadrados Ordinarios (OLS)**, "
        f"**Colinealidad (VIF)**, **Regularización Lasso/Ridge**, **Cromosomas de Algoritmos Genéticos (Cruce OX)** o **Enjambres PSO**? "
        f"Por favor, formula tu duda técnica y con gusto te proveeré un análisis detallado."
    )

@csrf_exempt
@login_required(login_url='student_login')
def student_course_chat(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'Sólo se permiten solicitudes POST.'}, status=405)
        
    try:
        data = json.loads(request.body)
        message = data.get('message', '').strip()
    except ValueError:
        return JsonResponse({'error': 'Carga útil JSON inválida.'}, status=400)
        
    if not message:
        return JsonResponse({'response': '¿En qué puedo asistirte académicamente hoy?', 'reply': '¿En qué puedo asistirte académicamente hoy?'})
        
    ai_resp = get_unified_cognitive_response(message)
    return JsonResponse({'response': ai_resp, 'reply': ai_resp})

@csrf_exempt
@login_required(login_url='student_login')
def student_dashboard_chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Sólo se permiten solicitudes POST.'}, status=405)
        
    try:
        data = json.loads(request.body)
        message = data.get('message', '').strip()
    except ValueError:
        return JsonResponse({'error': 'Carga útil JSON inválida.'}, status=400)
        
    if not message:
        return JsonResponse({'response': '¿En qué puedo asistirte hoy con respecto a tus cursos o plataforma?', 'reply': '¿En qué puedo asistirte hoy con respecto a tus cursos o plataforma?'})
        
    ai_resp = get_unified_cognitive_response(message)
    return JsonResponse({'response': ai_resp, 'reply': ai_resp})
