from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Carga los datos iniciales de cursos, lecciones y exámenes'

    def handle(self, *args, **options):
        self.stdout.write('Ejecutando populate_premium_full...')
        exec(open('populate_premium_full.py').read())
        self.stdout.write(self.style.SUCCESS('OK'))

        self.stdout.write('Ejecutando setup_exam_questions...')
        exec(open('setup_exam_questions.py').read())
        self.stdout.write(self.style.SUCCESS('OK'))

        self.stdout.write('Ejecutando final_content_setup...')
        exec(open('final_content_setup.py').read())
        self.stdout.write(self.style.SUCCESS('OK'))

        self.stdout.write('Ejecutando populate_challenges...')
        exec(open('populate_challenges.py').read())
        self.stdout.write(self.style.SUCCESS('OK'))

        self.stdout.write(self.style.SUCCESS('Todos los datos cargados exitosamente'))
