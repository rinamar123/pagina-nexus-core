from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from enrollment.models import Student, Course, EnrollmentRequest
from notificaciones.models import Notification, AdminNotification
from student_portal.models import LessonProgress, AssignmentSubmission, DiplomaRequest
from panel.models import AdminRequest
from email_service.services import send_student_welcome_email, send_enrollment_rejected_email, send_student_deleted_email, send_student_accepted_email, send_student_suspended_email
from django.http import JsonResponse
from django.utils import timezone


def is_admin(user):
    return user.is_authenticated and user.is_staff

def generate_random_password(length=10):
    # Usaremos una contraseña predecible por defecto para facilitar las pruebas
    return 'Iacademy2026*'

def admin_login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        messages.error(request, 'Identificación fallida. Acceso denegado.')
    return render(request, 'panel/login.html')

def admin_logout(request):
    logout(request)
    # Consumir y limpiar todos los mensajes pendientes para evitar que aparezcan en el login
    list(messages.get_messages(request))
    return redirect('admin_login')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def dashboard(request):
    # Solicitudes pendientes siempre visibles arriba
    pending_requests = EnrollmentRequest.objects.filter(status='pending').order_by('-created_at')
    
    # Todos los estudiantes en el sistema (Lista General)
    all_students = Student.objects.all().order_by('-created_at')
    
    # Cursos para el filtro
    courses = Course.objects.all()
    
    # Filtrado por curso
    course_filter = request.GET.get('course')
    if course_filter:
        all_students = all_students.filter(courses__id=course_filter)

    # Métricas para el Dashboard
    course_metrics = []
    for c in courses:
        # Estudiantes por curso
        students_in_course = c.students.count()
        # Promedio del curso
        submissions = AssignmentSubmission.objects.filter(lesson__course=c, grade__isnull=False)
        avg = 0
        if submissions.exists():
            raw_avg = sum(s.grade for s in submissions) / submissions.count()
            avg = round((raw_avg / 100) * 5, 1)
        
        course_metrics.append({
            'title': c.title,
            'students': students_in_course,
            'avg': avg
        })

    # Estudiantes modificados recientemente (ordenados por fecha de actualización, excluyendo los quitados manualmente de la vista)
    excluded_ids = request.session.get('excluded_recent_students', [])
    recently_modified = Student.objects.exclude(id__in=excluded_ids).order_by('-updated_at')[:4]

    courses_count = courses.count()
    students_count = Student.objects.count()
    pending_count = EnrollmentRequest.objects.filter(status='pending').count()
    
    # Diploma Requests (both pending and all for records)
    diploma_requests = DiplomaRequest.objects.all().order_by('-requested_at')
    pending_diplomas_count = DiplomaRequest.objects.filter(status='pending').count()

    # Admin Requests
    admin_requests = AdminRequest.objects.all().order_by('-requested_at')
    
    # Active Admins list
    active_admins = User.objects.filter(is_active=True, is_staff=True).order_by('username')

    return render(request, 'panel/dashboard.html', {
        'pending_requests': pending_requests,
        'students': all_students,
        'courses': courses,
        'selected_course': int(course_filter) if course_filter else None,
        'courses_count': courses_count,
        'students_count': students_count,
        'pending_count': pending_count,
        'course_metrics': course_metrics,
        'recently_modified': recently_modified,
        'diploma_requests': diploma_requests,
        'pending_diplomas_count': pending_diplomas_count,
        'admin_requests': admin_requests,
        'active_admins': active_admins,
    })


