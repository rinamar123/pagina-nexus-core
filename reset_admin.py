import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.is_staff = True
    user.is_superuser = True
    user.save()
    print("Contraseña del usuario 'admin' restablecida a: admin123")
except User.DoesNotExist:
    user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("Usuario 'admin' creado con contraseña: admin123")
