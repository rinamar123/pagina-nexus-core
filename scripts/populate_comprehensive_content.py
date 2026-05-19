import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from enrollment.models import Course, CourseContent
from django.conf import settings

def create_dummy_csv(filename, content):
    media_path = os.path.join(settings.MEDIA_ROOT, 'course_demos')
    os.makedirs(media_path, exist_ok=True)
    file_path = os.path.join(media_path, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

def get_real_code_snippet(topic):
    t = topic.lower()
    
    if "regresión" in t or "múltiple" in t or "salari" in t or "inmobiliario" in t:
        return f"""# Análisis Predictivo: {topic}
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Cargar datos
df = pd.read_csv('dataset.csv')
X = df[['variable_independiente']]
y = df['variable_dependiente']

# 2. Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. Predecir y evaluar
predicciones = modelo.predict(X_test)
mse = mean_squared_error(y_test, predicciones)
print(f"Error Cuadrático Medio: {{mse}}")
print(f"Coeficiente (m): {{modelo.coef_[0]}}, Intercepto (b): {{modelo.intercept_}}")"""

    elif "neur" in t or "perceptrón" in t or "deep" in t or "multicapa" in t:
        return f"""# Arquitectura de Redes Neuronales: {topic}
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Definir la arquitectura de la red
modelo = Sequential([
    Dense(16, activation='relu', input_shape=(8,)), # Capa de entrada y oculta
    Dense(8, activation='relu'),                    # Capa oculta adicional
    Dense(1, activation='sigmoid')                  # Capa de salida (clasificación binaria)
])

# 2. Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 3. Entrenar la red
# Asumiendo que X_train y y_train están definidos
# modelo.fit(X_train, y_train, epochs=50, batch_size=10, validation_split=0.2)

# 4. Resumen de la red
modelo.summary()"""

    elif "genétic" in t or "cruce" in t or "mutación" in t or "población" in t or "fitness" in t or "darwin" in t or "elitismo" in t:
        return f"""# Algoritmos Evolutivos: {topic}
import random

def generar_individuo(longitud):
    return [random.randint(0, 1) for _ in range(longitud)]

def calcular_fitness(individuo):
    # El fitness será la suma de los genes (maximizar los 1s)
    return sum(individuo)

def mutar(individuo, tasa_mutacion=0.05):
    for i in range(len(individuo)):
        if random.random() < tasa_mutacion:
            individuo[i] = 1 - individuo[i] # Voltear bit
    return individuo

def cruzar(padre1, padre2):
    punto_cruce = len(padre1) // 2
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Simulación de una generación
poblacion = [generar_individuo(10) for _ in range(50)]
mejores = sorted(poblacion, key=calcular_fitness, reverse=True)[:10]
print("Mejor fitness de la generación:", calcular_fitness(mejores[0]))"""

    elif "texto" in t or "nlp" in t or "logístic" in t:
        return f"""# Procesamiento de Lenguaje y Clasificación: {topic}
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

textos = [
    "Oferta exclusiva, gana dinero rápido",
    "Hola, ¿nos vemos mañana para estudiar?",
    "Felicidades, has ganado un premio",
    "El reporte de métricas está listo"
]
etiquetas = [1, 0, 1, 0] # 1: Spam, 0: Normal

# Vectorización de texto (TF-IDF)
vectorizador = TfidfVectorizer()
X = vectorizador.fit_transform(textos)

# Entrenamiento de Clasificador Logístico
clf = LogisticRegression()
clf.fit(X, etiquetas)

# Predicción de un texto nuevo
nuevo_texto = ["Gana dinero desde casa hoy mismo"]
X_nuevo = vectorizador.transform(nuevo_texto)
prediccion = clf.predict(X_nuevo)
print("Predicción (1=Spam, 0=Normal):", prediccion[0])"""

    elif "estadístic" in t or "covarianza" in t or "error" in t or "residual" in t:
        return f"""# Análisis Estadístico y Métricas: {topic}
import numpy as np
import pandas as pd

# Datos de muestra
horas_estudio = np.array([2, 3, 5, 7, 9])
notas_examen = np.array([50, 60, 80, 85, 95])

# Cálculo de Varianza y Covarianza
var_x = np.var(horas_estudio, ddof=1)
cov_xy = np.cov(horas_estudio, notas_examen)[0][1]

# Cálculo de pendiente (m) para regresión
m = cov_xy / var_x
b = np.mean(notas_examen) - m * np.mean(horas_estudio)

print(f"La ecuación de la recta es: Y = {{m:.2f}}X + {{b:.2f}}")

# Predicción
nueva_nota = m * 6 + b
print(f"Si estudias 6 horas, tu nota estimada será: {{nueva_nota:.2f}}")"""

    else:
        # Fallback genérico pero completo
        return f"""# Análisis de Datos Generales: {topic}
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carga y exploración de datos
try:
    df = pd.read_csv('dataset_analisis.csv')
    print("Primeras filas del dataset:")
    print(df.head())
    
    # 2. Limpieza básica
    df = df.dropna() # Eliminar valores nulos
    
    # 3. Análisis descriptivo
    print("\\nEstadísticas principales:")
    print(df.describe())
    
    # 4. Visualización de correlaciones
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    plt.show()
    
except FileNotFoundError:
    print("Asegúrate de haber descargado el archivo CSV adjunto en esta lección.")"""


def generate_platzi_html(title, explanation, code_example, key_takeaways):
    return f"""
    <h3>Introducción a {title}</h3>
    <p style="font-size: 1.1rem; color: #d1d5db;">En esta clase, profundizaremos en <strong>{title}</strong>. Comprender este concepto es fundamental para avanzar en tu carrera profesional como Data Scientist o Ingeniero de Machine Learning. Presta mucha atención a la teoría y asegúrate de replicar los ejemplos en tu entorno local.</p>
    
    <h4 style="color: var(--neon-blue); margin-top: 2rem;">¿Qué es y por qué importa?</h4>
    <p>{explanation}</p>
    <p>En la industria tecnológica actual, dominar estas herramientas marca la diferencia entre un desarrollador tradicional y un experto en inteligencia artificial. Empresas top a nivel mundial utilizan estas mismas lógicas para resolver problemas a gran escala.</p>
    
    <h4 style="color: var(--neon-blue); margin-top: 2rem;">Implementación Real (Código Python)</h4>
    <p>A continuación, analizaremos cómo se implementa este concepto de forma práctica en un entorno real de producción. Copia este código, estúdialo y ejecútalo paso a paso:</p>
    <pre style="background: #0d1117; padding: 1.5rem; border-radius: 1rem; border: 1px solid #30363d; overflow-x: auto; margin-top: 1rem; margin-bottom: 2rem;"><code style="color: #58d68d; font-family: monospace; font-size: 0.95rem; line-height: 1.5;">{code_example}</code></pre>
    
    <h4 style="color: var(--neon-blue); margin-top: 2rem;">Puntos Clave (Takeaways)</h4>
    <ul style="line-height: 2;">
        {key_takeaways}
    </ul>
    
    <hr style="border: 0; border-top: 1px dashed rgba(255,255,255,0.2); margin: 3rem 0;">
    <p style="text-align: center; font-style: italic; color: #8b949e;">"Nunca pares de aprender. Implementa, equivócate y mejora tu código iterativamente."</p>
    """

def run():
    CourseContent.objects.all().delete()
    
    # 1. Crear CSVs de prueba reales
    csv_ia = create_dummy_csv('dataset_ia_basico.csv', "id,feature1,feature2,label\n1,0.5,0.2,A\n2,0.9,0.8,B")
    csv_reg = create_dummy_csv('dataset_casas_precios.csv', "metros,cuartos,precio\n120,3,150000\n85,2,90000")
    csv_gen = create_dummy_csv('ciudades_coordenadas.csv', "ciudad,x,y\nA,10,20\nB,15,35\nC,5,5")

    # Temas generales por curso
    topics = {
        'IA Academy': {
            'BASICO': ['Historia de la IA', 'Test de Turing', 'Clasificación Base', 'Sistemas Expertos', 'Lógica Difusa', 'Taller Lógico'],
            'INTERMEDIO': ['Perceptrón Simple', 'Compuertas Lógicas', 'Tu Primera Neurona', 'Redes Multicapa', 'Funciones Activación', 'Taller Multicapa'],
            'AVANZADO': ['Backpropagation', 'Gradient Descent', 'Taller Optimización', 'Deep Learning', 'Procesamiento Texto', 'Proyecto Final IA']
        },
        'Regresi': {
            'BASICO': ['Estadística Predictiva', 'Covarianza', 'Taller Estadístico', 'Regresión Simple', 'Minimos Cuadrados', 'Predicción Salarial'],
            'INTERMEDIO': ['Métricas de Error', 'Análisis Residual', 'Taller Evaluación', 'Regresión Múltiple', 'Variables Dummy', 'Mercado Inmobiliario'],
            'AVANZADO': ['Regresión Logística', 'Matriz Confusión', 'Taller Logístico', 'Multicolinealidad', 'Regularización', 'Proyecto Avanzado']
        },
        'Gen': {
            'BASICO': ['Darwinismo Digital', 'Cromosomas y Genes', 'Población Inicial', 'Función Fitness', 'Paisaje Fitness', 'Taller Fitness'],
            'INTERMEDIO': ['Operador de Selección', 'Cruce (Crossover)', 'Taller Cruce', 'Mutación', 'Elitismo', 'Taller Ciclo Completo'],
            'AVANZADO': ['Problema del Viajero', 'Cruce de Orden (OX)', 'Taller Rutas', 'Inteligencia de Enjambre', 'PSO en Acción', 'Proyecto Bio-IA']
        }
    }

    csv_map = {'IA Academy': csv_ia, 'Regresi': csv_reg, 'Gen': csv_gen}
    courses = Course.objects.all()
    
    for course in courses:
        course_key = None
        for key in topics.keys():
            match_key = key.lower() if key != 'IA Academy' else 'ia'
            if match_key in course.title.lower():
                course_key = key
                break
        
        if not course_key:
            continue

        order = 1
        for level in ['BASICO', 'INTERMEDIO', 'AVANZADO']:
            lessons = topics[course_key][level]
            for i, topic in enumerate(lessons):
                is_taller = 'Taller' in topic or 'Proyecto' in topic
                s_type = 'demo' if is_taller else 'explicacion'
                
                exp_text = f"El concepto de {topic} representa uno de los pilares más fundamentales que discutimos en esta ruta de aprendizaje. Su aplicación te permite transformar datos crudos en decisiones inteligentes. Matemáticamente y conceptualmente, sirve como puente entre la estadística tradicional y el machine learning moderno."
                
                code_text = get_real_code_snippet(topic)
                
                takeaways = f"<li><b>Concepto Principal:</b> {topic} es crucial para modelar datos.</li><li><b>Bibliotecas de apoyo:</b> Familiarízate con Pandas, Numpy o Scikit-Learn.</li><li><b>Siguiente paso:</b> Descarga el CSV si aplica y ejecuta este mismo código en Google Colab o Jupyter.</li>"

                html_content = generate_platzi_html(topic, exp_text, code_text, takeaways)

                c = CourseContent(
                    course=course,
                    title=f'[{level}] {topic}',
                    content=html_content,
                    order=order,
                    section_type=s_type
                )
                
                if is_taller:
                    with open(csv_map[course_key], 'rb') as f:
                        c.file.save(os.path.basename(csv_map[course_key]), File(f), save=False)
                
                c.save()
                order += 1
                
        print(f"Curso '{course.title}' actualizado con clases extensas, CSVs y CÓDIGO REAL.")

if __name__ == "__main__":
    run()
