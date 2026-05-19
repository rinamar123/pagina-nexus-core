from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Student, Course, CourseContent, Exam, CourseFile, EnrollmentRequest
from notificaciones.models import Notification
import json


def index(request):
    courses = Course.objects.filter(is_active=True).order_by('order')
    
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
            else:
                data = request.POST

            name  = data.get('name', '').strip()
            email = data.get('email', '').strip()
            level = data.get('level', '').strip()
            course_id = data.get('course_id')

            if name and email and course_id:
                student, created = Student.objects.update_or_create(
                    email=email,
                    defaults={'name': name, 'level': 'principiante', 'status': 'pending'}
                )
                
                course = get_object_or_404(Course, id=course_id)
                
                # Crear la solicitud de inscripción específica
                EnrollmentRequest.objects.get_or_create(
                    student=student,
                    course=course,
                    defaults={'status': 'pending'}
                )

                Notification.objects.create(
                    student=student, title='Solicitud de ingreso IA',
                    message=f'Tu solicitud para el curso "{course.title}" ha sido recibida.',
                    notif_type='info'
                )
                return JsonResponse({
                    'status': 'success',
                    'message': '¡Solicitud enviada! Analizando tu perfil para el ingreso a la academia.'
                })
            else:
                return JsonResponse({'status': 'error', 'message': 'Faltan datos.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return render(request, 'enrollment/index.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id, is_active=True)
    contents = course.contents.all()
    exams = course.exams.all()
    files = course.files.all()
    return render(request, 'enrollment/course_preview.html', {
        'course': course,
        'contents': contents,
        'exams': exams,
        'files': files
    })

def course_detail_api(request, course_id):
    course = get_object_or_404(Course, id=course_id, is_active=True)
    return JsonResponse({'title': course.title, 'description': course.description})
