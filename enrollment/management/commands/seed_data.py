from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Carga los datos desde datos.json'

    def handle(self, *args, **options):
        self.stdout.write('Cargando datos desde datos.json...')
        call_command('loaddata', 'datos.json')
        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))
