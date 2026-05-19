from django.core.mail import send_mail
from django.conf import settings
from .gmail_api import send_gmail_api_message

def send_student_welcome_email(student, password):
    subject = '🔑 CREDENCIALES DE ACCESO - IA ACADEMY'
    body = f"""
    SISTEMA DE SINCRONIZACIÓN IA ACADEMY
    ------------------------------------
    
    Hola {student.name},
    
    Tu perfil ha sido analizado y aceptado en nuestra red neuronal. 
    A continuación, tus credenciales de acceso al Nexus Core:
    
    USUARIO: {student.user.username}
    PASSWORD: {password}
    
    Portal de Acceso: http://127.0.0.1:8000/estudiante/login/
    
    Por favor, sincroniza tu red lo antes posible.
    
    -- SISTEMA NUCLEUS IA --
    """
    
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(student.email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [student.email])

def send_enrollment_rejected_email(student, course=None):
    subject = '🔴 ACTUALIZACIÓN DE ESTADO - IA ACADEMY'
    body = f"Hola {student.name},\n\nTu solicitud de sincronización ha sido rechazada por el sistema. Inténtalo más tarde."
    
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(student.email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [student.email])

def send_password_changed_email(student, reset_url):
    subject = '✅ ACTUALIZACIÓN DE CREDENCIALES EXITOSA - IA ACADEMY'
    body = f"""
    SISTEMA DE SEGURIDAD IA ACADEMY
    -------------------------------
    
    Hola {student.name},
    
    Te confirmamos que la contraseña de tu cuenta ha sido actualizada con éxito en nuestros servidores.
    
    Si tú realizaste este cambio, no es necesario realizar ninguna acción adicional.
    
    Si NO solicitaste este cambio y crees que tu cuenta ha sido comprometida, por favor recupera tu cuenta inmediatamente utilizando el siguiente enlace:
    {reset_url}
    
    -- SISTEMA NUCLEUS IA --
    """
    
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(student.email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [student.email])

def send_student_deleted_email(student_name, student_email):
    subject = '❌ REGISTRO ELIMINADO - IA ACADEMY'
    body = f"""
    SISTEMA DE SEGURIDAD IA ACADEMY
    -------------------------------
    
    Hola {student_name},
    
    Te notificamos que tu registro y cuenta asociada en la red neuronal de IA Academy han sido eliminados de manera permanente por el administrador del sistema.
    
    Si crees que esto ha sido un error, por favor ponte en contacto con el administrador.
    
    -- SISTEMA NUCLEUS IA --
    """
    
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(student_email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [student_email])

def send_student_accepted_email(student):
    subject = '🟢 REGISTRO ACEPTADO / ACCESO AUTORIZADO - IA ACADEMY'
    body = f"""
    SISTEMA DE REGISTRO IA ACADEMY
    ------------------------------
    
    Hola {student.name},
    
    ¡Tu registro ha sido ACEPTADO exitosamente! 
    Tu cuenta está activa y autorizada para ingresar al Nexus Core.
    
    Portal de Acceso: http://127.0.0.1:8000/estudiante/login/
    
    -- SISTEMA NUCLEUS IA --
    """
    
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(student.email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [student.email])

def send_student_suspended_email(student):
    subject = '⚠️ CUENTA SUSPENDIDA HASTA NUEVO AVISO - IA ACADEMY'
    body = f"""
    SISTEMA DE CONTROL IA ACADEMY
    -----------------------------
    
    Hola {student.name},
    
    Te informamos que tu estado en el sistema ha sido cambiado a SUSPENDIDO HASTA NUEVO AVISO por el administrador.
    Tu acceso a los módulos de aprendizaje y evaluaciones en el Nexus Core está restringido temporalmente.
    
    Si tienes alguna duda sobre esta medida o deseas solicitar su revisión, ponte en contacto con soporte técnico o administración.
    
    -- SISTEMA NUCLEUS IA --
    """
    
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(student.email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [student.email])

def send_password_reset_email(subject, body, to_email):
    if settings.GMAIL_API_ENABLED:
        return send_gmail_api_message(to_email, subject, body)
    else:
        return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [to_email])

