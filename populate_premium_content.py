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
            'lessons': [
                ('Historia de la IA', '<h3>Protocolo de Inicio: Historia de la IA</h3><p>Desde los autómatas griegos hasta la Máquina de Turing. La IA ha pasado por inviernos y primaveras. En esta lección exploraremos cómo pasamos de simples cálculos a redes neuronales masivas.</p><img src=\"https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800\" style=\"width:100%; border-radius:1rem; margin:1rem 0;\">', 'explicacion'),
                ('El Test de Turing', '<h3>Módulo Cognitivo: Test de Turing</h3><p>¿Puede una máquina pensar? Alan Turing propuso un juego de imitación para evaluar la inteligencia artificial. Analizaremos las implicaciones filosóficas y técnicas de este test hoy en día.</p>', 'explicacion'),
                ('Taller: Clasificación Base', '<h3>Laboratorio: Clasificación de Datos</h3><p>Usa este conjunto de datos para entender cómo una IA separa información. Descarga el CSV de prueba y sube tu análisis.</p>', 'demo'),
                ('Redes Neuronales', '<h3>Arquitectura Neural</h3><p>Las redes neuronales se inspiran en el cerebro humano. Capas de entrada, ocultas y salida. Veremos cómo viaja la información a través de los pesos y sesgos.</p><pre>input -> [W] -> sum -> f(x) -> output</pre>', 'explicacion'),
                ('Backpropagation', '<h3>Optimización: Propagación hacia atrás</h3><p>El corazón del entrenamiento. Cómo el error se propaga para ajustar los pesos y mejorar la precisión del modelo en cada iteración.</p>', 'explicacion'),
                ('Taller: Tu Primera Neurona', '<h3>Simulación de Perceptrón</h3><p>Implementa una neurona simple que aprenda la compuerta lógica AND. Sube tu notebook con la solución.</p>', 'demo'),
            ]
        },
        {
            'id': 5, # Regresión
            'lessons': [
                ('Estadística Predictiva', '<h3>Base de Datos: Estadística</h3><p>Para predecir el futuro necesitamos entender el pasado. Media, varianza y desviación estándar son las herramientas base de cualquier modelo de regresión lineal.</p>', 'explicacion'),
                ('Regresión Simple', '<h3>Modelo Lineal: Y = mX + b</h3><p>La relación entre una variable independiente y una dependiente. Aprenderemos a trazar la mejor línea posible a través de una nube de puntos.</p><img src=\"https://images.unsplash.com/photo-1551288049-bbda38a5f452?auto=format&fit=crop&q=80&w=800\" style=\"width:100%; border-radius:1rem; margin:1rem 0;\">', 'explicacion'),
                ('Taller: Predicción Salarial', '<h3>Laboratorio: Análisis de Sueldos</h3><p>Basado en los años de experiencia, predice el salario de un desarrollador. Descarga el CSV de entrenamiento abajo.</p>', 'demo'),
                ('Métricas de Error', '<h3>Evaluación: MSE y R2</h3><p>¿Qué tan buena es tu predicción? El Error Cuadrático Medio nos dice qué tan lejos estamos de la realidad. Buscamos el R2 más cercano a 1.</p>', 'explicacion'),
                ('Regresión Múltiple', '<h3>Predicción Multidimensional</h3><p>Cuando el precio de una casa depende no solo de los metros cuadrados, sino también del barrio y el número de baños.</p>', 'explicacion'),
                ('Taller: Mercado Inmobiliario', '<h3>Proyecto: Precios de Casas</h3><p>Sube tu modelo que use 3 variables independientes para predecir el valor de mercado. Usa el dataset inmobiliario adjunto.</p>', 'demo'),
            ]
        },
        {
            'id': 6, # Genéticos
            'lessons': [
                ('Darwinismo Digital', '<h3>Evolución Artificial</h3><p>Inspirado en la selección natural. Los algoritmos genéticos evolucionan soluciones a problemas complejos donde los métodos tradicionales fallan.</p>', 'explicacion'),
                ('Cromosomas y Genes', '<h3>Estructura de Datos: El Genoma</h3><p>Cómo codificar una solución en una cadena de bits o números. Definiremos qué genes representarán las características de nuestra solución.</p>', 'explicacion'),
                ('Taller: Población Inicial', '<h3>Laboratorio: Generación Aleatoria</h3><p>Crea una población de 100 individuos aleatorios y mide su fitness inicial. Sube tu script de generación.</p>', 'demo'),
                ('Cruce y Mutación', '<h3>Operadores Evolutivos</h3><p>El cruce mezcla lo mejor de dos padres. La mutación añade aleatoriedad para explorar nuevas posibilidades y no quedarse estancado.</p>', 'explicacion'),
                ('Elitismo', '<h3>Preservación de la Excelencia</h3><p>Aseguramos que los mejores individuos de la generación actual sobrevivan intactos a la siguiente, garantizando que nunca perdamos el progreso.</p>', 'explicacion'),
                ('Taller: El Problema del Viajero', '<h3>Desafío: Optimización de Rutas</h3><p>Encuentra el camino más corto entre 10 ciudades. Sube tu CSV con la secuencia óptima de coordenadas.</p>', 'demo'),
            ]
        }
    ]

    for c_data in courses_data:
        try:
            course = Course.objects.get(id=c_data['id'])
            for i, (title, content, s_type) in enumerate(c_data['lessons'], 1):
                CourseContent.objects.create(
                    course=course,
                    title=title,
                    content=content,
                    order=i,
                    section_type=s_type
                )
            print(f"Contenido premium cargado para {course.title}")
        except:
            pass

if __name__ == "__main__":
    run()
