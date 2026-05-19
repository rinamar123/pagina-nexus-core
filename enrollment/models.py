from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    LEVEL_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio',   'Intermedio'),
        ('avanzado',     'Avanzado'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='🤖')
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    duration = models.CharField(max_length=100, default='16 semanas')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='principiante')
    instructor_name = models.CharField(max_length=150, default='Instructor')
    instructor_bio = models.TextField(blank=True, default='')
    instructor_avatar_url = models.CharField(max_length=500, blank=True, default='')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Student(models.Model):
    LEVEL_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio',   'Intermedio'),
        ('avanzado',     'Avanzado'),
    ]
    STATUS_CHOICES = [
        ('pending',  'Pendiente'),
        ('accepted', 'Aceptado'),
        ('rejected', 'Rechazado'),
        ('suspended', 'Suspendido'),
    ]

    user       = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='student')
    generated_password = models.CharField(max_length=50, blank=True, null=True)
    name       = models.CharField(max_length=150)
    email      = models.EmailField(unique=True)
    phone      = models.CharField(max_length=20, blank=True, null=True)
    address    = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='default.png')
    level      = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    courses    = models.ManyToManyField(Course, blank=True, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def unread_notifications(self):
        return self.notifications.filter(is_read=False)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"


class CourseContent(models.Model):
    SECTION_TYPES = [
        ('explicacion', 'Explicación'),
        ('ejemplo', 'Ejemplo'),
        ('demo', 'Demo'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='course_demos/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['course', 'order']

    def __str__(self):
        return f"{self.get_section_type_display()}: {self.title}"

    @property
    def simple_task_description(self):
        title_lower = self.title.lower()
        
        # 1. Curso: IA y Machine Learning Academy
        if "historia de la ia" in title_lower:
            return """<strong>Desafío de Análisis Histórico:</strong><br>
            Escribe un breve ensayo de 1 página en formato PDF o una captura de pantalla de tus apuntes comparando el enfoque de la IA Simbólica (Sistemas Expertos) frente al enfoque Subsimbólico (Conexión/Redes Neuronales). Resalta cuál consideras que ha tenido mayor impacto en la industria moderna y por qué."""
            
        elif "test de turing" in title_lower:
            return """<strong>Evaluación del Test de Turing:</strong><br>
            Diseña un diálogo de 5 interacciones entre un humano y un chatbot de IA donde intentes poner a prueba el Test de Turing. Identifica qué preguntas clave harías para desenmascarar a la máquina y explica en un archivo PDF o captura de pantalla tu estrategia."""
            
        elif "clasificación base" in title_lower:
            return """<strong>Esquema de Clasificación Base:</strong><br>
            Dibuja un diagrama de flujo o mapa mental (toma una foto o súbelo en PDF) que represente el pipeline típico de un problema de Clasificación en Machine Learning, desde la recopilación de datos hasta la evaluación de la exactitud."""
            
        elif "sistemas expertos" in title_lower:
            return """<strong>Diseño de Reglas de Producción:</strong><br>
            Crea un pseudocódigo o listado de 5 reglas condicionales (If-Then) que modelen un Sistema Experto para predecir si un cliente es apto para un crédito financiero. Sube el código en un archivo de texto (.txt) o captura de pantalla."""
            
        elif "lógica difusa" in title_lower:
            return """<strong>Aplicación de Lógica Difusa:</strong><br>
            Diseña las funciones de pertenencia cualitativa (Frío, Templado, Caliente) para el termostato de un aire acondicionado usando Lógica Difusa. Sube un gráfico dibujado a mano (foto) o un escrito explicando las variables."""
            
        elif "perceptrón simple" in title_lower:
            return """<strong>Cálculo del Perceptrón:</strong><br>
            Dado un perceptrón con entradas X1 = 0.5, X2 = 0.8, pesos W1 = -0.4, W2 = 0.6 y un sesgo (bias) b = -0.1, calcula la salida usando la función de activación de paso (Heaviside). Sube el desarrollo matemático en una foto o PDF."""
            
        elif "compuertas lógicas" in title_lower:
            return """<strong>Compuerta XOR con Perceptrón:</strong><br>
            Explica detalladamente por qué un Perceptrón Simple no puede resolver el problema de clasificación no lineal de la compuerta XOR. Sube un documento corto en PDF o una foto de tu cuaderno con la demostración gráfica."""
            
        elif "tu primera neurona" in title_lower:
            return """<strong>Implementación de Neurona Artificial:</strong><br>
            Escribe una función simple en Python (`neurona_artificial(inputs, weights, bias)`) que calcule la suma ponderada y aplique la función Sigmoide. Sube tu script en archivo `.py` o captura del código funcionando."""
            
        elif "redes multicapa" in title_lower:
            return """<strong>Arquitectura de Redes Multicapa (MLP):</strong><br>
            Dibuja un esquema completo de una Red Neuronal con 3 entradas, 1 capa oculta de 4 neuronas y 2 salidas. Etiqueta cada capa y súbelo en una foto o archivo de imagen."""
            
        elif "funciones activación" in title_lower:
            return """<strong>Comparativa de Funciones de Activación:</strong><br>
            Escribe un cuadro comparativo entre las funciones ReLU, Sigmoide y Tangente Hiperbólica (Tanh) indicando sus rangos de salida y ventajas. Sube el cuadro en PDF o imagen de captura."""
            
        elif "backpropagation" in title_lower:
            return """<strong>Análisis del Flujo de Backpropagation:</strong><br>
            Describe en tus propias palabras el algoritmo de Retropropagación y cómo se calcula el gradiente del error respecto a los pesos usando la Regla de la Cadena. Sube un PDF o captura de pantalla de tu escrito."""
            
        elif "gradient descent" in title_lower:
            return """<strong>Optimización por Descenso de Gradiente:</strong><br>
            Escribe una explicación corta del rol de la Tasa de Aprendizaje (Learning Rate) y cómo una tasa muy alta o muy baja puede afectar la convergencia. Sube un archivo .txt, .py con pseudocódigo o captura."""
            
        elif "deep learning" in title_lower:
            return """<strong>Propuesta de Arquitectura Deep Learning:</strong><br>
            Propón qué tipo de red neuronal profunda (por ejemplo, CNN para imágenes o RNN/LSTM para texto) usarías para clasificar correos como Spam o No Spam. Sube tu justificación en PDF."""
            
        elif "procesamiento texto" in title_lower:
            return """<strong>Tokenización de Texto:</strong><br>
            Escribe un script en Python o un algoritmo conceptual que tome un párrafo de texto, lo convierta a minúsculas, elimine signos de puntuación y retorne una lista de palabras únicas (tokens). Sube el archivo `.py` o una captura."""

        # 2. Curso: Regresión Lineal Predictiva
        elif "estadística predictiva" in title_lower:
            return """<strong>Análisis de Varianza y Desviación:</strong><br>
            Calcula la media y la desviación estándar de un conjunto de datos simple: [10, 12, 15, 18, 20]. Sube el desarrollo matemático en una foto o PDF."""
            
        elif "covarianza" in title_lower:
            return """<strong>Interpretación de la Covarianza:</strong><br>
            Explica en un párrafo qué significa una covarianza positiva, negativa y cercana a cero entre dos variables financieras. Sube tu respuesta en un archivo .txt, PDF o captura de pantalla."""
            
        elif "regresión simple" in title_lower:
            return """<strong>Fórmula del Modelo Lineal:</strong><br>
            Dada la ecuación de regresión Y = 3.5 * X + 150, predice el valor de Y cuando X es igual a 20. Explica detalladamente qué representa el valor 150 (intercepto). Sube un PDF o captura del cálculo."""
            
        elif "minimos cuadrados" in title_lower:
            return """<strong>Método de Mínimos Cuadrados Ordinarios (OLS):</strong><br>
            Describe detalladamente cómo el método de mínimos cuadrados minimiza la suma de los residuos al cuadrado. Sube un breve ensayo o explicación matemática en PDF o foto."""
            
        elif "predicción salarial" in title_lower:
            return """<strong>Modelado de Predicción Salarial:</strong><br>
            Plantea una hipótesis sobre cómo influyen los Años de Experiencia y el Nivel Educativo en el salario estimado de un profesional del sector tecnológico. Sube tu hipótesis estructurada en PDF o captura."""
            
        elif "métricas de error" in title_lower:
            return """<strong>Cálculo de MAE y MSE:</strong><br>
            Dado un conjunto de valores reales [100, 150, 200] y sus predicciones correspondientes [105, 148, 210], calcula manualmente el error absoluto medio (MAE) y el error cuadrático medio (MSE). Sube el desarrollo en foto o PDF."""
            
        elif "análisis residual" in title_lower:
            return """<strong>Gráfico de Residuos:</strong><br>
            Explica qué es la Homocedasticidad y por qué es crucial analizar los gráficos de residuos para validar los supuestos de la regresión lineal. Sube un documento detallado en PDF o captura."""
            
        elif "regresión múltiple" in title_lower:
            return """<strong>Ecuación de Regresión Múltiple:</strong><br>
            Escribe la ecuación matemática para un modelo de regresión lineal múltiple con 3 variables independientes (X1, X2, X3). Sube tu ecuación y definición de términos en un archivo .txt o PDF."""
            
        elif "variables dummy" in title_lower:
            return """<strong>Codificación One-Hot / Dummy:</strong><br>
            Dada una variable categórica 'Ciudad' con los valores ['Cali', 'Bogotá', 'Medellín'], muestra cómo se transformarían en variables numéricas Dummy. Sube la tabla resultante en una captura o PDF."""
            
        elif "mercado inmobiliario" in title_lower:
            return """<strong>Factores Inmobiliarios:</strong><br>
            Haz una lista de 4 variables críticas que consideras deberían incluirse en un modelo predictivo para estimar el precio de venta de un apartamento en tu ciudad. Sube tu lista justificada en PDF o foto."""
            
        elif "regresión logística" in title_lower:
            return """<strong>Función Sigmoide en Logística:</strong><br>
            Explica por qué la regresión logística utiliza la función sigmoide en lugar de una línea recta para predecir probabilidades binarias. Sube un PDF o captura de pantalla de tu escrito."""
            
        elif "matriz confusión" in title_lower:
            return """<strong>Cálculo de Precision y Recall:</strong><br>
            Dada una matriz de confusión con Verdaderos Positivos = 40, Falsos Positivos = 10, Verdaderos Negativos = 80, Falsos Negativos = 5, calcula la Precisión y la Sensibilidad (Recall). Sube el desarrollo en foto o PDF."""
            
        elif "multicolinealidad" in title_lower:
            return """<strong>Detección de Multicolinealidad (VIF):</strong><br>
            Explica brevemente qué es el Factor de Inflación de la Varianza (VIF) y cómo afecta la estabilidad de los coeficientes de regresión. Sube tu explicación en archivo de texto o PDF."""
            
        elif "regularización" in title_lower:
            return """<strong>Lasso vs Ridge Regression:</strong><br>
            Establece la diferencia principal en la forma en que Lasso (L1) y Ridge (L2) regularizan y penalizan los coeficientes de un modelo lineal. Sube un cuadro comparativo en PDF o captura."""

        # 3. Curso: Algoritmos Genéticos
        elif "darwinismo digital" in title_lower:
            return """<strong>Analogía Evolutiva:</strong><br>
            Explica brevemente la analogía entre la selección natural de Charles Darwin (Supervivencia del más apto) y la optimización en Algoritmos Genéticos. Sube tu escrito en PDF o una foto de tus apuntes."""
            
        elif "cromosomas y genes" in title_lower:
            return """<strong>Representación Cromosómica:</strong><br>
            Diseña un esquema de representación binaria para codificar un número entero del 0 al 31 como un cromosoma. Sube la representación del número 19 en binario en un archivo de texto o foto."""
            
        elif "población inicial" in title_lower:
            return """<strong>Estrategias de Población Inicial:</strong><br>
            Explica la importancia del tamaño de la población inicial en un algoritmo genético y por qué una población extremadamente pequeña puede llevar a una convergencia prematura. Sube tu análisis en PDF."""
            
        elif "función fitness" in title_lower:
            return """<strong>Diseño de Función de Aptitud:</strong><br>
            Define conceptualmente una función fitness para optimizar el diseño de una mochila de viaje, maximizando el valor de los objetos y respetando un límite estricto de peso. Sube la fórmula o lógica matemática en PDF o foto."""
            
        elif "paisaje fitness" in title_lower:
            return """<strong>Optimización en Paisajes Fitness:</strong><br>
            Explica en tus propias palabras qué es un máximo local y cómo un algoritmo genético puede evitar quedar atrapado en él a diferencia de los métodos de gradiente clásicos. Sube un escrito en PDF o captura."""
            
        elif "operador de selección" in title_lower:
            return """<strong>Selección por Ruleta:</strong><br>
            Dada una población de 4 individuos con valores de fitness [10, 20, 30, 40], calcula la probabilidad de selección por Ruleta (Proporcional) para cada uno de ellos. Sube tus cálculos en foto o PDF."""
            
        elif "cruce (crossover)" in title_lower:
            return """<strong>Simulación de Cruce de un Punto:</strong><br>
            Dados dos cromosomas padres P1 = [1,1,0,0,1,1] y P2 = [0,0,1,1,0,0], realiza un cruce de un solo punto en la tercera posición. Sube los cromosomas hijos resultantes en un archivo .txt o foto."""
            
        elif "mutación" in title_lower:
            return """<strong>Efecto de la Tasa de Mutación:</strong><br>
            Discute el rol de la tasa de mutación en la exploración del espacio de búsqueda de un algoritmo genético. ¿Qué ocurre si la tasa de mutación es del 100%? Sube tu respuesta en PDF o captura de pantalla."""
            
        elif "elitismo" in title_lower:
            return """<strong>Elitismo vs Selección Estándar:</strong><br>
            Define el concept de Elitismo y explica por qué asegura que el fitness máximo de la población nunca disminuya de una generación a otra. Sube tu escrito en PDF o foto."""
            
        elif "problema del viajero" in title_lower:
            return """<strong>Modelado del TSP (Traveling Salesperson):</strong><br>
            Dibuja una red de 4 ciudades (A, B, C, D) con distancias arbitrarias y muestra cómo codificarías una ruta válida (cromosoma de permutación). Sube el dibujo en una foto o imagen de captura."""
            
        elif "cruce de orden (ox)" in title_lower:
            return """<strong>Operador de Cruce de Orden (OX):</strong><br>
            Explica brevemente por qué los operadores de cruce estándar (como el cruce de un punto) generan cromosomas inválidos para el TSP y cómo lo soluciona el Cruce de Orden (OX). Sube tu explicación en PDF."""
            
        elif "inteligencia de enjambre" in title_lower:
            return """<strong>Inteligencia de Enjambre (Swarm Intelligence):</strong><br>
            Menciona dos ejemplos de la naturaleza que utilicen inteligencia de enjambre (como hormigas o aves) y cómo se aplican a la optimización en ingeniería. Sube un archivo .txt, PDF o captura."""

        elif "pso en acción" in title_lower:
            return """<strong>Ecuaciones de PSO (Optimización por Enjambre de Partículas):</strong><br>
            Escribe las dos ecuaciones fundamentales de PSO (actualización de velocidad y actualización de posición). Explica qué representa el componente social y el componente cognitivo. Sube la respuesta en PDF o foto."""

        # 4. Caso General (Fallback)
        return """<strong>Desafío de Asimilación de la Lección:</strong><br>
        Realiza un resumen analítico de 3 puntos clave explicados en esta lección y propone una aplicación práctica de estos conceptos en un escenario de negocio real. Sube tu propuesta estructurada en PDF o en una foto de tus notas escritas."""


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    passing_score = models.PositiveIntegerField(default=70)
    time_limit_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['course', '-created_at']

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField(verbose_name='Pregunta')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['exam', 'order']

    def __str__(self):
        return self.text[:60]


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255, verbose_name='Opción')
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['question', 'order']

    def __str__(self):
        return self.text[:40]


class ExamAttempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='attempts')
    score = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
    passed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-started_at']

    def __str__(self):
        return f"{self.student.name} - {self.exam.title} ({self.score}/{self.total})"


class EnrollmentRequest(models.Model):
    STATUS_CHOICES = [
        ('pending',  'Pendiente'),
        ('accepted', 'Aceptado'),
        ('rejected', 'Rechazado'),
    ]
    student  = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment_requests')
    course   = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment_requests')
    status   = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['student', 'course']

    def __str__(self):
        return f"{self.student.name} → {self.course.title} ({self.get_status_display()})"


class CourseFile(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='files')
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='course_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title


class InteractiveChallenge(models.Model):
    content = models.ForeignKey(CourseContent, on_delete=models.CASCADE, related_name='challenges')
    prompt = models.TextField()
    code_snippet = models.TextField(blank=True, null=True)
    choices_json = models.TextField(help_text="Lista en formato JSON (ej: [\"opcion1\", \"opcion2\"])")
    correct_index = models.PositiveIntegerField(help_text="Índice base 0 de la respuesta correcta")
    feedback = models.TextField(help_text="Retroalimentación al responder mal")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Challenge para {self.content.title}: {self.prompt[:30]}"


class ChallengeAttempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='challenge_attempts')
    challenge = models.ForeignKey(InteractiveChallenge, on_delete=models.CASCADE, related_name='attempts')
    is_correct = models.BooleanField(default=False)
    attempted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'challenge')

    def __str__(self):
        return f"{self.student.name} - {self.challenge.id} - {'Correcto' if self.is_correct else 'Incorrecto'}"

