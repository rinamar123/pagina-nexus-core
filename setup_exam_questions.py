import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from enrollment.models import Exam, Question, QuestionOption

def run():
    # Limpiar preguntas existentes
    Question.objects.all().delete()
    
    exams_data = [
        {
            'title': 'Examen Final IA',
            'questions': [
                ('¿Qué es el Test de Turing?', ['Una prueba de potencia de hardware', 'Un método para determinar si una máquina exhibe comportamiento inteligente', 'Un algoritmo de compresión', 'Un tipo de base de datos'], 1),
                ('¿Cuál es la función principal de una función de activación?', ['Ahorrar memoria', 'Introducir no linealidad en la red', 'Conectar el teclado', 'Imprimir resultados'], 1),
                ('¿Qué significa NLP?', ['Neural Level Processing', 'Natural Language Processing', 'Network Logic Protocol', 'New Laser Printer'], 1),
                ('¿Qué es el aprendizaje supervisado?', ['Aprender sin datos', 'Aprender con datos etiquetados', 'Aprender solo de errores', 'Aprender de forma aleatoria'], 1),
                ('¿Qué es una neurona artificial?', ['Un cable de cobre', 'Una función matemática que procesa entradas para generar una salida', 'Un chip de silicio líquido', 'Un sensor de luz'], 1),
                ('¿Para qué sirve el Backpropagation?', ['Para apagar el modelo', 'Para ajustar los pesos minimizando el error', 'Para borrar la base de datos', 'Para aumentar la velocidad del ventilador'], 1),
                ('¿Qué es un Dataset?', ['Una computadora vieja', 'Una colección estructurada de datos', 'Un juego de cables', 'Un manual de usuario'], 1),
                ('¿Qué es el Overfitting?', ['Cuando el modelo es muy rápido', 'Cuando el modelo se memoriza los datos y no generaliza', 'Cuando el modelo no tiene datos', 'Cuando el modelo es muy grande'], 1),
                ('¿Qué es la visión artificial?', ['Lentes para computadoras', 'Capacidad de las máquinas para extraer información de imágenes', 'Un tipo de monitor neón', 'Una cámara web básica'], 1),
                ('¿Quién es considerado el padre de la IA?', ['Steve Jobs', 'Alan Turing', 'Bill Gates', 'Elon Musk'], 1),
            ]
        },
        {
            'title': 'Examen Final Regresión',
            'questions': [
                ('En y = mx + b, ¿qué representa "m"?', ['El error', 'La pendiente de la recta', 'El punto de corte', 'La variable dependiente'], 1),
                ('¿Qué busca minimizar la Regresión Lineal?', ['La velocidad', 'La suma de los errores al cuadrado', 'El número de variables', 'El uso de CPU'], 1),
                ('¿Qué indica un R-Cuadrado de 0.95?', ['Que el modelo es muy malo', 'Que el modelo explica el 95% de la variabilidad', 'Que el modelo tiene 95 errores', 'Que el modelo es lento'], 1),
                ('¿Qué es la Regresión Múltiple?', ['Hacer muchas regresiones simples', 'Predecir una variable usando varias independientes', 'Un error de sistema', 'Un tipo de suma'], 1),
                ('¿Para qué sirve la Regresión Logística?', ['Para predecir números infinitos', 'Para clasificación binaria (Sí/No)', 'Para dibujar círculos', 'Para medir distancias'], 1),
                ('¿Qué es el P-Value?', ['El precio de la variable', 'Un indicador de significancia estadística', 'Un punto de la recta', 'La posición inicial'], 1),
                ('¿Qué hace la regularización Lasso?', ['Borra todo el modelo', 'Penaliza coeficientes pudiendo llevarlos a cero', 'Aumenta el error', 'Dibuja una línea curva'], 1),
                ('¿Qué es un outlier?', ['Un dato muy bueno', 'Un valor atípico que se aleja mucho del resto', 'El título del gráfico', 'La variable X'], 1),
                ('¿Qué es la correlación?', ['Una suma de datos', 'La relación entre dos variables', 'Una división por cero', 'Un tipo de color'], 1),
                ('¿Qué es el MSE?', ['Mean Squared Error', 'Main System Engine', 'Multiple Star Effect', 'Manual Set Entry'], 0),
            ]
        },
        {
            'title': 'Examen Final Genético',
            'questions': [
                ('¿En qué se inspiran los Algoritmos Genéticos?', ['En la física cuántica', 'En la selección natural y evolución', 'En el tráfico vehicular', 'En la bolsa de valores'], 1),
                ('¿Qué es el Crossover?', ['Cruzar la calle', 'Intercambio de información genética entre padres', 'Borrar un gen', 'Reiniciar la población'], 1),
                ('¿Qué es la Mutación?', ['Un error fatal', 'Un cambio aleatorio en un gen para mantener diversidad', 'Un tipo de virus', 'El final del algoritmo'], 1),
                ('¿Qué mide la función Fitness?', ['La velocidad del PC', 'Qué tan apto es un individuo para resolver el problema', 'El tamaño del archivo', 'La cantidad de genes'], 1),
                ('¿Qué es un Individuo en AG?', ['Una persona real', 'Una solución potencial al problema', 'Un error de código', 'Un bit de memoria'], 1),
                ('¿Qué es una Población?', ['Un grupo de computadoras', 'Un conjunto de individuos/soluciones', 'La base de datos', 'El sistema operativo'], 1),
                ('¿Para qué sirve el Elitismo?', ['Para ser presumido', 'Para asegurar que los mejores pasen a la siguiente generación', 'Para borrar a los peores', 'Para cambiar el nombre'], 1),
                ('¿Qué es la convergencia?', ['Cuando el algoritmo falla', 'Cuando la población se vuelve muy similar al encontrar el óptimo', 'Cuando el PC se calienta', 'Cuando hay muchos genes'], 1),
                ('¿Qué es el Problema del Viajero (TSP)?', ['Un turista perdido', 'Un reto clásico de optimización de rutas', 'Un error de GPS', 'Un juego de mapas'], 1),
                ('¿Qué es un Gen en AG?', ['Una parte del código', 'La unidad mínima de información de un individuo', 'Una variable global', 'Una constante'], 1),
            ]
        }
    ]

    for e_data in exams_data:
        try:
            exam = Exam.objects.get(title__icontains=e_data['title'])
            for q_text, options, correct_idx in e_data['questions']:
                q = Question.objects.create(exam=exam, text=q_text)
                for i, opt_text in enumerate(options):
                    QuestionOption.objects.create(
                        question=q,
                        text=opt_text,
                        is_correct=(i == correct_idx)
                    )
            print(f"Examen '{exam.title}' cargado con 10 preguntas.")
        except Exam.DoesNotExist:
            print(f"No se encontró el examen: {e_data['title']}")

if __name__ == "__main__":
    run()
