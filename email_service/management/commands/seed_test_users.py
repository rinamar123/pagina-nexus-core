from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from enrollment.models import Student


class Command(BaseCommand):
    help = 'Crea usuarios de prueba'

    def handle(self, *args, **options):
        users_data = [
            # (username, password, email, is_staff, is_superuser)
            ('admin', 'admin123', 'admin@nexus.com', True, True),
            ('profesor', 'Profesor2026*', 'profesor@nexus.com', True, True),
        ]
        for username, password, email, staff, superuser in users_data:
            user, created = User.objects.update_or_create(
                username=username,
                defaults={'email': email, 'is_staff': staff, 'is_superuser': superuser}
            )
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Admin {username} / {password}'))

        students_data = [
            ('andres01032001', 'Iacademy2026*', 'andres01032001@gmail.com', 'Andres', 'accepted', ''),
            ('ana.garcia', 'Ana2026*', 'ana@ejemplo.com', 'Ana García', 'accepted', 'Ana2026*'),
            ('maria.rodriguez', 'Maria2026*', 'maria@ejemplo.com', 'María Rodríguez', 'accepted', ''),
            ('carlos.lopez', 'Carlos2026*', 'carlos@ejemplo.com', 'Carlos López', 'pending', 'Carlos2026*'),
        ]
        for username, password, email, name, status, gpwd in students_data:
            user, _ = User.objects.update_or_create(
                username=username, defaults={'email': email}
            )
            user.set_password(password)
            user.save()
            Student.objects.update_or_create(
                email=email,
                defaults={'name': name, 'status': status, 'user': user, 'generated_password': gpwd, 'level': 'principiante'}
            )
            self.stdout.write(self.style.SUCCESS(f'Estudiante {username} / {password}'))

        self.stdout.write(self.style.SUCCESS('\nUsuarios de prueba creados correctamente'))
