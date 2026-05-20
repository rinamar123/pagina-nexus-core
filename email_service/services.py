import logging
from django.core.mail import send_mail
from django.conf import settings
from .gmail_api import send_gmail_api_message

logger = logging.getLogger(__name__)

SITE_URL = getattr(settings, 'SITE_URL', 'http://127.0.0.1:8000')
LOGIN_URL = f'{SITE_URL}/estudiante/login/'


def _html_wrapper(title, content_html):
    return f'''<!DOCTYPE html>
<html lang="es">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background-color:#f4f4f4;font-family:'Segoe UI',Helvetica,Arial,sans-serif">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color:#f4f4f4;padding:30px 10px">
    <tr><td align="center">
      <table role="presentation" width="600" cellpadding="0" cellspacing="0" style="background-color:#ffffff;border-radius:8px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08)">
        <tr>
          <td style="background:linear-gradient(135deg,#0d1b2a,#1b3a5c);padding:30px 40px;text-align:center">
            <h1 style="margin:0;color:#ffffff;font-size:22px;font-weight:700;letter-spacing:1px">NEXUS CORE</h1>
            <p style="margin:4px 0 0;color:#88c0ff;font-size:13px">IA & ML Academy</p>
          </td>
        </tr>
        <tr><td style="padding:35px 40px;color:#333333;font-size:15px;line-height:1.6">
          {content_html}
        </td></tr>
        <tr>
          <td style="background-color:#f8f9fa;padding:20px 40px;text-align:center;border-top:1px solid #e9ecef">
            <p style="margin:0;color:#6c757d;font-size:12px;line-height:1.5">
              <strong style="color:#333">Nexus Core — IA & ML Academy</strong><br>
              Este es un mensaje automático, por favor no respondas a este correo.<br>
              &copy; 2026 Nexus Core. Todos los derechos reservados.
            </p>
          </td>
        </tr>
      </table>
    </td></tr>
  </table>
</body>
</html>'''


def _build_content(title, lines, cta_text=None, cta_url=None):
    lines_html = '\n'.join(f'<p style="margin:0 0 12px">{l}</p>' for l in lines)
    cta = ''
    if cta_text and cta_url:
        cta = f'''
  <table role="presentation" cellpadding="0" cellspacing="0" style="margin:22px 0 8px">
    <tr>
      <td align="center" style="background:linear-gradient(135deg,#0d1b2a,#1b3a5c);border-radius:6px;padding:12px 32px">
        <a href="{cta_url}" style="color:#ffffff;text-decoration:none;font-size:15px;font-weight:600;display:inline-block">{cta_text}</a>
      </td>
    </tr>
  </table>'''
    footer = '<hr style="border:none;border-top:1px solid #e9ecef;margin:20px 0 8px"><p style="margin:0;color:#6c757d;font-size:12px">— Equipo Nexus Core</p>' if not cta_text else ''
    return _html_wrapper(title, f'''
    <h2 style="color:#0d1b2a;font-size:19px;margin:0 0 18px">{title}</h2>
    {lines_html}
    {cta}
    {footer}
''')


def _send_email(subject, body, to_email, html_body=None):
    if settings.GMAIL_API_ENABLED:
        sent = send_gmail_api_message(to_email, subject, body, html=html_body)
        if sent:
            return True
        logger.warning(f"Gmail API falló para {to_email}, usando SMTP como respaldo")
    send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [to_email], html_message=html_body)
    return True


def send_student_welcome_email(student, password):
    subject = 'Credenciales de Acceso — Nexus Core IA Academy'
    plain = f"""Hola {student.name},

Tu registro ha sido aprobado. Tus credenciales de acceso al sistema son:

USUARIO: {student.user.username}
CONTRASEÑA: {password}

Ingresa aquí: {LOGIN_URL}

— Equipo Nexus Core"""
    html = _build_content(
        'Credenciales de Acceso',
        [f'Hola <strong>{student.name}</strong>,',
         'Tu registro ha sido aprobado. Estas son tus credenciales para ingresar al sistema:',
         f'<table cellpadding="6" cellspacing="0" style="background:#f1f3f5;border-radius:6px;margin:8px 0 16px;width:100%">'
         f'<tr><td style="color:#555;font-size:13px;font-weight:600;width:110px">USUARIO</td>'
         f'<td style="font-size:14px;color:#0d1b2a;font-family:monospace">{student.user.username}</td></tr>'
         f'<tr><td style="color:#555;font-size:13px;font-weight:600;width:110px">CONTRASEÑA</td>'
         f'<td style="font-size:14px;color:#0d1b2a;font-family:monospace">{password}</td></tr>'
         f'</table>',
         'Por seguridad, cambia tu contraseña después del primer ingreso.'],
        cta_text='INGRESAR AL SISTEMA',
        cta_url=LOGIN_URL
    )
    return _send_email(subject, plain, student.email, html_body=html)


