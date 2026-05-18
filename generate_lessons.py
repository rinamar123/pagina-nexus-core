from enrollment.models import Course, CourseContent

def run():
    CourseContent.objects.all().delete()
    
    courses_info = [
        {
            'title': 'Academy',
            'data': {
                'BASICO': ['Intro IA', 'Historia IA', 'Tipos Aprendizaje', 'Perceptrón', 'Dataset IRIS', 'Limpieza Datos'],
                'INTERMEDIO': ['Redes Neuronales', 'Backpropagation', 'Funciones Activación', 'Optimizadores', 'Overfitting', 'Validación'],
                'AVANZADO': ['Deep Learning', 'CNN Vision', 'NLP Texto', 'Transformers', 'GANs Generativas', 'IA Ética']
            }
        },
        {
            'title': 'Regresi',
            'data': {
                'BASICO': ['Estadística Base', 'Variables X/Y', 'Recta Regresión', 'Mínimos Cuadrados', 'Error Cuadrático', 'Correlación'],
                'INTERMEDIO': ['Regresión Múltiple', 'Multicolinealidad', 'Variables Dummy', 'R-Cuadrado', 'Residuos', 'P-Value'],
                'AVANZADO': ['Regresión Logística', 'Regularización L1/L2', 'Elastic Net', 'Series Temporales', 'Predicción Ventas', 'Modelos No Lineales']
            }
        },
        {
            'title': 'Gen',
            'data': {
                'BASICO': ['Teoría Evolución', 'Estructura Cromosoma', 'Población Inicial', 'Función Fitness', 'Ruleta Selección', 'Cruce Un Punto'],
                'INTERMEDIO': ['Mutación Inteligente', 'Elitismo', 'Torneo Selección', 'Cruce Multipunto', 'Convergencia', 'Parámetros Genéticos'],
                'AVANZADO': ['Algoritmos Meméticos', 'Optimización Multiobjetivo', 'Enjambres PSO', 'Colonias Hormigas', 'Problema Viajante', 'Bio-IA Aplicada']
            }
        }
    ]

    for info in courses_info:
        c = Course.objects.get(title__icontains=info['title'])
        order = 1
        for level, lessons in info['data'].items():
            for lesson in lessons:
                CourseContent.objects.create(
                    course=c,
                    title=f'[{level}] {lesson}',
                    content=f'Bienvenido al módulo de {lesson}. En esta sección profundizaremos en los aspectos técnicos y aplicaciones prácticas de este concepto dentro del área de {c.title}.',
                    order=order,
                    section_type='explicacion' if order % 3 != 0 else 'demo'
                )
                order += 1
    print('54 lecciones generadas exitosamente.')

if __name__ == "__main__":
    run()
