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
                    ('Introducción a la IA', '<h3>Protocolo de Inicio: Historia de la IA</h3><p>Desde los autómatas griegos hasta la Máquina de Turing. La IA ha pasado por inviernos y primaveras. En esta lección exploraremos cómo pasamos de simples cálculos a redes neuronales masivas.</p><img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=800" style="width:100%; border-radius:1rem; margin:1rem 0;">', 'explicacion'),
                    ('El Test de Turing', '<h3>Módulo Cognitivo: Test de Turing</h3><p>¿Puede una máquina pensar? Alan Turing propuso un juego de imitación para evaluar la inteligencia artificial. Analizaremos las implicaciones filosóficas y técnicas de este test hoy en día.</p>', 'explicacion'),
                    ('Clasificación Base', '<h3>Laboratorio: Clasificación de Datos</h3><p>Usa este conjunto de datos para entender cómo una IA separa información. Descarga el CSV de prueba y sube tu análisis.</p>', 'demo'),
                    ('Sistemas Expertos', '<h3>Reglas Lógicas</h3><p>Los primeros sistemas de IA basados en reglas "If-Then". Aprenderemos cómo estructurar conocimiento humano en código.</p>', 'explicacion'),
                    ('Lógica Difusa', '<h3>Más allá de 0 y 1</h3><p>Cómo las máquinas manejan la incertidumbre y conceptos como "mucho", "poco" o "casi".</p>', 'explicacion'),
                    ('Taller Lógico', '<h3>Laboratorio: Sistema Difuso</h3><p>Crea un sistema de frenado automático usando lógica difusa y sube tu notebook.</p>', 'demo'),
                ]),
                ('INTERMEDIO', [
                    ('Perceptrón Simple', '<h3>La Unidad Básica</h3><p>El perceptrón es la neurona artificial más simple. Aprenderemos cómo los pesos y el sesgo determinan si la neurona se activa.</p>', 'explicacion'),
                    ('Compuertas Lógicas', '<h3>Aprendiendo AND/OR</h3><p>Demostración de cómo un perceptrón puede aprender operaciones booleanas básicas iterando sobre sus pesos.</p>', 'explicacion'),
                    ('Tu Primera Neurona', '<h3>Simulación de Perceptrón</h3><p>Implementa una neurona simple que aprenda la compuerta lógica AND. Sube tu notebook con la solución.</p>', 'demo'),
                    ('Redes Multicapa', '<h3>Capas Ocultas</h3><p>Las limitaciones del perceptrón simple se superan apilando neuronas. Veremos la arquitectura de las redes neuronales profundas.</p>', 'explicacion'),
                    ('Funciones Activación', '<h3>ReLU y Sigmoide</h3><p>Cómo introducir no-linealidad en la red para que pueda aprender patrones complejos.</p>', 'explicacion'),
                    ('Taller Multicapa', '<h3>Clasificador Iris</h3><p>Entrena una red neuronal con 1 capa oculta para clasificar flores Iris. Sube tus resultados.</p>', 'demo'),
                ]),
                ('AVANZADO', [
                    ('Backpropagation', '<h3>Optimización: Propagación hacia atrás</h3><p>El corazón del entrenamiento. Cómo el error se propaga para ajustar los pesos y mejorar la precisión del modelo en cada iteración.</p>', 'explicacion'),
                    ('Gradient Descent', '<h3>Descenso del Gradiente</h3><p>El algoritmo de optimización que encuentra el mínimo error posible ajustando los parámetros.</p>', 'explicacion'),
                    ('Taller Optimización', '<h3>Optimiza tu Red</h3><p>Aplica Descenso del Gradiente a tu red anterior y compara la mejora. Sube el notebook modificado.</p>', 'demo'),
                    ('Deep Learning', '<h3>Redes Convolucionales (CNN)</h3><p>El estándar para visión artificial. Cómo las redes extraen características de las imágenes usando filtros.</p>', 'explicacion'),
                    ('Procesamiento Texto', '<h3>NLP y Transformers</h3><p>Una introducción a cómo las máquinas entienden el lenguaje humano, desde Word2Vec hasta la atención.</p>', 'explicacion'),
                    ('Proyecto Final IA', '<h3>Clasificación de Imágenes</h3><p>Entrena una CNN básica para clasificar dígitos escritos a mano (MNIST) y sube tu código.</p>', 'demo'),
                ])
            ]
        },
        {
            'id': 5, # Regresión
            'levels': [
                ('BASICO', [
                    ('Estadística Predictiva', '<h3>Base de Datos: Estadística</h3><p>Para predecir el futuro necesitamos entender el pasado. Media, varianza y desviación estándar son las herramientas base de cualquier modelo de regresión lineal.</p>', 'explicacion'),
                    ('Covarianza', '<h3>Relación de Variables</h3><p>Entenderemos cómo dos variables se mueven juntas y qué significa esto para la predicción.</p>', 'explicacion'),
                    ('Taller Estadístico', '<h3>Cálculo de Métricas</h3><p>Descarga el dataset de estudiantes y calcula la varianza y covarianza de sus notas. Sube el resultado.</p>', 'demo'),
                    ('Regresión Simple', '<h3>Modelo Lineal: Y = mX + b</h3><p>La relación entre una variable independiente y una dependiente. Aprenderemos a trazar la mejor línea posible a través de una nube de puntos.</p><img src="https://images.unsplash.com/photo-1551288049-bbda38a5f452?auto=format&fit=crop&q=80&w=800" style="width:100%; border-radius:1rem; margin:1rem 0;">', 'explicacion'),
                    ('Minimos Cuadrados', '<h3>Ajustando la Línea</h3><p>El método matemático para encontrar la pendiente (m) y el intercepto (b) óptimos.</p>', 'explicacion'),
                    ('Predicción Salarial', '<h3>Laboratorio: Análisis de Sueldos</h3><p>Basado en los años de experiencia, predice el salario de un desarrollador. Descarga el CSV de entrenamiento abajo.</p>', 'demo'),
                ]),
                ('INTERMEDIO', [
                    ('Métricas de Error', '<h3>Evaluación: MSE y R2</h3><p>¿Qué tan buena es tu predicción? El Error Cuadrático Medio nos dice qué tan lejos estamos de la realidad. Buscamos el R2 más cercano a 1.</p>', 'explicacion'),
                    ('Análisis Residual', '<h3>Validando el Modelo</h3><p>Cómo analizar los errores (residuos) para saber si nuestro modelo lineal es apropiado para los datos.</p>', 'explicacion'),
                    ('Taller Evaluación', '<h3>Evalúa tu Modelo</h3><p>Calcula el MSE y el R2 de tu predicción salarial anterior. Sube el notebook con las métricas.</p>', 'demo'),
                    ('Regresión Múltiple', '<h3>Predicción Multidimensional</h3><p>Cuando el precio de una casa depende no solo de los metros cuadrados, sino también del barrio y el número de baños.</p>', 'explicacion'),
                    ('Variables Dummy', '<h3>Manejando Texto</h3><p>Cómo convertir variables categóricas (como ciudad o color) en números que el modelo pueda entender.</p>', 'explicacion'),
                    ('Mercado Inmobiliario', '<h3>Proyecto: Precios de Casas</h3><p>Sube tu modelo que use 3 variables independientes para predecir el valor de mercado. Usa el dataset inmobiliario adjunto.</p>', 'demo'),
                ]),
                ('AVANZADO', [
                    ('Regresión Logística', '<h3>Clasificación Binaria</h3><p>Cuando no predecimos un número, sino una categoría (Sí/No). La función sigmoide en acción.</p>', 'explicacion'),
                    ('Matriz Confusión', '<h3>Evaluando Clasificadores</h3><p>Precisión, Recall y F1-Score. Entendiendo falsos positivos y falsos negativos.</p>', 'explicacion'),
                    ('Taller Logístico', '<h3>Clasificador Spam</h3><p>Usa regresión logística para predecir si un correo es Spam o no. Sube tu modelo evaluado.</p>', 'demo'),
                    ('Multicolinealidad', '<h3>Cuando las variables compiten</h3><p>Qué pasa cuando dos variables independientes están muy correlacionadas y cómo solucionarlo.</p>', 'explicacion'),
                    ('Regularización', '<h3>Lasso y Ridge</h3><p>Técnicas avanzadas para penalizar modelos complejos y evitar el sobreajuste (overfitting).</p>', 'explicacion'),
                    ('Proyecto Avanzado', '<h3>Regularización L1/L2</h3><p>Aplica regularización a un dataset complejo con 50 variables. Sube tu modelo optimizado.</p>', 'demo'),
                ])
            ]
        },
        {
            'id': 6, # Genéticos
            'levels': [
                ('BASICO', [
                    ('Darwinismo Digital', '<h3>Evolución Artificial</h3><p>Inspirado en la selección natural. Los algoritmos genéticos evolucionan soluciones a problemas complejos donde los métodos tradicionales fallan.</p>', 'explicacion'),
                    ('Cromosomas y Genes', '<h3>Estructura de Datos: El Genoma</h3><p>Cómo codificar una solución en una cadena de bits o números. Definiremos qué genes representarán las características de nuestra solución.</p>', 'explicacion'),
                    ('Población Inicial', '<h3>Laboratorio: Generación Aleatoria</h3><p>Crea una población de 100 individuos aleatorios y mide su fitness inicial. Sube tu script de generación.</p>', 'demo'),
                    ('Función Fitness', '<h3>La Medida del Éxito</h3><p>La función matemática que decide qué tan "bueno" es un individuo resolviendo el problema.</p>', 'explicacion'),
                    ('Paisaje Fitness', '<h3>Óptimos Locales y Globales</h3><p>Entendiendo el espacio de búsqueda y por qué los algoritmos pueden quedarse estancados.</p>', 'explicacion'),
                    ('Taller Fitness', '<h3>Diseña tu Fitness</h3><p>Crea una función fitness para maximizar el valor de items en una mochila (Knapsack problem). Sube el código.</p>', 'demo'),
                ]),
                ('INTERMEDIO', [
                    ('Operador de Selección', '<h3>Supervivencia del más apto</h3><p>Métodos de selección: Ruleta, Torneo y Ranking. ¿Quién se reproduce?</p>', 'explicacion'),
                    ('Cruce (Crossover)', '<h3>Operadores Evolutivos</h3><p>El cruce mezcla lo mejor de dos padres. Veremos cruce de un punto, dos puntos y uniforme.</p>', 'explicacion'),
                    ('Taller Cruce', '<h3>Simula una Reproducción</h3><p>Implementa el cruce de un punto entre dos individuos binarios. Sube el resultado.</p>', 'demo'),
                    ('Mutación', '<h3>Mantenimiento de Diversidad</h3><p>La mutación añade aleatoriedad para explorar nuevas posibilidades y no quedarse estancado.</p>', 'explicacion'),
                    ('Elitismo', '<h3>Preservación de la Excelencia</h3><p>Aseguramos que los mejores individuos de la generación actual sobrevivan intactos a la siguiente, garantizando que nunca perdamos el progreso.</p>', 'explicacion'),
                    ('Taller Ciclo Completo', '<h3>Algoritmo Genético Base</h3><p>Une selección, cruce y mutación para resolver el problema de la mochila. Sube el notebook.</p>', 'demo'),
                ]),
                ('AVANZADO', [
                    ('Problema del Viajero', '<h3>TSP (Traveling Salesperson Problem)</h3><p>Un problema clásico de optimización de rutas. Cómo adaptar el cruce y la mutación para permutaciones.</p>', 'explicacion'),
                    ('Cruce de Orden (OX)', '<h3>Crossover para Rutas</h3><p>Operadores especiales cuando no podemos tener genes repetidos en un cromosoma.</p>', 'explicacion'),
                    ('Taller Rutas', '<h3>Desafío: Optimización de Rutas</h3><p>Encuentra el camino más corto entre 10 ciudades. Sube tu CSV con la secuencia óptima de coordenadas.</p>', 'demo'),
                    ('Inteligencia de Enjambre', '<h3>Más allá de los genes</h3><p>Introducción a algoritmos inspirados en el comportamiento colectivo: PSO y ACO.</p>', 'explicacion'),
                    ('PSO en Acción', '<h3>Optimización por Enjambre de Partículas</h3><p>Cómo las "partículas" comparten información para encontrar el óptimo en un espacio multidimensional.</p>', 'explicacion'),
                    ('Proyecto Bio-IA', '<h3>Implementa PSO</h3><p>Usa la librería PySwarms para encontrar el mínimo de la función de Rastrigin. Sube tu solución.</p>', 'demo'),
                ])
            ]
        }
    ]

    for c_data in courses_data:
        try:
            course = Course.objects.get(id=c_data['id'])
            order = 1
            for level_tag, lessons in c_data['levels']:
                for title, content, s_type in lessons:
                    CourseContent.objects.create(
                        course=course,
                        title=f'[{level_tag}] {title}',
                        content=content,
                        order=order,
                        section_type=s_type
                    )
                    order += 1
            print(f"18 lecciones Premium cargadas para {course.title}")
        except:
            pass

if __name__ == "__main__":
    run()
