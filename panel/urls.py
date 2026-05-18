from django.urls import path
from . import views

urlpatterns = [
    path('login/',   views.admin_login,  name='admin_login'),
    path('logout/',  views.admin_logout, name='admin_logout'),
    path('',         views.dashboard,    name='admin_dashboard'),
    path('estudiante/<int:pk>/editar/',   views.student_edit,   name='student_edit'),
    path('estudiante/<int:pk>/eliminar/', views.student_delete, name='student_delete'),
    path('cursos/',                         views.course_list,     name='course_list'),
    path('notificaciones/', views.notifications_view, name='notifications_view'),
    path('inscripcion/<int:pk>/aceptar/', views.enrollment_accept, name='enrollment_accept'),
    path('inscripcion/<int:pk>/rechazar/', views.enrollment_reject, name='enrollment_reject'),
    path('talleres/', views.grade_assignments, name='admin_grade_assignments'),
    path('talleres/<int:submission_id>/calificar/', views.submit_grade, name='admin_submit_grade'),
]
