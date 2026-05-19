from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from enrollment.models import Student, Course
from .models import LessonProgress, AssignmentSubmission

@login_required(login_url='student_login')
def student_stats(request):
    student = request.user.student
    courses = student.courses.all()
    
    course_stats = []
    total_avg = 0
    
    for course in courses:
        # Calcular progreso de lecciones
        total_lessons = course.contents.count()
        completed_lessons = LessonProgress.objects.filter(student=student, lesson__course=course, completed=True).count()
        progress_pct = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        
        # Calcular promedio de notas (escala 1-5)
        submissions = AssignmentSubmission.objects.filter(student=student, lesson__course=course, grade__isnull=False)
        avg_grade = 0
        if submissions.exists():
            # Convertimos la escala 100 a escala 5
            raw_avg = sum(s.grade for s in submissions) / submissions.count()
            avg_grade = round((raw_avg / 100) * 5, 1)
        
        status = "APROBADO" if avg_grade >= 3.0 else "EN PROCESO"
        if not submissions.exists(): status = "SIN NOTAS"

        course_stats.append({
            'course': course,
            'progress': progress_pct,
            'avg_grade': avg_grade,
            'status': status,
            'submissions_count': submissions.count()
        })
        total_avg += avg_grade

    overall_avg = round(total_avg / courses.count(), 1) if courses.exists() else 0

    return render(request, 'student_portal/estadisticas.html', {
        'student': student,
        'course_stats': course_stats,
        'overall_avg': overall_avg
    })