@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def enrollment_accept(request, pk):
    enroll_req = get_object_or_404(EnrollmentRequest, pk=pk)
    student = enroll_req.student
    course = enroll_req.course
    
    temp_password = generate_random_password()

    if not student.user:
        username = student.email.split('@')[0]
        user, created = User.objects.get_or_create(username=username, email=student.email)
        user.set_password(temp_password)
        user.save()
        student.user = user

    student.generated_password = temp_password
        
    student.status = 'accepted'
    student.courses.add(course)
    student.save()
    
    enroll_req.status = 'accepted'
    enroll_req.save()
    
    Notification.objects.create(
        student=student, 
        title='Sincronización Exitosa', 
        message=f'Has sido aceptado en el curso: {course.title}.', 
        notif_type='success'
    )
    
    try:
        send_student_welcome_email(student, student.generated_password)
        messages.success(request, f'Estudiante {student.name} aceptado en {course.title}. Contraseña: {student.generated_password}. ¡Email enviado con éxito!')
    except:
        messages.warning(request, f'Estudiante {student.name} aceptado en {course.title}, pero hubo un error al enviar el email. Contraseña inicial del estudiante: {student.generated_password}')
    
    return redirect('admin_dashboard')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def enrollment_reject(request, pk):
    enroll_req = get_object_or_404(EnrollmentRequest, pk=pk)
    student = enroll_req.student
    course = enroll_req.course
    
    student.status = 'rejected'
    student.save()
    
    enroll_req.status = 'rejected'
    enroll_req.save()
    
    try:
        send_enrollment_rejected_email(student, course)
        messages.success(request, f'Solicitud de {student.name} para {course.title} rechazada. Correo enviado.')
    except Exception as e:
        messages.warning(request, f'Solicitud rechazada, pero falló el envío del correo: {e}')
        
    return redirect('admin_dashboard')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    courses = Course.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        level = request.POST.get('level')
        status = request.POST.get('status')
        selected_courses = request.POST.getlist('courses')
        
        old_status = student.status
        
        # Sincronizar el User de Django asociado
        if student.user:
            u = student.user
            u.email = email
            u.username = email.split('@')[0]
            u.save()
            
        student.name = name
        student.email = email
        student.phone = phone
        student.address = address
        student.level = level
        student.status = status
        student.save()
        
        # Vincular cursos seleccionados
        student.courses.set(selected_courses)
        
        if old_status != status:
            if status == 'accepted':
                try:
                    send_student_accepted_email(student)
                    messages.success(request, f'¡Estudiante {student.name} actualizado con éxito! Correo de aceptación enviado.')
                except Exception as e:
                    messages.warning(request, f'¡Estudiante {student.name} actualizado, pero falló el envío del correo de aceptación: {e}')
            elif status == 'suspended':
                try:
                    send_student_suspended_email(student)
                    messages.success(request, f'¡Estudiante {student.name} actualizado con éxito! Correo de suspensión enviado.')
                except Exception as e:
                    messages.warning(request, f'¡Estudiante {student.name} actualizado, pero falló el envío del correo de suspensión: {e}')
            elif status == 'rejected':
                try:
                    send_enrollment_rejected_email(student)
                    messages.success(request, f'¡Estudiante {student.name} actualizado con éxito! Correo de rechazo enviado.')
                except Exception as e:
                    messages.warning(request, f'¡Estudiante {student.name} actualizado, pero falló el envío del correo de rechazo: {e}')
            else:
                messages.success(request, f'¡Estudiante {student.name} actualizado con éxito!')
        else:
            messages.success(request, f'¡Estudiante {student.name} actualizado con éxito!')
            
        return redirect('admin_dashboard')
        
    return render(request, 'panel/student_edit.html', {
        'student': student,
        'courses': courses,
    })

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def student_delete(request, pk):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=pk)
        name = student.name
        email = student.email
        if student.user:
            student.user.delete()
        student.delete()
        
        try:
            send_student_deleted_email(name, email)
            messages.success(request, f'El estudiante {name} y su cuenta asociada han sido eliminados de forma permanente. Correo enviado.')
        except Exception as e:
            messages.warning(request, f'El estudiante {name} fue eliminado, pero falló el envío del correo: {e}')
    return redirect('admin_dashboard')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def notifications_view(request):
    return render(request, 'panel/notifications.html')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def course_list(request):
    return render(request, 'panel/course_list.html')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def grade_assignments(request):
    # Obtener todos los estudiantes aceptados
    students = Student.objects.filter(status='accepted').order_by('name')
    
    # Calcular entregas pendientes para cada estudiante
    for s in students:
        s.pending_count = s.submissions.filter(grade__isnull=True).count()
        
    selected_student_id = request.GET.get('student_id')
    selected_lesson_id = request.GET.get('lesson_id')
    
    selected_student = None
    student_courses_data = []
    selected_submission = None
    
    if selected_student_id:
        selected_student = get_object_or_404(Student, id=selected_student_id)
        # Cursos en los que está inscrito el estudiante
        courses = selected_student.courses.prefetch_related('contents').all()
        
        for c in courses:
            lessons_data = []
            for cc in c.contents.all():
                # Entrega de este estudiante para esta lección específica
                sub = AssignmentSubmission.objects.filter(student=selected_student, lesson=cc).last()
                status = 'no_submission'
                grade_five = None
                
                if sub:
                    if sub.grade is not None:
                        status = 'graded'
                        grade_five = round((sub.grade / 100) * 5, 1)
                    else:
                        status = 'pending'
                        
                lessons_data.append({
                    'lesson': cc,
                    'submission': sub,
                    'status': status,
                    'grade_five': grade_five
                })
            student_courses_data.append({
                'course': c,
                'lessons': lessons_data
            })
            
        if selected_lesson_id:
            # Obtener el taller específico
            selected_submission = AssignmentSubmission.objects.filter(student=selected_student, lesson_id=selected_lesson_id).last()
            if selected_submission and selected_submission.grade is not None:
                selected_submission.grade_five = round((selected_submission.grade / 100) * 5, 1)

    return render(request, 'panel/grade_assignments.html', {
        'students': students,
        'selected_student': selected_student,
        'courses_data': student_courses_data,
        'selected_submission': selected_submission,
        'selected_student_id': int(selected_student_id) if selected_student_id else None,
        'selected_lesson_id': int(selected_lesson_id) if selected_lesson_id else None,
    })

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def submit_grade(request, submission_id):
    if request.method == 'POST':
        submission = get_object_or_404(AssignmentSubmission, pk=submission_id)
        raw_grade = request.POST.get('grade')
        feedback = request.POST.get('feedback', '')
        
        try:
            grade_float = float(raw_grade)
            if 0.0 <= grade_float <= 5.0:
                # Almacenar en escala 100
                submission.grade = int(grade_float * 20)
            else:
                messages.error(request, 'La calificación debe estar entre 0.0 y 5.0.')
                return redirect(request.META.get('HTTP_REFERER', 'admin_grade_assignments'))
        except ValueError:
            messages.error(request, 'Calificación numérica inválida.')
            return redirect(request.META.get('HTTP_REFERER', 'admin_grade_assignments'))
            
        submission.feedback = feedback
        submission.save()
        
        # Crear notificación para el estudiante
        Notification.objects.create(
            student=submission.student,
            title='Taller Calificado 📝',
            message=f'Tu entrega en "{submission.lesson.title}" fue calificada con {grade_float}/5.0.',
            notif_type='success'
        )
        
        messages.success(request, f'¡Calificación registrada con éxito para {submission.student.name}! Nota: {grade_float}/5.0')
        
    return redirect(request.META.get('HTTP_REFERER', 'admin_grade_assignments'))

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_diploma_approve(request, pk):
    req = get_object_or_404(DiplomaRequest, pk=pk)
    req.status = 'approved'
    req.approved_at = timezone.now()
    req.save()
    
    # Notify Student
    Notification.objects.create(
        student=req.student,
        title="Diploma Autorizado 🎓",
        message=f"¡Felicidades! Tu diploma para el curso '{req.course.title}' ha sido autorizado. Ya puedes descargarlo en tu panel de estadísticas.",
        notif_type='success'
    )
    
    messages.success(request, f"Se ha aprobado la solicitud de diploma para {req.student.name} - {req.course.title}.")
    return redirect('admin_dashboard')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_diploma_reject(request, pk):
    req = get_object_or_404(DiplomaRequest, pk=pk)
    req.status = 'rejected'
    req.save()
    
    # Notify Student
    Notification.objects.create(
        student=req.student,
        title="Solicitud de Diploma Rechazada ⚠️",
        message=f"Tu solicitud de diploma para el curso '{req.course.title}' fue rechazada por el administrador. Contacta soporte para más información.",
        notif_type='warning'
    )
    
    messages.warning(request, f"Se ha rechazado la solicitud de diploma para {req.student.name} - {req.course.title}.")
    return redirect('admin_dashboard')

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_notifications_json(request):
    notifications = AdminNotification.objects.all().order_by('-created_at')
    data = []
    for n in notifications:
        data.append({
            'id': n.id,
            'title': n.title,
            'message': n.message,
            'notif_type': n.notif_type,
            'is_read': n.is_read,
            'created_at': n.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        })
    return JsonResponse({'notifications': data})

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_mark_read_notification(request, pk):
    n = get_object_or_404(AdminNotification, pk=pk)
    n.is_read = True
    n.save()
    return JsonResponse({'success': True})

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_delete_notification(request, pk):
    n = get_object_or_404(AdminNotification, pk=pk)
    n.delete()
    return JsonResponse({'success': True})

