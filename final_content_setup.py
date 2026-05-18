import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from enrollment.models import Course, CourseContent

def run():
    CourseContent.objects.all().delete()
    
    courses_data = [
        {
            'id': 4, # IA Academy
            'levels': [
                ('BASICO', [
                    ('Introducción a la IA', 'La IA simula la inteligencia humana. Aprenderemos sobre sistemas expertos y lógica difusa.', 'Visualización de un árbol de decisión simple.', 'Clasifica este dataset de flores usando lógica base.'),
                    ('Historia y Evolución', 'Desde Turing hasta GPT-4. Entenderemos el "invierno de la IA".', 'Línea de tiempo interactiva de hitos.', 'Investiga y sube un ensayo sobre el impacto de la IA.'),
                ]),
                ('INTERMEDIO', [
                    ('Perceptrón y Neuronas', 'La unidad básica de una red neuronal. Pesos, sesgos y sumatorias.', 'Simulador de compuertas lógicas (AND/OR).', 'Entrena una neurona para reconocer patrones binarios.'),
                    ('Redes Neuronales', 'Capas ocultas y funciones de activación como ReLU y Sigmoide.', 'Demo de una red neuronal en tiempo real.', 'Sube tu arquitectura de red neuronal en Python.'),
                ]),
                ('AVANZADO', [
                    ('Deep Learning', 'Redes profundas y convolución para imágenes.', 'Demo de detección de bordes en fotos.', 'Entrena una CNN para clasificar perros vs gatos.'),
                    ('Ética en la IA', 'Sesgos algorítmicos y responsabilidad en el desarrollo.', 'Casos de estudio de IA con sesgos de género/raza.', 'Sube tu propuesta de marco ético para una IA.'),
                ])
            ]
        },
        {
            'id': 5, # Regresión
            'levels': [
                ('BASICO', [
                    ('Conceptos Estadísticos', 'Media, varianza y covarianza aplicada a modelos.', 'Cálculo manual de la covarianza.', 'Calcula las métricas base para este CSV de salarios.'),
                    ('Regresión Simple', 'La recta y = mx + b. Minimizando el error cuadrático.', 'Gráfico interactivo de dispersión.', 'Predice la nota de un examen basado en horas de estudio.'),
                ]),
                ('INTERMEDIO', [
                    ('Regresión Múltiple', 'Predicción con múltiples variables independientes.', 'Modelo de predicción de precio de casas.', 'Sube tu modelo multivariado para este dataset de ventas.'),
                    ('Evaluación de Modelos', 'Entendiendo R2, MSE y RMSE.', 'Comparativa de dos modelos con métricas.', 'Calcula el error de tu predicción anterior.'),
                ]),
                ('AVANZADO', [
                    ('Regresión Logística', 'Clasificación binaria usando la función sigmoide.', 'Predicción de abandono de clientes (Churn).', 'Sube tu clasificador de correos Spam/No Spam.'),
                    ('Regularización L1/L2', 'Lasso y Ridge para evitar el overfitting.', 'Efecto de la penalización en los coeficientes.', 'Aplica Ridge a un modelo con 50 variables.'),
                ])
            ]
        },
        {
            'id': 6, # Genéticos
            'levels': [
                ('BASICO', [
                    ('Conceptos Biológicos', 'Genes, cromosomas y selección natural en software.', 'Simulador de herencia genética simple.', 'Define el genoma para un robot caminante.'),
                    ('Función Fitness', 'Cómo medir el éxito de un individuo en la población.', 'Ejemplo de evaluación de individuos.', 'Crea la función fitness para maximizar ganancias.'),
                ]),
                ('INTERMEDIO', [
                    ('Crossover y Selección', 'Combinando los mejores padres. Ruleta y torneo.', 'Visualización de cruce de ADN digital.', 'Implementa el operador de cruce de un punto.'),
                    ('Mutación Genética', 'Manteniendo la diversidad para evitar óptimos locales.', 'Efecto de la tasa de mutación en la población.', 'Simula la mutación de una cadena binaria.'),
                ]),
                ('AVANZADO', [
                    ('Optimización de Rutas', 'El problema del viajero (TSP) con algoritmos genéticos.', 'Simulación de rutas evolutivas.', 'Sube la ruta más corta para 20 ciudades.'),
                    ('Bio-IA Aplicada', 'Enjambres de partículas y colonias de hormigas.', 'Demo de hormigas buscando comida.', 'Resuelve un problema de logística usando PSO.'),
                ])
            ]
        }
    ]

    for c_data in courses_data:
        try:
            course = Course.objects.get(id=c_data['id'])
            order = 1
            for level_tag, lessons in c_data['levels']:
                for title, expl, example, task in lessons:
                    # 1. EXPLICACIÓN
                    CourseContent.objects.create(
                        course=course,
                        title=f'[{level_tag}] 📖 {title}: Teoría',
                        content=f'<div class="cyber-content"><h3>Fundamentos de {title}</h3><p>{expl}</p></div>',
                        order=order,
                        section_type='explicacion'
                    )
                    order += 1
                    # 2. EJEMPLO
                    CourseContent.objects.create(
                        course=course,
                        title=f'[{level_tag}] 💻 {title}: Ejemplo',
                        content=f'<div class="cyber-content"><h3>Demostración de {title}</h3><p>{example}</p><pre># Demo de ejecución\nprint("Simulando {title}...")\ndata = load_sample_data()</pre></div>',
                        order=order,
                        section_type='demo'
                    )
                    order += 1
                    # 3. TALLER
                    CourseContent.objects.create(
                        course=course,
                        title=f'[{level_tag}] 🧪 {title}: Taller',
                        content=f'<div class="cyber-content"><h3>Reto Práctico</h3><p>{task}</p><p>Sincroniza tus resultados (CSV o Notebook) para revisión.</p></div>',
                        order=order,
                        section_type='demo'
                    )
                    order += 1
            print(f"Curso {course.title} actualizado con 18 lecciones.")
        except Course.DoesNotExist:
            print(f"Error: No se encontró el curso con ID {c_data['id']}")

if __name__ == "__main__":
    run()
