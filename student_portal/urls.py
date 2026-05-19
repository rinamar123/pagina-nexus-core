from django.urls import path
from django.contrib.auth import views as auth_views
from ai_project.views import GmailAPIPasswordResetView
from . import views

urlpatterns = [
    path('login/',            views.student_login,           name='student_login'),
    path('logout/',           views.student_logout,          name='student_logout'),
    path('',                  views.student_dashboard,       name='student_dashboard'),
    path('estadisticas/',    views.student_stats,           name='student_stats'),
    path('perfil/editar/',   views.student_update_profile,  name='student_update_profile'),
    path('perfil/password/', views.student_change_password, name='student_change_password'),
    path('inscribir/',       views.student_enroll_course,   name='student_enroll_course'),
    path('notificacion/<int:pk>/leer/',      views.student_mark_read,      name='student_mark_read'),
    path('notificacion/<int:pk>/eliminar/',  views.student_delete_notif,   name='student_delete_notif'),
    path('notificaciones/leer-todas/',       views.student_mark_all_read,  name='student_mark_all_read'),
    path('notificaciones/eliminar-todas/',   views.student_delete_all_notifs, name='student_delete_all_notifs'),
    path('notificaciones/contar/',           views.student_notifications_count, name='student_notifications_count'),
    path('chat-general/',                    views.student_dashboard_chat, name='student_dashboard_chat'),
    path('curso/<int:pk>/',                  views.course_detail, name='student_course_detail'),
    path('curso/<int:pk>/chat/',             views.student_course_chat, name='student_course_chat'),
    path('curso/<int:pk>/examen/',           views.take_exam,     name='take_exam'),
    path('curso/<int:pk>/examen/<int:attempt_pk>/resultado/', views.exam_result, name='exam_result'),
    path('curso/reto/submit/',               views.submit_challenge, name='submit_challenge'),
    path('curso/<int:pk>/diploma/',          views.student_diploma, name='student_diploma'),
    path('curso/<int:pk>/solicitar-diploma/',views.student_request_diploma, name='student_request_diploma'),


    # Recuperación de contraseña
    path('recuperar-password/', GmailAPIPasswordResetView.as_view(
        template_name='student_portal/password_reset.html',
        email_template_name='student_portal/password_reset_email.html',
        success_url='/estudiantes/recuperar-password/enviado/'
    ), name='password_reset'),
    
    path('recuperar-password/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='student_portal/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('recuperar-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='student_portal/password_reset_confirm.html',
        success_url='/estudiantes/recuperar-password/completado/'
    ), name='password_reset_confirm'),
    
    path('recuperar-password/completado/', auth_views.PasswordResetCompleteView.as_view(
        template_name='student_portal/password_reset_complete.html'
    ), name='password_reset_complete'),
]