@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_clear_all_notifications(request):
    AdminNotification.objects.all().delete()
    return JsonResponse({'success': True})


def admin_signup(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')
        
    if request.method == 'POST':
        u = request.POST.get('username')
        email = request.POST.get('email')
        p = request.POST.get('password')
        pc = request.POST.get('password_confirm')
        
        # Validations
        if p != pc:
            return render(request, 'panel/admin_signup.html', {
                'error_msg': 'Las contraseñas no coinciden.',
                'prefill_username': u,
                'prefill_email': email
            })
        if len(p) < 8:
            return render(request, 'panel/admin_signup.html', {
                'error_msg': 'La contraseña debe tener al menos 8 caracteres.',
                'prefill_username': u,
                'prefill_email': email
            })
        if User.objects.filter(username=u).exists():
            return render(request, 'panel/admin_signup.html', {
                'error_msg': 'El nombre de usuario ya está registrado en el sistema.',
                'prefill_username': u,
                'prefill_email': email
            })
        if User.objects.filter(email=email).exists():
            return render(request, 'panel/admin_signup.html', {
                'error_msg': 'La dirección de correo electrónico ya está registrada.',
                'prefill_username': u,
                'prefill_email': email
            })
            
        # Create Inactive user
        user = User.objects.create_user(username=u, email=email, password=p)
        user.is_active = False
        user.is_staff = True
        user.is_superuser = True
        user.save()
        
        # Create AdminRequest
        admin_req = AdminRequest.objects.create(user=user)
        
        # Get client IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        admin_req.ip_address = ip
        admin_req.save()
        
        # Create AdminNotification
        verify_url = f"/admin/solicitudes-admin/verificar/{admin_req.token}/"
        AdminNotification.objects.create(
            title="Nueva Solicitud de Acceso Admin 🛡️",
            message=f"El usuario '{u}' ({email}) solicita acceso administrativo. Haga clic para verificar: {verify_url}",
            notif_type='warning'
        )
        
        return render(request, 'panel/admin_signup.html', {
            'success_msg': 'Su solicitud de acceso administrativo ha sido registrada. Se ha enviado el token de verificación al Administrador Principal.'
        })
        
    return render(request, 'panel/admin_signup.html')


@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_request_verify(request, token):
    req = get_object_or_404(AdminRequest, token=token)
    
    if req.is_approved:
        messages.warning(request, f"La solicitud de {req.user.username} ya había sido aprobada previamente.")
        return redirect('admin_dashboard')
        
    # Approve request
    req.is_approved = True
    req.save()
    
    # Activate User
    req.user.is_active = True
    req.user.save()
    
    messages.success(request, f"Acceso administrativo para {req.user.username} habilitado con éxito. Ahora puede iniciar sesión.")
    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def admin_request_reject(request, token):
    req = get_object_or_404(AdminRequest, token=token)
    username = req.user.username
    
    # Mark as rejected (no deletion to keep audit proof)
    req.is_approved = False
    req.is_rejected = True
    req.save()
    
    # Ensure user stays inactive
    req.user.is_active = False
    req.user.save()
    
    messages.warning(request, f"Se ha denegado la solicitud de acceso de {username}. Se conservan los registros como prueba.")
    return redirect('admin_dashboard')


@login_required(login_url='admin_login')
@user_passes_test(is_admin, login_url='admin_login')
def download_database(request):
    import zipfile
    import os
    from io import BytesIO
    from django.http import HttpResponse
    from django.core.serializers import serialize
    from django.conf import settings
    
    # Create an in-memory zip file
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # 1. Serialize models to JSON
        models_to_backup = [
            (User, 'users.json'),
            (Student, 'students.json'),
            (Course, 'courses.json'),
            (EnrollmentRequest, 'enrollment_requests.json'),
            (DiplomaRequest, 'diploma_requests.json'),
            (AdminRequest, 'admin_requests.json'),
            (AssignmentSubmission, 'assignment_submissions.json'),
            (LessonProgress, 'lesson_progress.json'),
        ]
        
        for model, filename in models_to_backup:
            try:
                data = serialize('json', model.objects.all(), indent=2)
                zip_file.writestr(filename, data)
            except Exception as e:
                zip_file.writestr(f"error_{filename}", f"Error serializing {model.__name__}: {str(e)}")

        # 2. Add raw SQLite database if it exists
        sqlite_path = settings.DATABASES['default'].get('NAME')
        if sqlite_path and os.path.exists(sqlite_path):
            try:
                zip_file.write(sqlite_path, arcname='db.sqlite3')
            except Exception as e:
                zip_file.writestr('sqlite_error.txt', f"Error backing up sqlite file: {str(e)}")

    buffer.seek(0)
    response = HttpResponse(buffer.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="nexus_core_backup.zip"'
    return response

def exclude_recent_student(request, student_id):
    if not (request.user.is_authenticated and request.user.is_staff):
        return redirect('admin_login')
    
    if request.method == 'POST':
        excluded = request.session.get('excluded_recent_students', [])
        if student_id not in excluded:
            excluded.append(student_id)
            request.session['excluded_recent_students'] = excluded
            request.session.modified = True
            
    return redirect('admin_dashboard')
