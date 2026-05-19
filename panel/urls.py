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
    
    # Diplomas y Notificaciones del Admin
    path('diploma/<int:pk>/aprobar/', views.admin_diploma_approve, name='admin_diploma_approve'),
    path('diploma/<int:pk>/rechazar/', views.admin_diploma_reject, name='admin_diploma_reject'),
    path('notificaciones/admin/json/', views.admin_notifications_json, name='admin_notifications_json'),
    path('notificaciones/admin/<int:pk>/leer/', views.admin_mark_read_notification, name='admin_mark_read_notification'),
    path('notificaciones/admin/<int:pk>/eliminar/', views.admin_delete_notification, name='admin_delete_notification'),
    path('notificaciones/admin/limpiar/', views.admin_clear_all_notifications, name='admin_clear_all_notifications'),

    # Solicitudes de nuevos Administradores
    path('solicitar-acceso/', views.admin_signup, name='admin_signup'),
    path('solicitudes-admin/verificar/<uuid:token>/', views.admin_request_verify, name='admin_request_verify'),
    path('solicitudes-admin/rechazar/<uuid:token>/', views.admin_request_reject, name='admin_request_reject'),
    path('descargar-datos/', views.download_database, name='admin_download_database'),
    path('estudiante/<int:student_id>/quitar-recientes/', views.exclude_recent_student, name='exclude_recent_student'),
]
