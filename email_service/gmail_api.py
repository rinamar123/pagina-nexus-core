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


def _load_credentials(scopes):
    """Intenta cargar credenciales desde archivo o variable de entorno."""
    token_path = settings.GMAIL_API_TOKEN_FILE
    token_env = os.environ.get('GMAIL_API_TOKEN_JSON')

    if os.path.exists(token_path):
        logger.info("Cargando token desde archivo %s", token_path)
        return Credentials.from_authorized_user_file(str(token_path), scopes)

    if token_env:
        logger.info("Cargando token desde variable de entorno GMAIL_API_TOKEN_JSON")
        try:
            info = json.loads(base64.b64decode(token_env).decode('utf-8'))
            return Credentials.from_authorized_user_info(info, scopes)
        except Exception as e:
            logger.error("Error decodificando GMAIL_API_TOKEN_JSON: %s", e)

    return None


def _save_credentials(creds):
    """Guarda credenciales en archivo para usos futuros."""
    token_path = settings.GMAIL_API_TOKEN_FILE
    with open(token_path, 'w') as token:
        token.write(creds.to_json())
    logger.info("Token guardado en %s", token_path)


def _load_client_config():
    """Intenta cargar client_config desde archivo o variable de entorno."""
    creds_path = settings.GMAIL_API_CREDENTIALS_FILE
    env_var = os.environ.get('GMAIL_API_CLIENT_SECRET_JSON')

    if os.path.exists(creds_path):
        logger.info("Cargando client_secret desde archivo %s", creds_path)
        with open(creds_path) as f:
            return json.load(f)

    if env_var:
        logger.info("Cargando client_secret desde variable de entorno GMAIL_API_CLIENT_SECRET_JSON")
        try:
            return json.loads(base64.b64decode(env_var).decode('utf-8'))
        except Exception as e:
            logger.error("Error decodificando GMAIL_API_CLIENT_SECRET_JSON: %s", e)

    return None


def get_gmail_service():
    """
    Autentica y devuelve el servicio de la API de Gmail.
    Soporta credenciales desde archivo o variables de entorno.
    Usa run_console() para entornos sin navegador (servidores headless).
    """
    scopes = settings.GMAIL_API_SCOPES
    creds = _load_credentials(scopes)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            logger.info("Refrescando token de Gmail API...")
            creds.refresh(Request())
        else:
            client_config = _load_client_config()
            if not client_config:
                raise RuntimeError(
                    "No se encontraron credenciales de Gmail API. "
                    "Define GMAIL_API_TOKEN_JSON y GMAIL_API_CLIENT_SECRET_JSON "
                    "como variables de entorno (base64), o coloca los archivos "
                    "token.json y client_secret_*.json en el directorio del proyecto."
                )
            logger.info("Iniciando flujo de autorización de Gmail API via consola...")
            flow = InstalledAppFlow.from_client_config(client_config, scopes)
            creds = flow.run_console()
        _save_credentials(creds)

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
        logger.info("Correo enviado exitosamente a %s", to)
        return True
    except Exception as e:
        logger.error("Error enviando via Gmail API a %s: %s", to, e)
        return False
