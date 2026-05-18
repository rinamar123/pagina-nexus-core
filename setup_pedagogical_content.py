import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from enrollment.models import Course, CourseContent

def run():
    CourseContent.objects.all().delete()
    
    courses_data = [
        {
            'course_key': 'Academy',
            'topics': [
                ('Fundamentos de IA', 'Aprende qué es la IA y su historia.', 'Implementación de un Perceptrón simple.', 'Entrena tu propia neurona con este CSV.'),
                ('Redes Neuronales', 'Arquitectura de capas y neuronas.', 'Demo de clasificación de imágenes.', 'Sube tu modelo de clasificación de dígitos.'),
                ('Deep Learning', 'Redes profundas y visión artificial.', 'Demo de detección de objetos en tiempo real.', 'Sube tu proyecto de detección facial.')
            ]
        },
        {
            'course_key': 'Regresi',
            'topics': [
                ('Regresión Lineal Simple', 'Teoría de y = mx + b.', 'Predicción de precios de autos.', 'Predice el costo de vivienda usando este CSV.'),
                ('Regresión Múltiple', 'Análisis de múltiples variables.', 'Predicción de demanda de productos.', 'Sube tu análisis de regresión multivariada.'),
                ('Regularización (Lasso/Ridge)', 'Evitando el sobreajuste.', 'Optimización de modelos predictivos.', 'Limpia y regula este dataset complejo.')
            ]
        },
        {
            'course_key': 'Gen',
            'topics': [
                ('Selección y Fitness', 'Cómo elegir a los mejores individuos.', 'Simulación de evolución de especies.', 'Diseña la función fitness para este problema.'),
                ('Cruce y Mutación', 'Operadores genéticos avanzados.', 'Optimización de rutas de transporte.', 'Sube tu algoritmo de cruce para el TSP.'),
                ('Optimización Bio-IA', 'Enjambres y colonias de hormigas.', 'Demo de inteligencia colectiva.', 'Resuelve este problema de optimización masiva.')
            ]
        }
    ]

    for c_data in courses_data:
        course = Course.objects.get(title__icontains=c_data['course_key'])
        order = 1
        for topic, expl, example, task in c_data['topics']:
            # 1. EXPLICACIÓN
            CourseContent.objects.create(
                course=course,
                title=f'📖 Teoría: {topic}',
                content=f'<div class="cyber-content"><h3>Conceptos de {topic}</h3><p>{expl}</p></div>',
                order=order,
                section_type='explicacion'
            )
            order += 1
            # 2. EJEMPLO / DEMO
            CourseContent.objects.create(
                course=course,
                title=f'💻 Ejemplo: {topic}',
                content=f'<div class="cyber-content"><h3>Demostración Práctica</h3><p>{example}</p><pre># Código de ejemplo\nimport ai_core\nmodel = ai_core.build("{topic}")</pre></div>',
                order=order,
                section_type='demo'
            )
            order += 1
            # 3. TALLER / SUBIDA
            CourseContent.objects.create(
                course=course,
                title=f'🧪 Taller: {topic}',
                content=f'<div class="cyber-content"><h3>Reto de Aplicación</h3><p>{task}</p><p><b>Instrucciones:</b> Descarga el dataset, aplica lo aprendido y sube tu archivo final.</p></div>',
                order=order,
                section_type='demo'
            )
            order += 1

    print("54 Lecciones (Ciclo Completo: Teoría -> Ejemplo -> Taller) generadas.")

if __name__ == "__main__":
    run()
