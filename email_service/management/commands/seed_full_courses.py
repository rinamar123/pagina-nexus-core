import json
from django.core.management.base import BaseCommand
from django.utils import timezone
from enrollment.models import Course, CourseContent, Exam, Question, QuestionOption, InteractiveChallenge, CourseFile

LEVEL_PREFIXES = {
    'principiante': '[BASICO] ',
    'intermedio': '[INTERMEDIO] ',
    'avanzado': '[AVANZADO] ',
}

SECTION_TYPE_MAP = {
    'explicacion': 'explicacion',
    'ejemplo': 'ejemplo',
    'taller': 'demo',
    'demo': 'demo',
}


COURSES_DATA = [
    {
        'id': 1,
        'title': 'Fundamentos de Inteligencia Artificial',
        'icon': '🧠',
        'description': 'Sumérgete en el fascinante mundo de la Inteligencia Artificial. Este curso cubre desde la historia y filosofía de la IA hasta los algoritmos fundamentales de búsqueda, representación del conocimiento y sistemas expertos. Ideal para quienes inician su camino en la IA sin experiencia previa.',
        'duration': '16 semanas | 48 horas',
        'level': 'principiante',
        'order': 0,
        'instructor_name': 'Dr. Andrés Bravo',
        'instructor_bio': 'PhD en Ciencias de la Computación con 15+ años de experiencia en IA. Investigador en sistemas inteligentes y aprendizaje automático. Ha publicado más de 30 artículos en revistas indexadas y dirigido múltiples proyectos de innovación en IA aplicada.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=andres',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Historia y Filosofía de la IA',
                'content': '<h2>Introducción a la Inteligencia Artificial</h2><p>La Inteligencia Artificial (IA) es una rama de las ciencias de la computación que busca crear sistemas capaces de realizar tareas que requieren inteligencia humana. Desde sus inicios en la conferencia de Dartmouth en 1956, la IA ha evolucionado desde sistemas basados en reglas hasta modernas redes neuronales profundas.</p><h3>Hitos Fundamentales</h3><ul><li><strong>1950:</strong> Alan Turing publica "Computing Machinery and Intelligence" y propone el Test de Turing.</li><li><strong>1956:</strong> Conferencia de Dartmouth, donde nace oficialmente el campo de la IA.</li><li><strong>1966:</strong> ELIZA, el primer chatbot de la historia.</li><li><strong>1997:</strong> Deep Blue vence a Garry Kasparov en ajedrez.</li><li><strong>2012:</strong> AlexNet revoluciona la visión por computadora con deep learning.</li><li><strong>2020+:</strong> Modelos de lenguaje masivos como GPT transforman el procesamiento del lenguaje natural.</li></ul><p>La IA se divide en tres categorías: IA Débil (especializada en una tarea), IA General (capacidad cognitiva humana) y Superinteligencia (supera capacidades humanas). Actualmente nos encontramos en la era de la IA Débil, con avances acelerados hacia la IA General.</p>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Agentes Inteligentes y su Arquitectura',
                'content': '<h2>Agentes Inteligentes</h2><p>Un agente inteligente es cualquier entidad que percibe su entorno a través de sensores y actúa sobre él mediante actuadores. La arquitectura de un agente define cómo se mapean las percepciones a acciones.</p><h3>Tipos de Agentes</h3><ul><li><strong>Agente Reactivo Simple:</strong> Responde directamente a estímulos sin memoria interna. Ej: un termostato.</li><li><strong>Agente Reactivo Basado en Modelo:</strong> Mantiene un estado interno del mundo. Ej: un asistente virtual.</li><li><strong>Agente Basado en Metas:</strong> Además del estado, conoce objetivos y planifica para alcanzarlos. Ej: un robot de navegación.</li><li><strong>Agente Basado en Utilidad:</strong> Maximiza una función de utilidad para elegir la mejor acción. Ej: sistemas de recomendación.</li><li><strong>Agente Aprendiz:</strong> Mejora su rendimiento con la experiencia. Ej: AlphaGo.</li></ul><pre><code>class AgenteReactivo:&#10;    def __init__(self, reglas):&#10;        self.reglas = reglas&#10;    def actuar(self, percepcion):&#10;        for condicion, accion in self.reglas:&#10;            if condicion(percepcion):&#10;                return accion()&#10;        return accion_default()</code></pre>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Ejercicio: Diseña tu Propio Agente',
                'content': '<h2>Taller Práctico</h2><p>Diseña un agente inteligente para un asistente de recomendación de películas. El agente debe percibir el género favorito del usuario, las películas vistas y la calificación otorgada. Debe recomendar películas no vistas que maximicen la satisfacción esperada.</p><p><strong>Requisitos:</strong></p><ol><li>Define el conjunto de percepciones y acciones del agente.</li><li>Implementa una función de utilidad basada en calificaciones históricas.</li><li>Agrega un mecanismo de exploración vs explotación.</li><li>Prueba tu agente con un conjunto de datos de ejemplo.</li></ol><p>Entrega tu solución en un archivo Python comentado.</p>'
            },
        ]
    },
    {
        'id': 2,
        'title': 'Machine Learning Avanzado',
        'icon': '🤖',
        'description': 'Domina las técnicas más avanzadas de aprendizaje automático. Este curso profundiza en algoritmos de ensemble learning, máquinas de soporte vectorial, redes bayesianas, clustering avanzado y técnicas de regularización. Incluye proyectos prácticos con datasets reales.',
        'duration': '20 semanas | 60 horas',
        'level': 'intermedio',
        'order': 1,
        'instructor_name': 'Dr. Andrés Bravo',
        'instructor_bio': 'PhD en Ciencias de la Computación con 15+ años de experiencia en IA. Investigador en sistemas inteligentes y aprendizaje automático. Ha publicado más de 30 artículos en revistas indexadas y dirigido múltiples proyectos de innovación en IA aplicada.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=andres',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Fundamentos de Aprendizaje Supervisado',
                'content': '<h2>Aprendizaje Supervisado</h2><p>El aprendizaje supervisado es una técnica donde el modelo aprende a mapear entradas a salidas a partir de ejemplos etiquetados. Formalmente, dado un conjunto de datos $D = {(x_i, y_i)}_{i=1}^n$, buscamos una función $f: X \\rightarrow Y$ que generalice correctamente.</p><h3>Algoritmos Clásicos</h3><ul><li><strong>Regresión Lineal:</strong> $y = \\beta_0 + \\beta_1 x_1 + ... + \\beta_p x_p + \\epsilon$. Mínimos cuadrados ordinarios.</li><li><strong>Regresión Logística:</strong> $P(y=1|x) = 1/(1+e^{-\\beta^T x})$. Clasificación binaria.</li><li><strong>Árboles de Decisión:</strong> Particionamiento recursivo del espacio de características usando criterios como Gini o entropía.</li><li><strong>K-Vecinos Cercanos (KNN):</strong> Clasifica según la mayoría de los k vecinos más cercanos en el espacio de características.</li></ul><pre><code>from sklearn.linear_model import LinearRegression&#10;modelo = LinearRegression()&#10;modelo.fit(X_train, y_train)&#10;predicciones = modelo.predict(X_test)&#10;print(f"R²: {modelo.score(X_test, y_test):.3f}")</code></pre>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Ensemble Learning: Random Forest y Gradient Boosting',
                'content': '<h2>Ensemble Learning</h2><p>Los métodos ensemble combinan múltiples modelos débiles para crear un predictor fuerte. Dos técnicas principales:</p><h3>Bagging (Random Forest)</h3><p>Entrena múltiples árboles en paralelo usando subconjuntos bootstrap de los datos. La predicción final es el promedio (regresión) o voto mayoritario (clasificación). Reduce la varianza sin aumentar el sesgo.</p><h3>Boosting (Gradient Boosting)</h3><p>Entrena modelos secuencialmente, donde cada nuevo modelo corrige los errores del anterior. Algoritmos populares: AdaBoost, XGBoost, LightGBM, CatBoost.</p><pre><code>from sklearn.ensemble import RandomForestClassifier&#10;rf = RandomForestClassifier(n_estimators=100, max_depth=10)&#10;rf.fit(X_train, y_train)&#10;print(f"Accuracy RF: {rf.score(X_test, y_test):.3f}")</code></pre>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Proyecto: Clasificación de Dígitos',
                'content': '<h2>Taller: Clasificación de Dígitos con MNIST</h2><p>Implementa un clasificador para el dataset MNIST de dígitos escritos a mano usando al menos tres algoritmos diferentes. Compara su rendimiento y crea un ensemble que supere a cada modelo individual.</p><p><strong>Entregables:</strong></p><ol><li>Notebook Jupyter con el análisis exploratorio de datos.</li><li>Implementación de Random Forest, SVM y una red neuronal simple.</li><li>Ensemble por votación ponderada.</li><li>Matriz de confusión y reporte de clasificación.</li></ol>'
            },
        ]
    },
    {
        'id': 3,
        'title': 'Visión por Computadora',
        'icon': '👁️',
        'description': 'Explora cómo las máquinas interpretan el mundo visual. Aprende sobre procesamiento de imágenes, detección de características, convoluciones, redes neuronales convolucionales (CNN), detección de objetos, segmentación semántica y generación de imágenes con GANs.',
        'duration': '18 semanas | 54 horas',
        'level': 'intermedio',
        'order': 2,
        'instructor_name': 'Dr. Andrés Bravo',
        'instructor_bio': 'PhD en Ciencias de la Computación con 15+ años de experiencia en IA. Investigador en sistemas inteligentes y aprendizaje automático. Ha publicado más de 30 artículos en revistas indexadas y dirigido múltiples proyectos de innovación en IA aplicada.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=andres',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Fundamentos de Procesamiento de Imágenes',
                'content': '<h2>Procesamiento Digital de Imágenes</h2><p>Una imagen digital es una matriz bidimensional de píxeles, donde cada píxel representa un valor de intensidad. En imágenes a color, cada píxel tiene tres canales: Rojo, Verde y Azul (RGB).</p><h3>Operaciones Fundamentales</h3><ul><li><strong>Convolución:</strong> $(f * g)[i,j] = \\sum_m \\sum_n f[m,n] \\cdot g[i-m, j-n]$. Filtros de detección de bordes (Sobel, Canny).</li><li><strong>Umbralización:</strong> Convertir a binario usando un threshold: $I\'(x,y) = 1$ si $I(x,y) > T$, sino $0$.</li><li><strong>Ecualización del Histograma:</strong> Mejora el contraste distribuyendo uniformemente los valores de intensidad.</li><li><strong>Filtros Morfológicos:</strong> Erosión, dilatación, apertura y cierre para eliminar ruido.</li></ul><pre><code>import cv2&#10;import numpy as np&#10;img = cv2.imread("imagen.jpg", cv2.IMREAD_GRAYSCALE)&#10;bordes = cv2.Canny(img, 100, 200)&#10;cv2.imshow("Bordes", bordes)</code></pre>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Redes Neuronales Convolucionales (CNN)',
                'content': '<h2>Arquitectura CNN</h2><p>Las CNN están diseñadas para procesar datos con topología de cuadrícula (imágenes). Sus componentes principales:</p><ul><li><strong>Capas de Convolución:</strong> Aplican filtros aprendibles para extraer características. Cada filtro detecta patrones como bordes, texturas o formas.</li><li><strong>Capas de Pooling:</strong> Reducen la dimensionalidad (max pooling, average pooling).</li><li><strong>Capas Fully Connected:</strong> Clasifican basándose en las características extraídas.</li><li><strong>Arquitecturas Clásicas:</strong> LeNet-5, AlexNet, VGG16, ResNet, Inception, EfficientNet.</li></ul><pre><code>from tensorflow.keras import layers, models&#10;model = models.Sequential([&#10;    layers.Conv2D(32, (3,3), activation="relu", input_shape=(64,64,3)),&#10;    layers.MaxPooling2D(2,2),&#10;    layers.Conv2D(64, (3,3), activation="relu"),&#10;    layers.MaxPooling2D(2,2),&#10;    layers.Flatten(),&#10;    layers.Dense(128, activation="relu"),&#10;    layers.Dense(10, activation="softmax")&#10;])</code></pre>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Proyecto: Clasificador de Objetos',
                'content': '<h2>Taller: Clasificador de Imágenes</h2><p>Construye un clasificador de imágenes usando transfer learning con ResNet50 pre-entrenado en ImageNet. Clasifica al menos 5 categorías de objetos con un dataset propio.</p><p><strong>Pasos:</strong></p><ol><li>Recolecta al menos 50 imágenes por categoría.</li><li>Preprocesa las imágenes (redimensionar a 224x224, normalizar).</li><li>Carga ResNet50 sin la capa superior y congela los pesos.</li><li>Agrega capas fully connected personalizadas.</li><li>Entrena y evalúa el modelo.</li><li>Implementa una función de predicción para nuevas imágenes.</li></ol>'
            },
        ]
    },
    {
        'id': 4,
        'title': 'Procesamiento del Lenguaje Natural',
        'icon': '📝',
        'description': 'Aprende cómo las máquinas entienden, procesan y generan lenguaje humano. Desde tokenización y análisis sintáctico hasta transformers y modelos de lenguaje como BERT y GPT. Incluye proyectos de análisis de sentimientos, chatbots y traducción automática.',
        'duration': '18 semanas | 54 horas',
        'level': 'avanzado',
        'order': 3,
        'instructor_name': 'Dr. Andrés Bravo',
        'instructor_bio': 'PhD en Ciencias de la Computación con 15+ años de experiencia en IA. Investigador en sistemas inteligentes y aprendizaje automático. Ha publicado más de 30 artículos en revistas indexadas y dirigido múltiples proyectos de innovación en IA aplicada.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=andres',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Fundamentos de NLP',
                'content': '<h2>Procesamiento del Lenguaje Natural</h2><p>El NLP combina lingüística computacional con modelos estadísticos y deep learning para procesar texto. Etapas clave del pipeline de NLP:</p><h3>Preprocesamiento</h3><ul><li><strong>Tokenización:</strong> Dividir texto en palabras o subpalabras.</li><li><strong>Stemming y Lemmatization:</strong> Reducir palabras a su raíz.</li><li><strong>Stop Words:</strong> Eliminar palabras frecuentes sin significado.</li><li><strong>POS Tagging:</strong> Etiquetado gramatical de cada palabra.</li><li><strong>NER:</strong> Reconocimiento de entidades nombradas (personas, lugares, fechas).</li></ul><h3>Representación de Texto</h3><ul><li><strong>Bag of Words (BoW):</strong> Vector de frecuencia de palabras.</li><li><strong>TF-IDF:</strong> $tfidf(t,d,D) = tf(t,d) \\cdot log(N/df(t))$. Pondera términos raros.</li><li><strong>Word Embeddings:</strong> Word2Vec, GloVe, FastText.</li></ul><pre><code>import nltk&#10;from sklearn.feature_extraction.text import TfidfVectorizer&#10;textos = ["IA es el futuro", "El aprendizaje automatico es IA"]&#10;vectorizer = TfidfVectorizer()&#10;X = vectorizer.fit_transform(textos)</code></pre>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Transformers y Modelos de Lenguaje',
                'content': '<h2>Arquitectura Transformer</h2><p>El transformer, introducido en "Attention is All You Need" (Vaswani et al., 2017), revolucionó el NLP eliminando las recurrencias y usando solo mecanismos de atención.</p><h3>Componentes Clave</h3><ul><li><strong>Self-Attention:</strong> $Attention(Q,K,V) = softmax(QK^T/\\sqrt{d_k})V$. Cada palabra atiende a todas las demás.</li><li><strong>Multi-Head Attention:</strong> Múltiples cabezas de atención en paralelo capturan diferentes relaciones.</li><li><strong>Positional Encoding:</strong> Codifica la posición de cada token en la secuencia.</li><li><strong>Encoder-Decoder:</strong> El encoder procesa la entrada, el decoder genera la salida.</li></ul><p>Modelos populares basados en transformers: BERT (encoder-only), GPT (decoder-only), T5 (encoder-decoder).</p>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Análisis de Sentimientos con BERT',
                'content': '<h2>Taller: Análisis de Sentimientos</h2><p>Implementa un clasificador de sentimientos usando BERT (Bidirectional Encoder Representations from Transformers) con la biblioteca Hugging Face Transformers.</p><p><strong>Tareas:</strong></p><ol><li>Instala transformers y torch.</li><li>Carga el modelo pre-entrenado bert-base-uncased.</li><li>Tokeniza reseñas de películas del dataset IMDB.</li><li>Fine-tune el modelo para clasificación binaria (positivo/negativo).</li><li>Evalúa con precisión, recall y F1-score.</li><li>Prueba con reseñas escritas por ti mismo.</li></ol>'
            },
        ]
    },
    {
        'id': 5,
        'title': 'Regresión Lineal Predictiva',
        'icon': '📈',
        'description': 'Domina la técnica estadística más utilizada en análisis de datos. Aprende desde los fundamentos matemáticos de mínimos cuadrados hasta implementaciones avanzadas con regularización, detección de outliers y validación cruzada. Incluye proyectos con datos económicos y financieros reales.',
        'duration': '14 semanas | 42 horas',
        'level': 'intermedio',
        'order': 4,
        'instructor_name': 'Dr. Carlos Mendoza',
        'instructor_bio': 'PhD en Estadística Aplicada con 12 años de experiencia en modelado predictivo. Especialista en econometría y series temporales. Ha liderado equipos de data science en bancos y consultoras internacionales.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=carlos',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Fundamentos de la Regresión Lineal',
                'content': '<h2>Regresión Lineal Simple</h2><p>La regresión lineal modela la relación entre una variable dependiente $Y$ y una independiente $X$: $Y = \\beta_0 + \\beta_1 X + \\epsilon$</p><h3>Estimación por Mínimos Cuadrados</h3><p>Minimizamos la suma de errores cuadrados: $\\min \\sum_{i=1}^n (y_i - \\hat{y}_i)^2$</p><p>Las soluciones: $\\hat{\\beta}_1 = \\frac{\\sum(x_i - \\bar{x})(y_i - \\bar{y})}{\\sum(x_i - \\bar{x})^2}$, $\\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1 \\bar{x}$</p><h3>Supuestos del Modelo</h3><ul><li>Linealidad: relación lineal entre $X$ e $Y$.</li><li>Independencia: errores independientes.</li><li>Homocedasticidad: varianza constante de errores.</li><li>Normalidad: errores con distribución normal.</li></ul>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Regresión Múltiple y Regularización',
                'content': '<h2>Regresión Lineal Múltiple</h2><p>Extiende la regresión simple a múltiples variables: $Y = \\beta_0 + \\beta_1 X_1 + \\beta_2 X_2 + ... + \\beta_p X_p + \\epsilon$</p><h3>Regularización</h3><ul><li><strong>Ridge (L2):</strong> $\\min ||y - X\\beta||^2 + \\lambda||\\beta||^2$. Reduce coeficientes sin eliminar variables.</li><li><strong>Lasso (L1):</strong> $\\min ||y - X\\beta||^2 + \\lambda||\\beta||_1$. Puede llevar coeficientes a cero (selección de características).</li><li><strong>Elastic Net:</strong> Combina L1 y L2: $\\lambda(\\alpha||\\beta||_1 + (1-\\alpha)||\\beta||^2/2)$.</li></ul>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Predicción de Precios de Viviendas',
                'content': '<h2>Taller: Predicción con Regresión</h2><p>Usa el dataset de Boston Housing o California Housing para construir un modelo predictivo del precio de viviendas.</p><p><strong>Entregables:</strong></p><ol><li>Análisis exploratorio con visualizaciones (correlaciones, distribuciones, outliers).</li><li>Implementación de regresión lineal múltiple desde cero en NumPy.</li><li>Comparación con implementación de scikit-learn.</li><li>Ridge, Lasso y Elastic Net con validación cruzada.</li><li>Selección del mejor modelo basado en R² y RMSE.</li><li>Interpretación de coeficientes y conclusiones.</li></ol>'
            },
        ]
    },
    {
        'id': 6,
        'title': 'Algoritmos Genéticos',
        'icon': '🧬',
        'description': 'Descubre cómo la evolución biológica inspira algoritmos de optimización. Aprende sobre selección natural, cruce, mutación y cómo aplicar estos conceptos para resolver problemas complejos de optimización, planificación y diseño automático.',
        'duration': '12 semanas | 36 horas',
        'level': 'intermedio',
        'order': 5,
        'instructor_name': 'Dra. Laura Espinosa',
        'instructor_bio': 'PhD en Ingeniería de Sistemas con especialización en computación evolutiva. 10 años investigando algoritmos bio-inspirados. Autora de múltiples publicaciones sobre optimización multiobjetivo y algoritmos genéticos aplicados a ingeniería.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=laura',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Fundamentos de Algoritmos Evolutivos',
                'content': '<h2>Algoritmos Genéticos</h2><p>Los algoritmos genéticos (AG) son métodos de búsqueda y optimización inspirados en la evolución natural. Fueron desarrollados por John Holland en la década de 1970.</p><h3>Componentes Clave</h3><ul><li><strong>Población:</strong> Conjunto de soluciones candidatas (cromosomas).</li><li><strong>Fitness:</strong> Función que evalúa la calidad de cada solución.</li><li><strong>Selección:</strong> Elige los mejores individuos para reproducirse (ruleta, torneo, ranking).</li><li><strong>Cruce (Crossover):</strong> Combina dos padres para generar hijos. Punto simple, uniforme, aritmético.</li><li><strong>Mutación:</strong> Altera aleatoriamente genes para mantener diversidad.</li><li><strong>Elitismo:</strong> Preserva los mejores individuos en cada generación.</li></ul><pre><code>import random&#10;def crear_individuo(longitud):&#10;    return [random.randint(0,1) for _ in range(longitud)]&#10;def fitness(individuo):&#10;    return sum(individuo)  # Maximizar cantidad de unos</code></pre>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Operadores Genéticos y Estrategias Avanzadas',
                'content': '<h2>Operadores Genéticos</h2><h3>Cruce Uniforme</h3><p>Cada gen del hijo se hereda aleatoriamente de uno de los dos padres. Útil cuando no hay dependencia posicional entre genes.</p><h3>Mutación Adaptativa</h3><p>La tasa de mutación se ajusta dinámicamente: aumenta si la población se estanca en un óptimo local, disminuye si hay suficiente diversidad.</p><h3>Estrategias Avanzadas</h3><ul><li><strong>NSGA-II:</strong> Algoritmo genético multiobjetivo (Pareto-óptimo).</li><li><strong>CHC:</strong> Cruce con reinicio selectivo para evitar estancamiento.</li><li><strong>Algoritmos Meméticos:</strong> Combinan AG con búsqueda local.</li><li><strong>Programación Genética:</strong> Los individuos son árboles de programas.</li></ul>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Optimización del Problema del Viajante',
                'content': '<h2>Taller: Problema del Viajante (TSP)</h2><p>Implementa un algoritmo genético para resolver el Problema del Viajante, donde se deben visitar N ciudades minimizando la distancia total recorrida.</p><p><strong>Especificaciones:</strong></p><ol><li>Representación: permutación de ciudades (codificación ordinal).</li><li>Fitness: inverso de la distancia total del recorrido.</li><li>Selección: torneo de tamaño 3.</li><li>Cruce: Order Crossover (OX) o Partially Mapped Crossover (PMX).</li><li>Mutación: swap de dos ciudades o inversión de segmento.</li><li>Elitismo: preserva el 5% de la población.</li><li>Prueba con 20, 50 y 100 ciudades.</li></ol>'
            },
        ]
    },
    {
        'id': 7,
        'title': 'Inteligencia Artificial: Fundamentos y Aplicaciones',
        'icon': '🤖',
        'description': 'Un recorrido completo por las aplicaciones prácticas de la IA en la industria moderna. Desde sistemas de recomendación hasta vehículos autónomos, pasando por diagnóstico médico y asistentes virtuales. Enfoque 100% práctico con proyectos reales.',
        'duration': '16 semanas | 48 horas',
        'level': 'principiante',
        'order': 6,
        'instructor_name': 'Dr. Andrés Bravo',
        'instructor_bio': 'PhD en Ciencias de la Computación con 15+ años de experiencia en IA. Investigador en sistemas inteligentes y aprendizaje automático. Ha publicado más de 30 artículos en revistas indexadas y dirigido múltiples proyectos de innovación en IA aplicada.',
        'instructor_avatar_url': 'https://i.pravatar.cc/150?u=andres',
        'lessons': [
            {
                'section_type': 'explicacion', 'order': 0,
                'title': 'Introducción a las Aplicaciones de IA',
                'content': '<h2>IA en la Industria</h2><p>La Inteligencia Artificial está transformando todos los sectores industriales. Este módulo explora las aplicaciones más impactantes de la IA en el mundo real.</p><h3>Sectores Clave</h3><ul><li><strong>Salud:</strong> Diagnóstico asistido por IA, análisis de imágenes médicas, descubrimiento de fármacos.</li><li><strong>Finanzas:</strong> Detección de fraude, trading algorítmico, scoring crediticio.</li><li><strong>Transporte:</strong> Vehículos autónomos, optimización de rutas, logística inteligente.</li><li><strong>Comercio:</strong> Sistemas de recomendación, personalización, chatbots de atención al cliente.</li><li><strong>Manufactura:</strong> Mantenimiento predictivo, control de calidad visual, robótica colaborativa.</li><li><strong>Educación:</strong> Tutores inteligentes, aprendizaje adaptativo, evaluación automatizada.</li></ul>'
            },
            {
                'section_type': 'ejemplo', 'order': 1,
                'title': 'Sistemas de Recomendación',
                'content': '<h2>Sistemas de Recomendación</h2><p>Los sistemas de recomendación filtran información para predecir la preferencia de un usuario sobre un ítem.</p><h3>Tipos Principales</h3><ul><li><strong>Filtrado Colaborativo:</strong> Recomienda basándose en preferencias de usuarios similares. $\\hat{r}_{ui} = \\mu + b_u + b_i$</li><li><strong>Filtrado Basado en Contenido:</strong> Recomienda ítems similares a los que el usuario ha preferido antes.</li><li><strong>Híbridos:</strong> Combinan ambos enfoques para mayor precisión.</li></ul><h3>Métricas de Evaluación</h3><ul><li>Precision@K, Recall@K, MAP (Mean Average Precision)</li><li>RMSE, MAE para predicciones de rating</li><li>NDCG (Normalized Discounted Cumulative Gain)</li></ul>'
            },
            {
                'section_type': 'taller', 'order': 2,
                'title': 'Crea un Sistema de Recomendación',
                'content': '<h2>Taller: Motor de Recomendación</h2><p>Implementa un sistema de recomendación de películas usando el dataset MovieLens (100k ratings).</p><p><strong>Requisitos:</strong></p><ol><li>Carga y explora el dataset MovieLens.</li><li>Implementa filtrado colaborativo basado en usuarios (User-User).</li><li>Implementa filtrado colaborativo basado en ítems (Item-Item).</li><li>Implementa descomposición de matrices (SVD).</li><li>Compara los métodos usando RMSE en validación cruzada.</li><li>Construye una función que recomiende N películas para un usuario dado.</li></ol>'
            },
        ]
    },
]


