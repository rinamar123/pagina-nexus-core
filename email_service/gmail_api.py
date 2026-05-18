import os
import pickle
import base64
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from django.conf import settings

def get_gmail_service():
    """
    Autentica y devuelve el servicio de la API de Gmail.
    Genera token.json si no existe.
    """
    creds = None
    token_path = settings.GMAIL_API_TOKEN_FILE
    creds_path = settings.GMAIL_API_CREDENTIALS_FILE
    scopes = settings.GMAIL_API_SCOPES

    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, scopes)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def send_gmail_api_message(to, subject, body):
    """
    Envía un correo usando la Gmail API.
    """
    try:
        service = get_gmail_service()
        message = MIMEText(body)
        message['to'] = to
        message['subject'] = subject
        
        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
        
        service.users().messages().send(
            userId='me',
            body={'raw': raw_message}
        ).execute()
        return True
    except Exception as e:
        print(f"Error sending via Gmail API: {e}")
        return False
