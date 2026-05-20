import os
import json
import base64
import logging
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.conf import settings

logger = logging.getLogger(__name__)

def get_gmail_service():
    """
    Autentica y devuelve el servicio de la API de Gmail.
    Usa run_console() para entornos sin navegador (servidores headless).
    """
    creds = None
    token_path = settings.GMAIL_API_TOKEN_FILE
    creds_path = settings.GMAIL_API_CREDENTIALS_FILE
    scopes = settings.GMAIL_API_SCOPES

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(str(token_path), scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logger.info("Refrescando token de Gmail API...")
            creds.refresh(Request())
        else:
            logger.info("Iniciando flujo de autorización de Gmail API via consola...")
            flow = InstalledAppFlow.from_client_secrets_file(str(creds_path), scopes)
            creds = flow.run_console()
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
            logger.info(f"Token guardado en {token_path}")

    return build('gmail', 'v1', credentials=creds)

def send_gmail_api_message(to, subject, body):
    """
    Envía un correo usando la Gmail API.
    Retorna True si se envió correctamente, False en caso contrario.
    """
    try:
        service = get_gmail_service()
        message = MIMEText(body, _charset='utf-8')
        message['to'] = to
        message['subject'] = subject

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

        service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        logger.info(f"Correo enviado exitosamente a {to}")
        return True
    except Exception as e:
        logger.error(f"Error enviando via Gmail API a {to}: {e}")
        return False