EXAMS_DATA = [
    {
        'course_id': 1,
        'title': 'Examen Final: Fundamentos de IA',
        'description': 'Evalúa tu comprensión de los conceptos fundamentales de Inteligencia Artificial, historia, tipos de agentes y aplicaciones.',
        'passing_score': 60,
        'time_limit_minutes': 45,
        'questions': [
            {'text': '¿En qué año se celebró la conferencia de Dartmouth, considerada el nacimiento oficial de la IA?', 'order': 0, 'options': [
                {'text': '1950', 'is_correct': False, 'order': 0},
                {'text': '1956', 'is_correct': True, 'order': 1},
                {'text': '1960', 'is_correct': False, 'order': 2},
                {'text': '1945', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué tipo de agente mantiene un estado interno del mundo para tomar decisiones?', 'order': 1, 'options': [
                {'text': 'Agente Reactivo Simple', 'is_correct': False, 'order': 0},
                {'text': 'Agente Reactivo Basado en Modelo', 'is_correct': True, 'order': 1},
                {'text': 'Agente Basado en Metas', 'is_correct': False, 'order': 2},
                {'text': 'Agente Aprendiz', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué prueba propuso Alan Turing para evaluar la inteligencia de una máquina?', 'order': 2, 'options': [
                {'text': 'Prueba de Turing', 'is_correct': True, 'order': 0},
                {'text': 'Prueba de Voight-Kampff', 'is_correct': False, 'order': 1},
                {'text': 'Prueba de Lovelace', 'is_correct': False, 'order': 2},
                {'text': 'Prueba de Chinese Room', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué rama de la IA se enfoca en crear sistemas que aprenden de datos?', 'order': 3, 'options': [
                {'text': 'Sistemas Expertos', 'is_correct': False, 'order': 0},
                {'text': 'Robótica', 'is_correct': False, 'order': 1},
                {'text': 'Machine Learning', 'is_correct': True, 'order': 2},
                {'text': 'Lógica Difusa', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Cuál de los siguientes NO es un tipo de aprendizaje automático?', 'order': 4, 'options': [
                {'text': 'Supervisado', 'is_correct': False, 'order': 0},
                {'text': 'No Supervisado', 'is_correct': False, 'order': 1},
                {'text': 'Por Refuerzo', 'is_correct': False, 'order': 2},
                {'text': 'Por Osmosis', 'is_correct': True, 'order': 3},
            ]},
        ]
    },
    {
        'course_id': 2,
        'title': 'Examen Final: Machine Learning Avanzado',
        'description': 'Evalúa tu dominio de algoritmos de machine learning, ensemble methods y evaluación de modelos.',
        'passing_score': 60,
        'time_limit_minutes': 60,
        'questions': [
            {'text': '¿Qué técnica de ensemble entrena modelos secuencialmente corrigiendo errores anteriores?', 'order': 0, 'options': [
                {'text': 'Bagging', 'is_correct': False, 'order': 0},
                {'text': 'Boosting', 'is_correct': True, 'order': 1},
                {'text': 'Stacking', 'is_correct': False, 'order': 2},
                {'text': 'Votación', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué métrica es más apropiada para un problema de clasificación desbalanceado?', 'order': 1, 'options': [
                {'text': 'Accuracy', 'is_correct': False, 'order': 0},
                {'text': 'F1-Score', 'is_correct': True, 'order': 1},
                {'text': 'R²', 'is_correct': False, 'order': 2},
                {'text': 'RMSE', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué hace la regularización Lasso (L1)?', 'order': 2, 'options': [
                {'text': 'Aumenta la complejidad del modelo', 'is_correct': False, 'order': 0},
                {'text': 'Puede llevar coeficientes a cero', 'is_correct': True, 'order': 1},
                {'text': 'Reduce la varianza sin cambiar coeficientes', 'is_correct': False, 'order': 2},
                {'text': 'Solo funciona con redes neuronales', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Cuál es el propósito de la validación cruzada (cross-validation)?', 'order': 3, 'options': [
                {'text': 'Aumentar el tamaño del dataset', 'is_correct': False, 'order': 0},
                {'text': 'Evaluar la capacidad de generalización del modelo', 'is_correct': True, 'order': 1},
                {'text': 'Reducir el tiempo de entrenamiento', 'is_correct': False, 'order': 2},
                {'text': 'Eliminar datos atípicos', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué algoritmo es mejor para datos con muchas características y pocas muestras?', 'order': 4, 'options': [
                {'text': 'KNN', 'is_correct': False, 'order': 0},
                {'text': 'Regresión Logística con L2', 'is_correct': True, 'order': 1},
                {'text': 'Árbol de Decisión sin podar', 'is_correct': False, 'order': 2},
                {'text': 'Naive Bayes', 'is_correct': False, 'order': 3},
            ]},
        ]
    },
    {
        'course_id': 3,
        'title': 'Examen Final: Visión por Computadora',
        'description': 'Evalúa tus conocimientos en procesamiento de imágenes, CNNs y detección de objetos.',
        'passing_score': 60,
        'time_limit_minutes': 60,
        'questions': [
            {'text': '¿Qué operación matemática es fundamental en las capas convolucionales?', 'order': 0, 'options': [
                {'text': 'Multiplicación de matrices', 'is_correct': False, 'order': 0},
                {'text': 'Convolución', 'is_correct': True, 'order': 1},
                {'text': 'Transformada de Fourier', 'is_correct': False, 'order': 2},
                {'text': 'Derivación', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué capa reduce la dimensionalidad espacial en una CNN?', 'order': 1, 'options': [
                {'text': 'Convolución', 'is_correct': False, 'order': 0},
                {'text': 'Pooling', 'is_correct': True, 'order': 1},
                {'text': 'Dropout', 'is_correct': False, 'order': 2},
                {'text': 'Batch Normalization', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué arquitectura introdujo el concepto de conexiones residuales?', 'order': 2, 'options': [
                {'text': 'VGG16', 'is_correct': False, 'order': 0},
                {'text': 'ResNet', 'is_correct': True, 'order': 1},
                {'text': 'AlexNet', 'is_correct': False, 'order': 2},
                {'text': 'LeNet-5', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué técnica permite usar un modelo pre-entrenado en un nuevo dataset?', 'order': 3, 'options': [
                {'text': 'Data Augmentation', 'is_correct': False, 'order': 0},
                {'text': 'Transfer Learning', 'is_correct': True, 'order': 1},
                {'text': 'Fine-tuning inverso', 'is_correct': False, 'order': 2},
                {'text': 'Zero-shot learning', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué detector de objetos usa regiones propuestas?', 'order': 4, 'options': [
                {'text': 'YOLO', 'is_correct': False, 'order': 0},
                {'text': 'Faster R-CNN', 'is_correct': True, 'order': 1},
                {'text': 'SSD', 'is_correct': False, 'order': 2},
                {'text': 'RetinaNet', 'is_correct': False, 'order': 3},
            ]},
        ]
    },
    {
        'course_id': 4,
        'title': 'Examen Final: Procesamiento del Lenguaje Natural',
        'description': 'Evalúa tu comprensión de NLP, transformers y modelos de lenguaje.',
        'passing_score': 60,
        'time_limit_minutes': 60,
        'questions': [
            {'text': '¿Qué técnica de representación de texto asigna vectores densos con significado semántico?', 'order': 0, 'options': [
                {'text': 'Bag of Words', 'is_correct': False, 'order': 0},
                {'text': 'Word Embeddings', 'is_correct': True, 'order': 1},
                {'text': 'TF-IDF', 'is_correct': False, 'order': 2},
                {'text': 'One-Hot Encoding', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué mecanismo es central en la arquitectura Transformer?', 'order': 1, 'options': [
                {'text': 'Memoria a largo plazo', 'is_correct': False, 'order': 0},
                {'text': 'Self-Attention', 'is_correct': True, 'order': 1},
                {'text': 'Puertas de recurrencia', 'is_correct': False, 'order': 2},
                {'text': 'Convoluciones dilatadas', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué modelo de lenguaje usa solo el decoder de la arquitectura transformer?', 'order': 2, 'options': [
                {'text': 'BERT', 'is_correct': False, 'order': 0},
                {'text': 'GPT', 'is_correct': True, 'order': 1},
                {'text': 'T5', 'is_correct': False, 'order': 2},
                {'text': 'RoBERTa', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué tarea de NLP identifica personas, lugares y fechas en un texto?', 'order': 3, 'options': [
                {'text': 'POS Tagging', 'is_correct': False, 'order': 0},
                {'text': 'NER (Named Entity Recognition)', 'is_correct': True, 'order': 1},
                {'text': 'Análisis de sentimientos', 'is_correct': False, 'order': 2},
                {'text': 'Resumen automático', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué métrica se usa comúnmente para evaluar la calidad de traducción automática?', 'order': 4, 'options': [
                {'text': 'Perplejidad', 'is_correct': False, 'order': 0},
                {'text': 'BLEU', 'is_correct': True, 'order': 1},
                {'text': 'ROUGE', 'is_correct': False, 'order': 2},
                {'text': 'CER', 'is_correct': False, 'order': 3},
            ]},
        ]
    },
    {
        'course_id': 5,
        'title': 'Examen Final: Regresión Lineal Predictiva',
        'description': 'Evalúa tu dominio de la regresión lineal, supuestos del modelo y técnicas de regularización.',
        'passing_score': 60,
        'time_limit_minutes': 45,
        'questions': [
            {'text': '¿Qué método se usa para estimar los coeficientes en regresión lineal?', 'order': 0, 'options': [
                {'text': 'Máxima verosimilitud', 'is_correct': False, 'order': 0},
                {'text': 'Mínimos cuadrados ordinarios', 'is_correct': True, 'order': 1},
                {'text': 'Descenso de gradiente', 'is_correct': False, 'order': 2},
                {'text': 'Método de Newton', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué supuesto de la regresión lineal indica que la varianza de los errores es constante?', 'order': 1, 'options': [
                {'text': 'Linealidad', 'is_correct': False, 'order': 0},
                {'text': 'Homocedasticidad', 'is_correct': True, 'order': 1},
                {'text': 'Normalidad', 'is_correct': False, 'order': 2},
                {'text': 'Independencia', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué métrica indica la proporción de varianza explicada por el modelo?', 'order': 2, 'options': [
                {'text': 'RMSE', 'is_correct': False, 'order': 0},
                {'text': 'MAE', 'is_correct': False, 'order': 1},
                {'text': 'R²', 'is_correct': True, 'order': 2},
                {'text': 'AIC', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué problema indica que las variables predictoras están correlacionadas entre sí?', 'order': 3, 'options': [
                {'text': 'Heterocedasticidad', 'is_correct': False, 'order': 0},
                {'text': 'Multicolinealidad', 'is_correct': True, 'order': 1},
                {'text': 'Sobreajuste', 'is_correct': False, 'order': 2},
                {'text': 'Subajuste', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué técnica de regularización agrega la norma L2 a la función de costo?', 'order': 4, 'options': [
                {'text': 'Lasso', 'is_correct': False, 'order': 0},
                {'text': 'Ridge', 'is_correct': True, 'order': 1},
                {'text': 'Elastic Net', 'is_correct': False, 'order': 2},
                {'text': 'Dropout', 'is_correct': False, 'order': 3},
            ]},
        ]
    },
    {
        'course_id': 6,
        'title': 'Examen Final: Algoritmos Genéticos',
        'description': 'Evalúa tu comprensión de los algoritmos evolutivos, operadores genéticos y optimización.',
        'passing_score': 60,
        'time_limit_minutes': 45,
        'questions': [
            {'text': '¿Quién desarrolló los algoritmos genéticos en la década de 1970?', 'order': 0, 'options': [
                {'text': 'Alan Turing', 'is_correct': False, 'order': 0},
                {'text': 'John Holland', 'is_correct': True, 'order': 1},
                {'text': 'John McCarthy', 'is_correct': False, 'order': 2},
                {'text': 'Marvin Minsky', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué operador genético combina dos padres para generar descendencia?', 'order': 1, 'options': [
                {'text': 'Mutación', 'is_correct': False, 'order': 0},
                {'text': 'Cruce (Crossover)', 'is_correct': True, 'order': 1},
                {'text': 'Selección', 'is_correct': False, 'order': 2},
                {'text': 'Elitismo', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué técnica preserva los mejores individuos de cada generación?', 'order': 2, 'options': [
                {'text': 'Selección por torneo', 'is_correct': False, 'order': 0},
                {'text': 'Elitismo', 'is_correct': True, 'order': 1},
                {'text': 'Cruce uniforme', 'is_correct': False, 'order': 2},
                {'text': 'Mutación adaptativa', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué algoritmo genético está diseñado para optimización multiobjetivo?', 'order': 3, 'options': [
                {'text': 'AG simple', 'is_correct': False, 'order': 0},
                {'text': 'NSGA-II', 'is_correct': True, 'order': 1},
                {'text': 'CHC', 'is_correct': False, 'order': 2},
                {'text': 'Programación Genética', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué tipo de problema se resuelve típicamente con codificación de permutaciones?', 'order': 4, 'options': [
                {'text': 'Optimización de funciones continuas', 'is_correct': False, 'order': 0},
                {'text': 'Problema del Viajante (TSP)', 'is_correct': True, 'order': 1},
                {'text': 'Clasificación de imágenes', 'is_correct': False, 'order': 2},
                {'text': 'Regresión lineal', 'is_correct': False, 'order': 3},
            ]},
        ]
    },
    {
        'course_id': 7,
        'title': 'Examen Final: Fundamentos y Aplicaciones',
        'description': 'Evalúa tu conocimiento sobre las aplicaciones prácticas de la IA en diversos sectores.',
        'passing_score': 60,
        'time_limit_minutes': 45,
        'questions': [
            {'text': '¿Qué tipo de sistema de recomendación usa preferencias de usuarios similares?', 'order': 0, 'options': [
                {'text': 'Basado en contenido', 'is_correct': False, 'order': 0},
                {'text': 'Filtrado colaborativo', 'is_correct': True, 'order': 1},
                {'text': 'Híbrido', 'is_correct': False, 'order': 2},
                {'text': 'Basado en reglas', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué sector utiliza IA para detección de fraudes en tiempo real?', 'order': 1, 'options': [
                {'text': 'Salud', 'is_correct': False, 'order': 0},
                {'text': 'Finanzas', 'is_correct': True, 'order': 1},
                {'text': 'Educación', 'is_correct': False, 'order': 2},
                {'text': 'Manufactura', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué técnica de IA usan los asistentes virtuales como Siri o Alexa?', 'order': 2, 'options': [
                {'text': 'Visión por computadora', 'is_correct': False, 'order': 0},
                {'text': 'Procesamiento del lenguaje natural', 'is_correct': True, 'order': 1},
                {'text': 'Algoritmos genéticos', 'is_correct': False, 'order': 2},
                {'text': 'Sistemas expertos', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué aplicación de IA permite a los vehículos detectar peatones y señales?', 'order': 3, 'options': [
                {'text': 'NLP', 'is_correct': False, 'order': 0},
                {'text': 'Visión por computadora', 'is_correct': True, 'order': 1},
                {'text': 'Sistemas de recomendación', 'is_correct': False, 'order': 2},
                {'text': 'Robótica', 'is_correct': False, 'order': 3},
            ]},
            {'text': '¿Qué métrica se usa para evaluar sistemas de recomendación?', 'order': 4, 'options': [
                {'text': 'BLEU', 'is_correct': False, 'order': 0},
                {'text': 'Precision@K', 'is_correct': True, 'order': 1},
                {'text': 'Perplejidad', 'is_correct': False, 'order': 2},
                {'text': 'IOU', 'is_correct': False, 'order': 3},
            ]},
        ]
    },
]


CHALLENGES_DATA = [
    {'course_id': 1, 'prompt': '¿Cuál de los siguientes NO es un tipo de agente inteligente?', 'code_snippet': '# Selecciona la respuesta correcta\ntipos_agentes = ["Reactivo Simple", "Basado en Metas", "Termodinámico", "Aprendiz"]', 'choices': ['Reactivo Simple', 'Basado en Metas', 'Termodinámico', 'Aprendiz'], 'correct_index': 2},
    {'course_id': 1, 'prompt': '¿Qué año se considera el nacimiento oficial de la IA?', 'code_snippet': 'hitos_ia = {\n    1950: "Test de Turing",\n    1956: "Conferencia Dartmouth",\n    1966: "ELIZA",\n    1997: "Deep Blue"\n}', 'choices': ['1950', '1956', '1966', '1997'], 'correct_index': 1},
    {'course_id': 1, 'prompt': '¿Qué arquitectura de agente utiliza una función de utilidad?', 'code_snippet': '# Arquitecturas de agentes\n# - Reactivo Simple\n# - Basado en Modelo\n# - Basado en Utilidad\n# - Aprendiz', 'choices': ['Reactivo Simple', 'Basado en Modelo', 'Basado en Utilidad', 'Aprendiz'], 'correct_index': 2},
    {'course_id': 2, 'prompt': '¿Qué técnica de ensemble learning entrena modelos en paralelo?', 'code_snippet': 'from sklearn.ensemble import RandomForestClassifier\nrf = RandomForestClassifier(n_estimators=100)\nrf.fit(X_train, y_train)', 'choices': ['Boosting', 'Bagging', 'Stacking', 'Votación'], 'correct_index': 1},
    {'course_id': 2, 'prompt': '¿Cuál es la métrica más apropiada para clasificación desbalanceada?', 'code_snippet': 'from sklearn.metrics import ???\n# ¿Qué métrica usar?', 'choices': ['Accuracy', 'F1-Score', 'RMSE', 'R²'], 'correct_index': 1},
    {'course_id': 2, 'prompt': '¿Qué hace la regularización Lasso?', 'code_snippet': '# Regularización\n# L1: ???\n# L2: Ridge', 'choices': ['Reduce todos los coeficientes proporcionalmente', 'Puede llevar coeficientes a cero', 'Aumenta la complejidad', 'Elimina datos atípicos'], 'correct_index': 1},
    {'course_id': 3, 'prompt': '¿Qué capa de una CNN reduce la dimensionalidad espacial?', 'code_snippet': 'model = models.Sequential([\n    layers.Conv2D(32, (3,3)),\n    layers.___(2,2),\n    layers.Flatten()\n])', 'choices': ['Conv2D', 'MaxPooling2D', 'Dropout', 'Dense'], 'correct_index': 1},
    {'course_id': 3, 'prompt': '¿Qué técnica permite reutilizar un modelo pre-entrenado?', 'code_snippet': '# Técnica de aprendizaje\n# Modelo pre-entrenado + nuevo dataset', 'choices': ['Transfer Learning', 'Data Augmentation', 'Fine-tuning', 'Zero-shot'], 'correct_index': 0},
    {'course_id': 4, 'prompt': '¿Qué mecanismo es central en la arquitectura Transformer?', 'code_snippet': 'class Transformer:\n    def __init__(self):\n        self.attention = ___()', 'choices': ['Self-Attention', 'LSTM', 'Convolución', 'Pooling'], 'correct_index': 0},
    {'course_id': 4, 'prompt': '¿Qué tarea de NLP identifica entidades como personas y lugares?', 'code_snippet': 'import spacy\nnlp = spacy.load("es_core_news_sm")\ndoc = nlp("Apple compra UK start-up por $1bn")\nfor ent in doc.ents:\n    print(ent.text, ent.label_)', 'choices': ['POS Tagging', 'NER', 'Análisis de sentimientos', 'Resumen'], 'correct_index': 1},
    {'course_id': 5, 'prompt': '¿Qué supuesto indica que la relación entre variables es lineal?', 'code_snippet': '# Supuestos de regresión lineal\n# Y = β₀ + β₁X + ε', 'choices': ['Homocedasticidad', 'Normalidad', 'Linealidad', 'Independencia'], 'correct_index': 2},
    {'course_id': 5, 'prompt': '¿Qué métrica mide la proporción de varianza explicada?', 'code_snippet': 'from sklearn.metrics import ???\ny_true = [3, 5, 2, 7]\ny_pred = [2.8, 5.1, 2.2, 6.8]\nprint(???(y_true, y_pred))', 'choices': ['MAE', 'RMSE', 'R²', 'AIC'], 'correct_index': 2},
    {'course_id': 6, 'prompt': '¿Qué operador genético introduce diversidad en la población?', 'code_snippet': '# Operadores genéticos\n# 1. Selección\n# 2. Cruce\n# 3. ???', 'choices': ['Elitismo', 'Mutación', 'Evaluación', 'Decodificación'], 'correct_index': 1},
    {'course_id': 6, 'prompt': '¿Qué tipo de selección elige aleatoriamente pero con probabilidad proporcional al fitness?', 'code_snippet': 'def seleccion(poblacion, fitness):\n    total = sum(fitness)\n    r = random.uniform(0, total)\n    # ¿Qué tipo de selección?', 'choices': ['Selección por torneo', 'Selección por ruleta', 'Selección por ranking', 'Selección elitista'], 'correct_index': 1},
    {'course_id': 7, 'prompt': '¿Qué tipo de sistema de recomendación usa similitud entre ítems?', 'code_snippet': '# Sistemas de recomendación\n# - User-User\n# - Item-Item\n# - Híbrido', 'choices': ['Filtrado colaborativo User-User', 'Filtrado colaborativo Item-Item', 'Basado en contenido', 'Híbrido'], 'correct_index': 1},
    {'course_id': 7, 'prompt': '¿Qué sector usa IA para diagnóstico asistido por imágenes?', 'code_snippet': '# Aplicaciones de IA por sector\nsalud: ???\nfinanzas: detección de fraude\ncomercio: recomendaciones', 'choices': ['Detección de fraude', 'Diagnóstico por imágenes', 'Vehículos autónomos', 'Chatbots'], 'correct_index': 1},
]


FEEDBACK_MAP = {
    0: '¡Incorrecto! Revisa el material sobre este concepto.',
    1: '¡Correcto! Excelente comprensión del tema.',
    2: 'No es la respuesta correcta. Vuelve a estudiar esta sección.',
    3: 'Incorrecto. Revisa los ejemplos prácticos del módulo.',
}


class Command(BaseCommand):
    help = 'Pobla todos los cursos con contenido completo: lecciones, exámenes y desafíos'

    def handle(self, *args, **options):
        self._seed_courses()
        self._seed_exams()
        self._seed_challenges()
        self.stdout.write(self.style.SUCCESS('\n¡Contenido completado exitosamente!'))

    def _seed_courses(self):
        for data in COURSES_DATA:
            course_id = data.pop('id')
            lessons = data.pop('lessons')
            course, created = Course.objects.update_or_create(id=course_id, defaults=data)
            self.stdout.write(f'  Curso: {course.title} {"(creado)" if created else "(actualizado)"}')

            prefix = LEVEL_PREFIXES.get(course.level, '[BASICO] ')
            CourseContent.objects.filter(course=course).delete()
            for les in lessons:
                les['title'] = prefix + les['title']
                les['section_type'] = SECTION_TYPE_MAP.get(les['section_type'], les['section_type'])
                CourseContent.objects.create(course=course, **les)
            self.stdout.write(f'    → {len(lessons)} lecciones creadas')

    def _seed_exams(self):
        for data in EXAMS_DATA:
            course = Course.objects.get(id=data['course_id'])
            questions_data = data.pop('questions')
            Exam.objects.filter(course=course).delete()
            exam = Exam.objects.create(course=course, **data)
            self.stdout.write(f'  Examen: {exam.title}')

            for qdata in questions_data:
                opts = qdata.pop('options')
                q = Question.objects.create(exam=exam, **qdata)
                for odata in opts:
                    QuestionOption.objects.create(question=q, **odata)
            self.stdout.write(f'    → {len(questions_data)} preguntas creadas')

    def _seed_challenges(self):
        InteractiveChallenge.objects.all().delete()
        for idx, data in enumerate(CHALLENGES_DATA):
            course = Course.objects.get(id=data['course_id'])
            contents = list(CourseContent.objects.filter(course=course).order_by('order'))
            if not contents:
                self.stdout.write(self.style.WARNING(f'  Sin contenidos para curso {course.title}, saltando desafíos'))
                continue
            content = contents[idx % len(contents)]
            feedback = FEEDBACK_MAP.get(data['correct_index'], '')
            InteractiveChallenge.objects.create(
                content=content,
                prompt=data['prompt'],
                code_snippet=data['code_snippet'],
                choices_json=json.dumps(data['choices']),
                correct_index=data['correct_index'],
                feedback=feedback,
            )
        self.stdout.write(f'  {len(CHALLENGES_DATA)} desafíos interactivos creados')