def send_enrollment_rejected_email(student, course=None):
    subject = 'Actualización de Estado — Nexus Core IA Academy'
    course_text = f' al curso <strong>{course.title}</strong>' if course else ''
    plain = f"""Hola {student.name},

Tu solicitud de inscripción{course_text} ha sido revisada y no pudo ser aprobada en esta ocasión.

Si tienes dudas, contacta al administrador del sistema.

— Equipo Nexus Core"""
    html = _build_content(
        'Solicitud Revisada',
        [f'Hola <strong>{student.name}</strong>,',
         f'Tu solicitud de inscripción{course_text} ha sido revisada y no pudo ser aprobada en esta ocasión.',
         'Si consideras que esto es un error, por favor ponte en contacto con el administrador del sistema.']
    )
    return _send_email(subject, plain, student.email, html_body=html)


def send_password_changed_email(student, reset_url):
    subject = 'Contraseña Actualizada — Nexus Core IA Academy'
    plain = f"""Hola {student.name},

Te confirmamos que tu contraseña ha sido actualizada exitosamente.

Si no realizaste este cambio, recupera tu cuenta aquí: {reset_url}

— Equipo Nexus Core"""
    html = _build_content(
        'Contraseña Actualizada',
        [f'Hola <strong>{student.name}</strong>,',
         'Te confirmamos que tu contraseña ha sido <strong>actualizada exitosamente</strong>.',
         'Si tú realizaste este cambio, no necesitas hacer nada más.',
         'Si <strong>no</strong> solicitaste este cambio, protege tu cuenta de inmediato.'],
        cta_text='RECUPERAR CUENTA',
        cta_url=reset_url
    )
    return _send_email(subject, plain, student.email, html_body=html)


def send_student_deleted_email(student_name, student_email):
    subject = 'Registro Eliminado — Nexus Core IA Academy'
    plain = f"""Hola {student_name},

Te notificamos que tu cuenta en Nexus Core ha sido eliminada de forma permanente por el administrador.

Si crees que esto ha sido un error, contacta al administrador.

— Equipo Nexus Core"""
    html = _build_content(
        'Registro Eliminado',
        [f'Hola <strong>{student_name}</strong>,',
         'Te notificamos que tu registro y cuenta asociada han sido <strong>eliminados de forma permanente</strong> por el administrador del sistema.',
         'Si crees que esto ha sido un error, por favor contacta al administrador para resolver la situación.']
    )
    return _send_email(subject, plain, student_email, html_body=html)


def send_student_accepted_email(student):
    subject = 'Acceso Autorizado — Nexus Core IA Academy'
    plain = f"""Hola {student.name},

¡Tu registro ha sido ACEPTADO! Tu cuenta está activa y autorizada.

Ingresa aquí: {LOGIN_URL}

— Equipo Nexus Core"""
    html = _build_content(
        'Acceso Autorizado',
        [f'Hola <strong>{student.name}</strong>,',
         '¡Tu registro ha sido <strong>aceptado exitosamente</strong>!',
         'Tu cuenta está activa y autorizada para ingresar al sistema Nexus Core.'],
        cta_text='INGRESAR AL SISTEMA',
        cta_url=LOGIN_URL
    )
    return _send_email(subject, plain, student.email, html_body=html)


def send_student_suspended_email(student):
    subject = 'Cuenta Suspendida — Nexus Core IA Academy'
    plain = f"""Hola {student.name},

Tu cuenta ha sido suspendida temporalmente por el administrador. Tu acceso está restringido hasta nuevo aviso.

Si tienes dudas, contacta al administrador.

— Equipo Nexus Core"""
    html = _build_content(
        'Cuenta Suspendida',
        [f'Hola <strong>{student.name}</strong>,',
         'Tu cuenta ha sido <strong>suspendida temporalmente</strong> por el administrador del sistema.',
         'Tu acceso a los módulos de aprendizaje y evaluaciones está restringido hasta nuevo aviso.',
         'Si tienes dudas sobre esta medida, contacta al administrador.']
    )
    return _send_email(subject, plain, student.email, html_body=html)


def send_password_reset_email(subject, body, to_email):
    return _send_email(subject, body, to_email)
