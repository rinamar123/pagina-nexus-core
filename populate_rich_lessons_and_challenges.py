import os
import sys
import django
import json

# Setup Django environment
sys.path.append(r"c:\Users\SANDRA\Desktop\LABbb de RINA\lab1\Laboratorio_RinaMarriaga")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ai_project.settings")
django.setup()

from enrollment.models import Course, CourseContent, InteractiveChallenge

print("Starting rich lesson and challenge database population...")

# Data structures for 54 lessons
data = {
    # COURSE 4: IA Y MACHINE LEARNING ACADEMY
    4: [
        {
            "order": 1,
            "title": "[BASICO] Historia de la IA",
            "section_type": "explicacion",
            "content": """
<h3>Historia y Evolución de la Inteligencia Artificial</h3>
<p>La Inteligencia Artificial (IA) nació formalmente como disciplina académica en el verano de 1956 durante la histórica <strong>Conferencia de Dartmouth</strong>. Esta conferencia fue convocada por destacados científicos como John McCarthy, Marvin Minsky, Nathaniel Rochester y Claude Shannon. Fue allí donde <strong>John McCarthy acuñó por primera vez el término "Inteligencia Artificial"</strong>, proponiendo la hipótesis de que cualquier aspecto del aprendizaje o de la inteligencia puede ser descrito con tal precisión que se puede construir una máquina para simularlo.</p>
<p>Históricamente, la IA se ha dividido en dos grandes paradigmas en constante tensión dialéctica:</p>
<ul>
    <li><strong>IA Simbólica o Conexionista (Top-Down):</strong> Basada en la manipulación lógica de símbolos explícitos y reglas formales (como los Sistemas Expertos). Asume que la inteligencia radica en el razonamiento deductivo deductivo y representaciones formales del conocimiento.</li>
    <li><strong>IA Subsimbólica o Conexionista (Bottom-Up):</strong> Inspirada en la neurobiología y las redes neuronales artificiales. No requiere reglas explícitas, sino que aprende patrones continuos y aproximaciones funcionales a partir de datos empíricos.</li>
</ul>
<p>A pesar del entusiasmo inicial, la IA sufrió periodos de desilusión y recortes presupuestarios conocidos como los <em>Inviernos de la IA</em> (el primero tras el reporte Lighthill en 1973 y las críticas al perceptrón de Minsky; el segundo a finales de los años 80 por el colapso del mercado de las máquinas LISP). Hoy en día, gracias a la explosión del Big Data y el poder de cómputo de las GPUs, la IA conexionista (Deep Learning) domina la escena mundial.</p>
""",
            "challenge": {
                "prompt": "¿Quién acuñó formalmente el término 'Inteligencia Artificial' durante la Conferencia de Dartmouth en 1956?",
                "choices": ["A) Alan Turing", "B) John McCarthy", "C) Marvin Minsky"],
                "correct_index": 1,
                "feedback": "Incorrecto. Fue John McCarthy quien acuñó formalmente el término en la Conferencia de Dartmouth de 1956."
            }
        },
        {
            "order": 2,
            "title": "[BASICO] El Test de Turing",
            "section_type": "explicacion",
            "content": """
<h3>El Test de Turing: Criterio de Inteligencia Operacional</h3>
<p>En su influyente artículo de 1950 titulado <em>"Computing Machinery and Intelligence"</em>, el matemático británico Alan Turing planteó una pregunta revolucionaria: <em>"¿Pueden pensar las máquinas?"</em>. Para evitar debates metafísicos sobre la naturaleza de la conciencia, Turing propuso reemplazar la pregunta con un experimento operacional que llamó el <strong>Juego de la Imitación</strong>, conocido hoy universalmente como el <strong>Test de Turing</strong>.</p>
<p>El experimento involucra a tres participantes en terminales ciegas aisladas:</p>
<ol>
    <li>Un evaluador humano (interrogador).</li>
    <li>Un ser humano de control.</li>
    <li>La máquina que está siendo evaluada.</li>
</ol>
<p>El interrogador formula preguntas de texto libre a ambos terminales. Si tras un periodo de conversación el interrogador no logra distinguir con certeza estadística a la máquina del humano, se considera que la máquina posee comportamiento inteligente equivalente.</p>
<p>El filósofo <strong>John Searle propuso en 1980 el famoso argumento de la "Habitación China"</strong> para criticar este test. Searle argumenta que una persona dentro de una habitación que manipula símbolos chinos siguiendo un manual de reglas sintácticas puede convencer a un observador externo de que habla chino sin comprender una sola palabra, demostrando que <strong>la mera sintaxis computacional no equivale a comprensión semántica</strong>.</p>
""",
            "challenge": {
                "prompt": "¿Qué experimento mental diseñó John Searle para demostrar que pasar el Test de Turing mediante manipulación sintáctica no implica comprensión semántica?",
                "choices": ["A) El Demonio de Maxwell", "B) La Habitación China", "C) El Cerebro de Boltzmann"],
                "correct_index": 1,
                "feedback": "Incorrecto. Fue la Habitación China de John Searle el experimento mental que criticó al Test de Turing."
            }
        },
        {
            "order": 3,
            "title": "[BASICO] Clasificación Base",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Pipeline de Clasificación de Datos</h3>
<p>En el Machine Learning supervisado, la <strong>Clasificación</strong> consiste en predecir etiquetas de clase categóricas discretas (por ejemplo, Spam o No-Spam) para un conjunto de datos dado. El flujo estándar o <em>pipeline</em> de clasificación comprende las siguientes etapas estructurales:</p>
<ol>
    <li><strong>Adquisición y Limpieza:</strong> Recolección del conjunto de datos e imputación de valores faltantes.</li>
    <li><strong>División Estratégica:</strong> División de los datos en subconjuntos de <strong>Entrenamiento (Train)</strong> para ajustar los pesos del modelo, y de <strong>Prueba (Test)</strong> para evaluar la capacidad de generalización del modelo ante datos no vistos.</li>
    <li><strong>Extracción de Características (Feature Engineering):</strong> Transformación de los datos crudos en vectores numéricos óptimos.</li>
    <li><strong>Entrenamiento:</strong> Optimización de una función de pérdida (como la entropía cruzada) sobre el conjunto de entrenamiento.</li>
    <li><strong>Evaluación:</strong> Cálculo de métricas de desempeño cuantitativas sobre el conjunto de prueba.</li>
</ol>
<p>Es un error metodológico crítico entrenar y evaluar el modelo sobre el mismo conjunto de datos, ya que esto enmascara el <strong>sobreajuste (overfitting)</strong>, impidiendo medir el comportamiento real del modelo ante nuevas observaciones.</p>
""",
            "challenge": {
                "prompt": "¿Por qué es crucial dividir los datos en conjuntos independientes de Entrenamiento (Train) y Prueba (Test)?",
                "choices": ["A) Para acelerar la velocidad del entrenamiento en GPUs.", "B) Para evitar el sesgo por sobreajuste (overfitting) y medir la capacidad de generalización real.", "C) Para poder aplicar funciones de activación no lineales."],
                "correct_index": 1,
                "feedback": "Incorrecto. Se dividen para validar la capacidad de generalización real sobre datos nuevos y no vistos."
            }
        },
        {
            "order": 4,
            "title": "[BASICO] Sistemas Expertos",
            "section_type": "explicacion",
            "content": """
<h3>Sistemas Expertos e IA Simbólica</h3>
<p>Los <strong>Sistemas Expertos</strong> representan la cúspide de la IA simbólica basada en el conocimiento de los años 70 y 80. Son programas diseñados para emular la capacidad de toma de decisiones de un experto humano en un dominio altamente especializado.</p>
<p>La arquitectura de un Sistema Experto se compone fundamentalmente de tres pilares:</p>
<ol>
    <li><strong>Base de Conocimientos:</strong> Una base de datos estructurada que contiene las reglas heurísticas y hechos sobre el dominio, típicamente expresada en reglas lógicas condicionales del tipo <code>IF (Antecedente) THEN (Consecuente)</code>.</li>
    <li><strong>Motor de Inferencia:</strong> El cerebro lógico del sistema que procesa las reglas para derivar conclusiones. Utiliza dos estrategias de búsqueda lógica:
        <ul>
            <li><strong>Encadenamiento hacia Adelante (Forward Chaining):</strong> Inicia con los hechos conocidos y aplica las reglas para inferir nuevos hechos.</li>
            <li><strong>Encadenamiento hacia Atrás (Backward Chaining):</strong> Inicia con una hipótesis (meta) y busca reglas que la soporten, verificando sus antecedentes.</li>
        </ul>
    </li>
    <li><strong>Interfaz de Usuario y Módulo de Explicación:</strong> Permite la comunicación interactiva y detalla la traza lógica de por qué se llegó a una conclusión determinada.</li>
</ol>
""",
            "challenge": {
                "prompt": "¿Qué componente del Sistema Experto se encarga de procesar las reglas lógicas para derivar nuevas conclusiones o verificar metas?",
                "choices": ["A) La Interfaz de Usuario", "B) El Motor de Inferencia", "C) La Base de Conocimientos"],
                "correct_index": 1,
                "feedback": "Incorrecto. El Motor de Inferencia es el procesador lógico que ejecuta las deducciones."
            }
        },
        {
            "order": 5,
            "title": "[BASICO] Lógica Difusa",
            "section_type": "explicacion",
            "content": """
<h3>Lógica Difusa (Fuzzy Logic): Razonando en el Gris</h3>
<p>La lógica booleana clásica opera en un espacio binario estricto de verdad y falsedad: un elemento pertenece a un conjunto ($1$) o no pertenece ($0$). Sin embargo, el razonamiento humano es inherentemente vago. En 1965, el matemático <strong>Lotfi Zadeh introdujo la Lógica Difusa</strong> para formalizar esta ambigüedad.</p>
<p>En la Lógica Difusa, la pertenencia a un conjunto no es binaria, sino que está definida por una <strong>función de membresía $\mu_A(x)$</strong> que asigna a cada elemento un grado continuo de verdad en el intervalo real $[0, 1]$. Un elemento puede pertenecer un $0.7$ al conjunto de "Caliente" y simultáneamente un $0.3$ al conjunto de "Templado".</p>
<p>Un sistema de control difuso clásico sigue un ciclo de tres etapas:</p>
<ol>
    <li><strong>Fusificación (Fuzzification):</strong> Conversión de entradas numéricas nítidas (crisp inputs) a grados de membresía difusos usando funciones (triangulares, trapezoidales, gaussianas).</li>
    <li><strong>Inferencia Difusa:</strong> Evaluación de reglas del tipo <em>IF-THEN</em> difusas usando operadores lógicos específicos (como el mínimo para el operador AND y el máximo para el operador OR).</li>
    <li><strong>Defusificación (Defuzzification):</strong> Conversión de los conjuntos difusos resultantes en una única salida numérica física nítida (el método más común es el cálculo del <strong>Centroide</strong> o centro de gravedad).</li>
</ol>
""",
            "challenge": {
                "prompt": "¿Cuál es el método matemático más común en la Defusificación para convertir conjuntos difusos en una salida nítida física?",
                "choices": ["A) La Regla del Máximo de la Membresía", "B) El método del Centroide (Centro de Gravedad)", "C) La suma booleana de umbrales"],
                "correct_index": 1,
                "feedback": "Incorrecto. El método del Centroide es el estándar para obtener un valor físico nítido representativo de la masa difusa."
            }
        },
        {
            "order": 6,
            "title": "[BASICO] Taller Lógico",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Control Difuso de Temperatura</h3>
<p>En este módulo práctico, diseñamos un sistema de control difuso industrial para regular el motor de refrigeración de un servidor según la temperatura medida. Si la temperatura es "Alta", el motor debe acelerar drásticamente.</p>
<p>Evaluamos matemáticamente las funciones de membresía difusas definidas sobre el universo de discurso de la temperatura $[0^\circ\text{C}, 100^\circ\text{C}]$. Si medimos un valor nítido exacto de $35^\circ\text{C}$, se disparan múltiples reglas y el sistema debe integrar estas respuestas:</p>
<ul>
    <li>Regla 1: <code>IF Temp es Templada THEN Motor es Moderado</code> (Membresía calculada: $0.6$)</li>
    <li>Regla 2: <code>IF Temp es Caliente THEN Motor es Rápido</code> (Membresía calculada: $0.2$)</li>
</ul>
<p>Para fusionar estos valores de salida y generar las revoluciones por minuto del ventilador, aplicamos la defusificación del Centroide, resolviendo la integral continua del área combinada. Esto previene cambios abruptos en el motor, mitigando el desgaste físico del hardware.</p>
""",
            "challenge": {
                "prompt": "En un controlador de temperatura difuso, ¿qué beneficio físico ofrece la defusificación del centroide en comparación con la lógica booleana?",
                "choices": ["A) Aumenta el consumo de energía del ventilador.", "B) Genera salidas continuas y suaves que reducen el estrés mecánico y desgaste del motor.", "C) Elimina por completo la necesidad de medir la temperatura real."],
                "correct_index": 1,
                "feedback": "Incorrecto. La continuidad de la lógica difusa previene cambios escalonados bruscos, reduciendo el desgaste del hardware."
            }
        },
        {
            "order": 7,
            "title": "[INTERMEDIO] Perceptrón Simple",
            "section_type": "explicacion",
            "content": """
<h3>El Perceptrón Simple: Célula de la IA Conectiva</h3>
<p>Presentado por <strong>Frank Rosenblatt en 1957</strong>, el <strong>Perceptrón Simple</strong> es la forma más básica de una neurona artificial que puede tomar decisiones de clasificación binaria.</p>
<p>Matemáticamente, el perceptrón recibe un vector de entradas numéricas $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$, las multiplica por un vector de pesos sinápticos $\mathbf{w} = [w_1, w_2, \dots, w_n]^T$, añade un término de sesgo o <strong>bias ($b$)</strong>, y pasa el resultado a través de una función de activación de umbral rígido $\phi(z)$ (Heaviside o Paso Unitario):</p>
<p>$$\text{Suma ponderada: } z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b$$</p>
<p>$$\text{Salida: } y = \phi(z) = \begin{cases} 1 & \text{si } z \geq 0 \\ 0 & \text{si } z < 0 \end{cases}$$</p>
<p>El término de bias ($b$) es fundamental ya que actúa como un umbral de activación libre de entradas, permitiendo desplazar la frontera de decisión lineal fuera del origen coordinado del espacio vectorial.</p>
""",
            "challenge": {
                "prompt": "¿Cuál es el propósito matemático del término de sesgo o bias (b) en la ecuación de la neurona artificial?",
                "choices": ["A) Cancelar el valor de las entradas si estas son demasiado grandes.", "B) Desplazar la recta o hiperplano de la frontera de decisión fuera del origen coordenado.", "C) Actuar como una función de activación no lineal continuada."],
                "correct_index": 1,
                "feedback": "Incorrecto. El bias permite desplazar la frontera de decisión para clasificar conjuntos que no cruzan por el origen (0,0)."
            }
        },
        {
            "order": 8,
            "title": "[INTERMEDIO] Compuertas Lógicas",
            "section_type": "explicacion",
            "content": """
<h3>El Límite del Perceptrón Simple: Separabilidad Lineal</h3>
<p>A finales de los años 50, existía un optimismo desbordado sobre el potencial del perceptrón de Rosenblatt. Sin embargo, en 1969, los científicos <strong>Marvin Minsky y Seymour Papert publicaron el libro <em>"Perceptrons"</em></strong>, donde demostraron rigurosamente las limitaciones del modelo.</p>
<p>Minsky y Papert expusieron que el perceptrón simple es un clasificador lineal y, por lo tanto, <strong>solo puede resolver problemas que son linealmente separables</strong> (aquellos donde las clases pueden dividirse completamente con una línea recta o un hiperplano plano).</p>
<p>Demostraron que mientras el perceptrón simple puede aprender fácilmente compuertas lógicas linealmente separables como <strong>AND</strong> y <strong>OR</strong>, es <strong>matemáticamente incapaz de resolver la compuerta lógica no lineal XOR (OR Exclusivo)</strong>, ya que sus clases están distribuidas de tal forma en el espacio bidimensional que es imposible trazarse una sola línea recta que divida los 0s de los 1s.</p>
<p>Esta revelación histórica detuvo casi por completo el financiamiento de las redes neuronales por más de una década, desatando el primer gran invierno de la IA.</p>
""",
            "challenge": {
                "prompt": "¿Qué compuerta lógica demostraron Marvin Minsky y Seymour Papert en 1969 que un Perceptrón Simple es incapaz de resolver debido a la no-separabilidad lineal?",
                "choices": ["A) La compuerta lógica AND", "B) La compuerta lógica OR", "C) La compuerta lógica XOR (OR Exclusivo)"],
                "correct_index": 2,
                "feedback": "Incorrecto. La compuerta XOR requiere una frontera de decisión no lineal, por lo que un perceptrón simple falla."
            }
        },
        {
            "order": 9,
            "title": "[INTERMEDIO] Tu Primera Neurona",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Implementando una Neurona Artificial</h3>
<p>En este laboratorio práctico programamos una neurona artificial en Python puro. A diferencia de la función paso rígido del perceptrón de Rosenblatt, implementamos la <strong>función de activación Sigmoide</strong> para obtener una probabilidad de salida continua entre $0$ y $1$:</p>
<p>$$\sigma(z) = \frac{1}{1 + e^{-z}}$$</p>
<p>El código básico de nuestra neurona se estructura de la siguiente manera:</p>
<pre><code>import math

def sigmoide(z):
    return 1.0 / (1.0 + math.exp(-z))

def predecir_neurona(entradas, pesos, bias):
    # Suma ponderada
    z = sum(x * w for x, w in zip(entradas, pesos)) + bias
    return sigmoide(z)
</code></pre>
<p>Al entrenar esta neurona, ajustamos interativamente sus pesos utilizando un conjunto de datos linealmente separable, evaluando cómo converge la tasa de error a medida que el hiperplano se ajusta al contorno de las observaciones.</p>
""",
            "challenge": {
                "prompt": "¿Qué rango numérico de salida produce la función de activación Sigmoide utilizada en nuestra neurona artificial?",
                "choices": ["A) Rango continuo entre -1.0 y 1.0", "B) Rango continuo en el intervalo abierto o semiabierto (0, 1)", "C) Únicamente los valores discretos {0, 1}"],
                "correct_index": 1,
                "feedback": "Incorrecto. La función Sigmoide comprime cualquier entrada de número real a una probabilidad en el intervalo continuo entre 0 y 1."
            }
        },
        {
            "order": 10,
            "title": "[INTERMEDIO] Redes Multicapa",
            "section_type": "explicacion",
            "content": """
<h3>Redes Neuronales Multicapa (MLP)</h3>
<p>Para superar la limitación de la separabilidad lineal del perceptrón simple expuesta por Minsky, los científicos organizaron las neuronas en arquitecturas jerárquicas más complejas conocidas como <strong>Perceptrones Multicapa (MLP - Multi-Layer Perceptrons)</strong>.</p>
<p>Un MLP clásico consta de tres tipos de capas:</p>
<ol>
    <li><strong>Capa de Entrada (Input Layer):</strong> Recibe las características del conjunto de datos. No realiza cómputos neuronales.</li>
    <li><strong>Capas Ocultas (Hidden Layers):</strong> Capas intermedias que realizan transformaciones matemáticas no lineales sobre los datos. Es aquí donde la red aprende representaciones de características de alto nivel.</li>
    <li><strong>Capa de Salida (Output Layer):</strong> Produce las predicciones de clase o valores continuos finales del modelo.</li>
</ol>
<p>El poder de las capas ocultas radica en el <strong>Teorema de Aproximación Universal</strong>, el cual demuestra matemáticamente que una red neuronal prealimentada (feedforward) con una sola capa oculta y funciones de activación no lineales continuas puede aproximar cualquier función continua en espacios multidimensionales con cualquier grado de precisión deseado.</p>
""",
            "challenge": {
                "prompt": "¿Qué teorema matemático demuestra que una red neuronal prealimentada con una sola capa oculta no lineal puede aproximar cualquier función matemática continua?",
                "choices": ["A) Teorema Central del Límite", "B) Teorema de Aproximación Universal", "C) Teorema de Bayes Bayesiano"],
                "correct_index": 1,
                "feedback": "Incorrecto. El Teorema de Aproximación Universal es la base teórica que certifica el poder expresivo de las capas ocultas."
            }
        },
        {
            "order": 11,
            "title": "[INTERMEDIO] Funciones Activación",
            "section_type": "explicacion",
            "content": """
<h3>Funciones de Activación en Deep Learning</h3>
<p>Las <strong>Funciones de Activación</strong> son operadores matemáticos no lineales que se aplican a la salida de la suma ponderada de cada neurona. Sin ellas, una red neuronal de múltiples capas ocultas colapsaría en una simple combinación lineal de sus entradas, comportándose exactamente igual que una regresión lineal simple.</p>
<p>Las funciones de activación más utilizadas en la industria son:</p>
<ul>
    <li><strong>Sigmoide ($\sigma$):</strong> $\sigma(z) = 1 / (1 + e^{-z})$. Mapea salidas a $[0, 1]$. Históricamente popular, pero sufre de desvanecimiento de gradiente (vanishing gradient) en capas profundas.</li>
    <li><strong>Tangente Hiperbólica ($\tanh$):</strong> $\tanh(z) = (e^z - e^{-z}) / (e^z + e^{-z})$. Mapea salidas a $[-1, 1]$, estando centrada en cero, lo que acelera el entrenamiento.</li>
    <li><strong>Unidad Lineal Rectificada (ReLU):</strong> $f(z) = \max(0, z)$. Retorna cero para valores negativos e identidad para positivos. Es computacionalmente muy eficiente y mitiga el desvanecimiento de gradientes en el Deep Learning moderno.</li>
</ul>
""",
            "challenge": {
                "prompt": "¿Qué función de activación retorna exactamente 0 si la entrada es negativa, y la identidad (el mismo valor de entrada) si la entrada es positiva?",
                "choices": ["A) La función Sigmoide", "B) La función ReLU (Rectified Linear Unit)", "C) La función Tangente Hiperbólica (tanh)"],
                "correct_index": 1,
                "feedback": "Incorrecto. La función ReLU está definida matemáticamente como f(x) = max(0, x), anulando los valores negativos."
            }
        },
        {
            "order": 12,
            "title": "[INTERMEDIO] Taller Multicapa",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Conectando Capas Ocultas</h3>
<p>En este laboratorio conectamos programáticamente dos capas neuronales para procesar la frontera XOR. La capa de entrada cuenta con dos neuronas ($X_1, X_2$), la capa oculta posee dos neuronas con funciones de activación ReLU, y la capa de salida posee una única neurona con activación Sigmoide.</p>
<p>Al pasar los datos hacia adelante (<strong>Forward Pass</strong>):</p>
<ol>
    <li>La entrada se multiplica por la primera matriz de pesos $\mathbf{W}^{(1)}$ y se le añade el bias $\mathbf{b}^{(1)}$.</li>
    <li>Se aplica la no-linealidad ReLU para obtener la activación de la capa oculta $\mathbf{h} = \text{ReLU}(\mathbf{W}^{(1)}\mathbf{x} + \mathbf{b}^{(1)})$.</li>
    <li>El vector $\mathbf{h}$ se propaga a la capa de salida multiplicándose por los pesos $\mathbf{W}^{(2)}$, sumando el bias $b^{(2)}$, y aplicando la función Sigmoide.</li>
</ol>
<p>Este flujo permite doblar el espacio bidimensional de las entradas originales, convirtiendo un problema no separable en uno linealmente separable dentro de la capa oculta.</p>
""",
            "challenge": {
                "prompt": "Durante el Forward Pass de un MLP, ¿qué transformación matemática permite resolver la no-separabilidad lineal del problema XOR?",
                "choices": ["A) Mantener los datos sin cambios y aplicar una regresión lineal tradicional.", "B) Proyectar y doblar las entradas originales a un nuevo espacio dimensional a través de la capa oculta y su no-linealidad.", "C) Eliminar el bias de todas las neuronas del sistema."],
                "correct_index": 1,
                "feedback": "Incorrecto. La transformación no lineal de la capa oculta deforma el espacio permitiendo trazar un hiperplano separador."
            }
        },
        {
            "order": 13,
            "title": "[AVANZADO] Backpropagation",
            "section_type": "explicacion",
            "content": """
<h3>Algoritmo de Backpropagation (Retropropagación)</h3>
<p>El entrenamiento exitoso de redes neuronales profundas fue posible gracias a la popularización del algoritmo de <strong>Backpropagation</strong> en 1986 por Rumelhart, Hinton y Williams. Es un método para calcular de manera extremadamente eficiente el gradiente de la función de pérdida respecto a cada peso de la red.</p>
<p>Backpropagation se fundamenta matemáticamente en la aplicación recursiva de la <strong>Regla de la Cadena</strong> del cálculo multivariable. El proceso fluye al revés, de la capa de salida hacia la capa de entrada:</p>
<ol>
    <li>Se evalúa la pérdida (Error) en la salida de la red comparando la predicción con el valor real mediante una función de coste $E$.</li>
    <li>Se calcula la derivada parcial del error respecto a los pesos de la capa de salida.</li>
    <li>Este error se propaga hacia atrás, multiplicándose por los pesos correspondientes, calculando el gradiente local para cada neurona oculta anterior.</li>
</ol>
<p>El gradiente calculado nos indica la dirección de máxima pendiente del error. Para entrenar la red, modificamos los pesos en la dirección opuesta al gradiente para minimizar el error global.</p>
""",
            "challenge": {
                "prompt": "¿En qué pilar fundamental del cálculo multivariable se basa el algoritmo de Backpropagation para propagar gradientes de error hacia atrás?",
                "choices": ["A) El Teorema del Valor Medio", "B) La Regla de la Cadena", "C) La Regla de L'Hôpital"],
                "correct_index": 1,
                "feedback": "Incorrecto. Backpropagation utiliza la Regla de la Cadena de forma recursiva para derivar errores compuestos en capas ocultas."
            }
        },
        {
            "order": 14,
            "title": "[AVANZADO] Gradient Descent",
            "section_type": "explicacion",
            "content": """
<h3>Descenso de Gradiente y Tasa de Aprendizaje</h3>
<p>El <strong>Descenso de Gradiente (Gradient Descent)</strong> es el algoritmo de optimización nuclear utilizado para entrenar redes neuronales ajustando iterativamente sus pesos en función de los gradientes calculados mediante Backpropagation.</p>
<p>La regla de actualización de un peso $w$ se define matemáticamente como:</p>
<p>$$w_{nuevo} = w_{actual} - \eta \frac{\partial E}{\partial w}$$</p>
<p>Donde el hiperparámetro crítico $\eta$ (letra griega eta) representa la <strong>Tasa de Aprendizaje (Learning Rate)</strong>. La tasa de aprendizaje controla el tamaño del paso que damos en cada iteración descendente por la topografía de la función de pérdida:</p>
<ul>
    <li>Si la tasa de aprendizaje es <strong>demasiado pequeña</strong>, el entrenamiento será extremadamente lento y puede quedar atrapado en mínimos locales planos.</li>
    <li>Si es <strong>demasiado grande</strong>, el algoritmo puede oscilar y divergir bruscamente, saltándose por completo el mínimo global y desestabilizando el entrenamiento.</li>
</ul>
""",
            "challenge": {
                "prompt": "¿Qué consecuencia crítica ocurre en el entrenamiento de una red neuronal si ajustamos una Tasa de Aprendizaje (Learning Rate) extremadamente alta?",
                "choices": ["A) El entrenamiento converge de forma instantánea al mínimo global.", "B) El algoritmo puede oscilar, saltarse el mínimo global y divergir destructivamente.", "C) Los pesos de la red neuronal se congelan en cero de forma permanente."],
                "correct_index": 1,
                "feedback": "Incorrecto. Una tasa excesivamente alta causa oscilaciones violentas e inestabilidad (divergencia en la optimización)."
            }
        },
        {
            "order": 15,
            "title": "[AVANZADO] Taller Optimización",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Descenso de Gradiente en Acción</h3>
<p>En este taller práctico programamos un optimizador de Descenso de Gradiente Estocástico (SGD) en Python. Aplicamos el optimizador sobre una superficie tridimensional sintética para visualizar la convergencia de una neurona entrenando sobre una compuerta lógica.</p>
<p>El script calcula interativamente las derivadas y actualiza los parámetros empleando una tasa de aprendizaje adaptativa de $\eta = 0.05$. Observamos cómo el error cuadrático medio (MSE) disminuye de forma constante a medida que los pesos descienden por el valle de pérdida matemática, estabilizándose cuando la magnitud del gradiente se aproxima a cero.</p>
""",
            "challenge": {
                "prompt": "Al monitorizar el entrenamiento mediante Descenso de Gradiente, ¿cómo sabemos que el optimizador ha convergido y debe detenerse?",
                "choices": ["A) Cuando la tasa de error aumenta drásticamente.", "B) Cuando el gradiente del error se aproxima a cero y el valor de la pérdida (Loss) se estabiliza.", "C) Cuando la tasa de aprendizaje se vuelve infinitamente grande."],
                "correct_index": 1,
                "feedback": "Incorrecto. La convergencia se alcanza cuando los pesos dejan de cambiar significativamente y la pérdida se estabiliza cerca del fondo del valle."
            }
        },
        {
            "order": 16,
            "title": "[AVANZADO] Deep Learning",
            "section_type": "explicacion",
            "content": """
<h3>La Revolución del Deep Learning (Aprendizaje Profundo)</h3>
<p>El <strong>Deep Learning</strong> es una subrama del Machine Learning basada en el uso de arquitecturas de redes neuronales artificiales profundas (que contienen múltiples capas ocultas interconectadas de forma secuencial).</p>
<p>La gran revolución del Deep Learning frente al Machine Learning tradicional radica en la capacidad de realizar un <strong>Aprendizaje Automático de Características (Representation Learning)</strong>. En los algoritmos clásicos, un experto humano debía extraer y seleccionar manualmente las características de entrada (feature engineering). En cambio, en una red profunda, las primeras capas detectan patrones primitivos básicos (como bordes y contornos en imágenes), las capas intermedias combinan estos bordes para formar texturas y partes de objetos, y las últimas capas consolidan representaciones semánticas complejas (como rostros completos u objetos enteros), todo de forma totalmente automatizada a través del entrenamiento.</p>
""",
            "challenge": {
                "prompt": "¿Cuál es la principal ventaja evolutiva del Deep Learning frente a los algoritmos de Machine Learning tradicionales?",
                "choices": ["A) Su capacidad de ejecutarse sin usar memoria de computador.", "B) Su habilidad para realizar aprendizaje de representaciones (Representation Learning) y extraer características complejas automáticamente sin intervención humana manual.", "C) Que solo funciona con variables categóricas booleanas estrictas."],
                "correct_index": 1,
                "feedback": "Incorrecto. La capacidad de aprender características jerárquicas directamente desde datos en bruto es la esencia revolucionaria del Deep Learning."
            }
        },
        {
            "order": 17,
            "title": "[AVANZADO] Procesamiento Texto",
            "section_type": "explicacion",
            "content": """
<h3>Procesamiento del Lenguaje Natural (NLP)</h3>
<p>El <strong>Procesamiento del Lenguaje Natural (NLP)</strong> es la disciplina científica que combina la lingüística y la Inteligencia Artificial para permitir que las computadoras comprendan, interpreten y generen lenguaje humano.</p>
<p>Antes de que una red neuronal profunda (como un Transformer) pueda procesar texto, este debe ser sometido a un riguroso pipeline de preprocesamiento numérico:</p>
<ol>
    <li><strong>Tokenización:</strong> Consiste en dividir la cadena de texto crudo en unidades mínimas con significado llamadas <strong>tokens</strong> (que pueden ser palabras completas, raíces gramaticales o subpalabras).</li>
    <li><strong>Construcción de Vocabulario:</strong> Asignación de un número entero índice único para cada token único encontrado en el corpus de texto.</li>
    <li><strong>Word Embeddings (Incrustaciones de Palabras):</strong> Mapeo de cada entero índice en un vector denso de números reales de alta dimensión (como 512 dimensiones). Estos vectores se entrenan de tal forma que palabras con afinidad semántica o contextos similares queden geográficamente muy cercanas en el espacio vectorial multidimensional.</li>
</ol>
""",
            "challenge": {
                "prompt": "¿En qué consiste la etapa inicial de Tokenización en el procesamiento de texto para Inteligencia Artificial?",
                "choices": ["A) En encriptar el texto con llaves simétricas públicas.", "B) En fragmentar el flujo de texto continuo en unidades mínimas discretas llamadas tokens (como palabras o subpalabras).", "C) En calcular la covarianza de la matriz de términos de entrada."],
                "correct_index": 1,
                "feedback": "Incorrecto. La tokenización divide el texto libre en elementos básicos discretos comprensibles para las etapas de vectorización."
            }
        },
        {
            "order": 18,
            "title": "[AVANZADO] Proyecto Final IA",
            "section_type": "demo",
            "content": """
<h3>Proyecto de Graduación: Clasificador Neural de Sentimiento</h3>
<p>En este módulo práctico final de graduación consolidamos todos los conocimientos adquiridos. Desarrollamos un clasificador neural profundo en Python para evaluar el sentimiento de reseñas de usuarios sobre tecnología (reseñas positivas frente a reseñas negativas).</p>
<p>El pipeline del proyecto final requiere:</p>
<ol>
    <li>Tokenizar un dataset compuesto por 10,000 reseñas reales de productos tecnológicos.</li>
    <li>Entrenar embeddings vectoriales semánticos para codificar el significado contextual de los términos.</li>
    <li>Implementar una red neuronal multicapa con inicialización de pesos aleatorios óptima.</li>
    <li>Ajustar hiperparámetros de bias y regularizar con dropout para evitar el sobreajuste.</li>
    <li>Calcular los gradientes por Backpropagation y optimizar con SGD usando una tasa de aprendizaje controlada.</li>
</ol>
<p>Sube tu entregable final (.ipynb o .py) conteniendo el entrenamiento y métricas del modelo entrenado para que sea calificado de forma final por el instructor.</p>
""",
            "challenge": {
                "prompt": "¿Qué métricas y flujos clave se consolidan para evaluar el Clasificador de Sentimiento del Proyecto Final?",
                "choices": ["A) Únicamente el tamaño físico en kilobytes de la base de datos.", "B) El pipeline completo de preprocesamiento, tokenización, embeddings vectoriales, entrenamiento MLP con Backpropagation y evaluación con datos no vistos.", "C) Únicamente la eliminación de la capa oculta de la red neuronal."],
                "correct_index": 1,
                "feedback": "Incorrecto. El proyecto final consolida la aplicación integrada de todo el flujo de NLP y Deep Learning estudiado a lo largo del curso."
            }
        }
    ],

    # COURSE 5: REGRESION LINEAL PREDICTIVA
    5: [
        {
            "order": 1,
            "title": "[BASICO] Estadística Predictiva",
            "section_type": "explicacion",
            "content": """
<h3>Estadística Descriptiva e Inferencial Predictiva</h3>
<p>La <strong>Estadística Predictiva</strong> es la ciencia de utilizar datos históricos para construir modelos matemáticos que estimen el comportamiento futuro de variables desconocidas. Se fundamenta firmemente sobre la teoría de la probabilidad y la estadística clásica descriptiva e inferencial.</p>
<p>Dos de las medidas estadísticas más cruciales sobre las que descansan los algoritmos lineales son:</p>
<ul>
    <li><strong>La Media Aritmética ($\bar{x}$):</strong> Representa el centro de masa o promedio aritmético de una distribución de datos. Se calcula sumando todas las observaciones divididas por el número total de muestras ($n$).</li>
    <li><strong>La Desviación Estándar ($\sigma$):</strong> Es una medida cuantitativa de la dispersión de los datos alrededor de la media. Un valor de desviación estándar pequeño indica que los datos están densamente agrupados cerca del promedio; un valor alto indica una alta dispersión y variabilidad de las observaciones.</li>
</ul>
<p>El entendimiento del centro de masa y la dispersión es vital, ya que los modelos predictivos asumen que los residuos o errores de estimación se distribuirán de forma normal alrededor de una media de cero con varianza constante.</p>
""",
            "challenge": {
                "prompt": "¿Qué medida estadística cuantitativa describe qué tan dispersos se encuentran los puntos de datos individuales alrededor de su promedio aritmético?",
                "choices": ["A) La Media Aritmética", "B) La Desviación Estándar", "C) El Coeficiente de Determinación"],
                "correct_index": 1,
                "feedback": "Incorrecto. La Desviación Estándar es la métrica de dispersión por excelencia sobre la media aritmética."
            }
        },
        {
            "order": 2,
            "title": "[BASICO] Covarianza",
            "section_type": "explicacion",
            "content": """
<h3>La Covarianza y el Coeficiente de Correlación</h3>
<p>Para construir modelos predictivos lineales, primero debemos evaluar si existe una relación lineal entre las variables de estudio. La métrica fundamental para evaluar esta relación es la <strong>Covarianza ($\text{Cov}(X, Y)$)</strong>.</p>
<p>La covarianza mide el grado de variación conjunta de dos variables aleatorias numéricas. Se define matemáticamente como el promedio del producto de las desviaciones de cada variable respecto a su media aritmética:</p>
<p>$$\text{Cov}(X, Y) = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$</p>
<p>La naturaleza de la covarianza nos indica la dirección del movimiento conjunto de las variables:</p>
<ul>
    <li><strong>Covarianza Positiva ($> 0$):</strong> Indica que cuando la variable $X$ aumenta, la variable $Y$ también tiende a aumentar de forma proporcional.</li>
    <li><strong>Covarianza Negativa ($< 0$):</strong> Indica una relación inversa; cuando la variable $X$ aumenta, la variable $Y$ tiende a disminuir.</li>
    <li><strong>Covarianza Cercana a Cero:</strong> Indica la ausencia de una relación lineal aparente entre las variables.</li>
</ul>
""",
            "challenge": {
                "prompt": "¿Qué nos indica matemáticamente una Covarianza Negativa (< 0) obtenida entre dos variables continuas X y Y?",
                "choices": ["A) Que ambas variables crecen simultáneamente de forma proporcional.", "B) Que existe una relación lineal directa y perfecta sin error residual.", "C) Que cuando la variable X aumenta, la variable Y tiende a disminuir (relación inversa)."],
                "correct_index": 2,
                "feedback": "Incorrecto. Una covarianza negativa señala una relación inversa entre las dos variables numéricas analizadas."
            }
        },
        {
            "order": 3,
            "title": "[BASICO] Taller Estadístico",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Calculando Relaciones Lineales</h3>
<p>En este laboratorio práctico, cargamos un dataset con el comportamiento histórico de la inversión en marketing frente a las ventas mensuales de la compañía. El objetivo es calcular analíticamente su covarianza y graficar su comportamiento conjunto.</p>
<p>Aplicando las fórmulas sobre nuestro conjunto de datos:</p>
<ol>
    <li>Calculamos la media de marketing ($\bar{x}$) y la media de ventas ($\bar{y}$).</li>
    <li>Restamos la media a cada punto de datos, obteniendo los vectores de desviación.</li>
    <li>Multiplicamos los vectores y promediamos el resultado. Obtenemos una covarianza fuertemente positiva de $+245.8$, lo que valida matemáticamente la viabilidad de ajustar una regresión lineal predictiva sobre estas variables.</li>
</ol>
""",
            "challenge": {
                "prompt": "Si en nuestro taller práctico obtenemos una covarianza fuertemente positiva entre Marketing y Ventas, ¿cuál es el siguiente paso lógico?",
                "choices": ["A) Descartar la variable de Marketing por falta de correlación.", "B) Ajustar un modelo de regresión lineal para predecir las ventas basándonos en la inversión de marketing.", "C) Aplicar un algoritmo genético de enjambre discreto para TSP."],
                "correct_index": 1,
                "feedback": "Incorrecto. La covarianza positiva confirma que existe una relación lineal que puede ser modelada predictivamente por una regresión."
            }
        },
        {
            "order": 4,
            "title": "[BASICO] Regresión Simple",
            "section_type": "explicacion",
            "content": """
<h3>Estructura del Modelo de Regresión Lineal Simple</h3>
<p>La <strong>Regresión Lineal Simple</strong> es un enfoque matemático supervisado que modela la relación lineal entre una única variable explicativa independiente ($X$) y una variable de respuesta continua dependiente ($Y$).</p>
<p>La ecuación formal del modelo lineal poblacional se define como:</p>
<p>$$Y = \beta_0 + \beta_1 X + \epsilon$$</p>
<p>Donde los componentes de la ecuación representan:</p>
<ul>
    <li><strong>$\beta_1$ (Pendiente o Coeficiente):</strong> Representa el cambio esperado en la variable dependiente $Y$ por cada incremento unitario en la variable independiente $X$.</li>
    <li><strong>$\beta_0$ (Intercepto o Sesgo):</strong> Representa el valor esperado de la variable $Y$ cuando la variable independiente $X$ es exactamente igual a cero. Graficamente, es el punto exacto donde la recta de regresión intersecta el eje vertical de las ordenadas ($Y$).</li>
    <li><strong>$\epsilon$ (Término de Error o Residuo):</strong> Representa la diferencia o desviación entre el valor observado real de $Y$ y el valor estimado por la línea recta teórica.</li>
</ul>
""",
            "challenge": {
                "prompt": "En la ecuación matemática de la regresión lineal simple, ¿qué representa físicamente el término de Intercepto (β0)?",
                "choices": ["A) El cambio esperado en Y ante un incremento unitario de X.", "B) El valor esperado de la variable dependiente Y cuando la variable independiente X es exactamente igual a cero.", "C) La tasa de aprendizaje o el multiplicador de penalización de la regularización."],
                "correct_index": 1,
                "feedback": "Incorrecto. El intercepto representa el valor base inicial de Y cuando la variable predictora X se anula (es cero)."
            }
        },
        {
            "order": 5,
            "title": "[BASICO] Minimos Cuadrados",
            "section_type": "explicacion",
            "content": """
<h3>El Método de Mínimos Cuadrados Ordinarios (OLS)</h3>
<p>Para ajustar la recta óptima de regresión lineal, debemos calcular los coeficientes idóneos $\beta_0$ y $\beta_1$. El algoritmo matemático por excelencia para resolver este problema es el método de <strong>Mínimos Cuadrados Ordinarios (OLS - Ordinary Least Squares)</strong>.</p>
<p>El principio fundamental de OLS es <strong>minimizar la Suma de los Residuos al Cuadrado (RSS - Residual Sum of Squares)</strong>, es decir, minimizar la sumatoria acumulada de las distancias verticales al cuadrado entre los puntos observados reales ($y_i$) y los puntos estimados teóricos de la recta ($\hat{y}_i$):</p>
<p>$$\text{Minimizar RSS} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - (\beta_0 + \beta_1 x_i))^2$$</p>
<p>Al derivar parcialmente la función RSS respecto a $\beta_0$ y $\beta_1$ e igualar a cero, deducimos analíticamente las fórmulas directas de los coeficientes óptimos:</p>
<p>$$\beta_1 = \frac{\text{Cov}(X, Y)}{\text{Var}(X)}$$</p>
<p>$$\beta_0 = \bar{y} - \beta_1 \bar{x}$$</p>
<p>Estas fórmulas cerradas garantizan de forma determinista la menor desviación cuadrada posible en todo el plano euclidiano.</p>
""",
            "challenge": {
                "prompt": "¿Cuál es el objetivo principal que minimiza el método de Mínimos Cuadrados Ordinarios (OLS) para ajustar la recta óptima?",
                "choices": ["A) Minimizar el número total de observaciones atípicas.", "B) Minimizar la Suma de los Residuos elevados al Cuadrado (RSS) entre los puntos reales y la estimación.", "C) Minimizar el valor del intercepto beta0 para cruzar por el origen."],
                "correct_index": 1,
                "feedback": "Incorrecto. El algoritmo OLS minimiza cuadráticamente las distancias de los errores (residuos) para optimizar la recta."
            }
        },
        {
            "order": 6,
            "title": "[BASICO] Predicción Salarial",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Estimación de Ingresos según Experiencia</h3>
<p>En este taller práctico construimos un modelo OLS en Python para predecir el salario estimado de desarrolladores de software basándonos en sus Años de Experiencia profesional.</p>
<p>Deduciendo los coeficientes óptimos a partir del conjunto de datos de entrenamiento:</p>
<ul>
    <li>Obtenemos una pendiente ajustada $\beta_1 = \$5,200$ dólares anuales.</li>
    <li>Obtenemos un intercepto base $\beta_0 = \$45,000$ dólares anuales.</li>
</ul>
<p>Esto define nuestra ecuación predictiva lineal como: <code>Salario = 45000 + 5200 * Experiencia</code>. Si deseamos estimar el salario para un desarrollador con 5 años de experiencia, evaluamos el modelo directo de la siguiente forma:</p>
<p>$$\text{Predicción} = 45000 + 5200 \times 5 = 45000 + 26000 = \$71,000\text{ dólares anuales.}$$</p>
""",
            "challenge": {
                "prompt": "Usando la ecuación Salario = 45000 + 5200 * Experiencia deducida en el taller, ¿cuál es el salario estimado para un profesional con 3 años de experiencia?",
                "choices": ["A) $45,000 dólares", "B) $60,600 dólares", "C) $71,000 dólares"],
                "correct_index": 1,
                "feedback": "Incorrecto. Reemplazando Experiencia = 3: 45000 + 5200 * 3 = 45000 + 15600 = 60600 dólares."
            }
        },
        {
            "order": 7,
            "title": "[INTERMEDIO] Métricas de Error",
            "section_type": "explicacion",
            "content": """
<h3>Métricas de Evaluación de Desempeño en Regresión</h3>
<p>Para cuantificar la calidad predictiva de un modelo de regresión lineal y comparar diferentes aproximaciones, debemos calcular métricas matemáticas de error sobre el conjunto de validación de prueba. Las métricas más relevantes son:</p>
<ul>
    <li><strong>Error Absoluto Medio (MAE - Mean Absolute Error):</strong> Promedio aritmético de las diferencias absolutas entre los valores reales ($y_i$) y estimados ($\hat{y}_i$). Al no elevar al cuadrado, trata a todas las desviaciones de forma lineal:
        $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$
    </li>
    <li><strong>Error Cuadrático Medio (MSE - Mean Squared Error):</strong> Promedio de los residuos al cuadrado. Al elevar los errores al cuadrado, <strong>penaliza severamente las desviaciones grandes u observaciones atípicas (outliers)</strong>:
        $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$
    </li>
    <li><strong>Coeficiente de Determinación ($R^2$):</strong> Proporción de la varianza total de la variable dependiente $Y$ que es explicada y capturada por las variables predictoras del modelo. Oscila entre $[0, 1]$ (donde $1$ representa un ajuste perfecto sin error).
    </li>
</ul>
""",
            "challenge": {
                "prompt": "¿Qué métrica de error penaliza con mayor severidad a los errores grandes y valores atípicos (outliers) debido a su formulación cuadrática?",
                "choices": ["A) Error Absoluto Medio (MAE)", "B) Coeficiente de Determinación (R2)", "C) Error Cuadrático Medio (MSE)"],
                "correct_index": 2,
                "feedback": "Incorrecto. El MSE eleva los errores al cuadrado, magnificando la penalización ante grandes desviaciones."
            }
        },
        {
            "order": 8,
            "title": "[INTERMEDIO] Análisis Residual",
            "section_type": "explicacion",
            "content": """
<h3>Análisis Residual y Supuestos de Gauss-Markov</h3>
<p>Para garantizar que los estimadores calculados por Mínimos Cuadrados Ordinarios (OLS) sean los mejores estimadores lineales insesgados posibles (es decir, que cumplan el Teorema de Gauss-Markov), se deben validar rigurosamente los supuestos del modelo a través de los residuos.</p>
<p>El supuesto fundamental del análisis de residuos es la <strong>Homocedasticidad</strong>. La homocedasticidad exige que la varianza de los términos de error ($\epsilon_i$) sea constante y homogénea para todos los niveles de la variable predictora independiente $X$.</p>
<p>Graficamente, si trazamos un diagrama de dispersión de los residuos en el eje vertical frente a los valores ajustados en el eje horizontal, los puntos deben distribuirse de forma totalmente aleatoria sin formar ningún patrón geométrico (como un abanico o una trompeta). Si los errores forman una trompeta, estamos ante un problema de <strong>heterocedasticidad</strong>, lo que indica que la incertidumbre y la variabilidad de las predicciones cambian significativamente con la magnitud de los datos.</p>
""",
            "challenge": {
                "prompt": "¿Qué término estadístico describe el supuesto crucial de que la varianza del término de error de una regresión lineal debe ser constante para todas las observaciones?",
                "choices": ["A) Heterocedasticidad", "B) Homocedasticidad", "C) Multicolinealidad"],
                "correct_index": 1,
                "feedback": "Incorrecto. La Homocedasticidad denota la homogeneidad de la varianza de los residuos en el modelo."
            }
        },
        {
            "order": 9,
            "title": "[INTERMEDIO] Taller Evaluación",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Diagnóstico de Errores y Homocedasticidad</h3>
<p>En este laboratorio cargamos los residuos del modelo de predicción salarial ajustado anteriormente. El objetivo es calcular de forma programática las métricas MAE, MSE y diagnosticar visualmente si el supuesto de homocedasticidad se cumple.</p>
<p>Al generar el gráfico de dispersión de los residuos:</p>
<ol>
    <li>Observamos un comportamiento libre de patrones definidos, distribuyéndose los errores de forma uniforme en una banda horizontal estrecha paralela al eje cero.</li>
    <li>Esto confirma que la varianza de los residuos es homogénea y constante.</li>
    <li>Validamos que se cumple el supuesto de homocedasticidad de Gauss-Markov, lo que certifica la estabilidad y fiabilidad analítica del modelo lineal ajustado.</li>
</ol>
""",
            "challenge": {
                "prompt": "En nuestro taller práctico de diagnóstico, ¿qué distribución visual de los residuos indica un cumplimiento satisfactorio de la homocedasticidad?",
                "choices": ["A) Un patrón geométrico bien definido en forma de abanico ascendente.", "B) Una dispersión de puntos aleatoria y uniforme dentro de una banda horizontal paralela al eje cero.", "C) Una línea curva sinusoidal de error acumulado."],
                "correct_index": 1,
                "feedback": "Incorrecto. Una dispersión aleatoria sin patrones definidos confirma que la varianza de los errores es constante (homocedástica)."
            }
        },
        {
            "order": 10,
            "title": "[INTERMEDIO] Regresión Múltiple",
            "section_type": "explicacion",
            "content": """
<h3>El Modelo de Regresión Lineal Múltiple</h3>
<p>En el mundo real, los fenómenos son complejos y están determinados por múltiples factores causales simultáneos. Para modelar estos escenarios complejos, ampliamos la regresión lineal simple a la <strong>Regresión Lineal Múltiple</strong>, permitiendo incorporar múltiples variables explicativas independientes ($X_1, X_2, \dots, X_p$).</p>
<p>La ecuación matemática que define al modelo de regresión lineal múltiple es:</p>
<p>$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$</p>
<p>Donde cada pendiente $\beta_j$ representa el efecto y cambio esperado en la variable dependiente $Y$ por cada incremento unitario en la variable explicativa $X_j$, <strong>manteniendo todas las demás variables predictoras constantes (condición Ceteris Paribus)</strong>.</p>
<p>El ajuste del modelo múltiple permite controlar estadísticamente las variables confusoras, aislando el verdadero impacto individual de cada factor explicativo sobre el resultado final predicho.</p>
""",
            "challenge": {
                "prompt": "En una regresión lineal múltiple, ¿bajo qué condición estricta se interpreta el impacto individual de un coeficiente beta_j sobre la variable dependiente Y?",
                "choices": ["A) Permitiendo que todas las variables predictoras cambien libremente de forma simultánea.", "B) Manteniendo todas las demás variables independientes de la ecuación constantes (Ceteris Paribus).", "C) Incrementando exponencialmente la tasa de aprendizaje."],
                "correct_index": 1,
                "feedback": "Incorrecto. El coeficiente múltiple mide el impacto neto de una variable aislando el efecto de las demás al mantenerlas fijas."
            }
        },
        {
            "order": 11,
            "title": "[INTERMEDIO] Variables Dummy",
            "section_type": "explicacion",
            "content": """
<h3>Codificación de Variables Categóricas (Variables Dummy)</h3>
<p>Los algoritmos de regresión lineal son puramente matemáticos y vectoriales; solo pueden operar sobre números reales continuos. Sin embargo, en el Machine Learning a menudo nos encontramos con variables cualitativas categóricas (como género, ciudad de origen o nivel educativo).</p>
<p>Para alimentar estas categorías en un modelo lineal, implementamos la codificación de <strong>Variables Dummy (Variables Indicadoras)</strong>. Consiste en crear nuevas variables numéricas binarias que toman únicamente el valor de $1$ si la categoría está presente, y $0$ si está ausente.</p>
<p>Un detalle técnico crítico es evitar la <strong>Trampa de la Variable Dummy</strong> (que genera una colinealidad perfecta en el modelo). Si una variable categórica posee $k$ categorías exclusivas posibles, debemos incorporar únicamente **$k - 1$ variables dummy** en la ecuación. La categoría omitida actúa como el nivel de referencia base contra el cual se comparan estadísticamente las demás.</p>
""",
            "challenge": {
                "prompt": "Si tenemos una variable categórica 'Ciudad' con 4 categorías posibles, ¿cuántas variables dummy binarias debemos incorporar en el modelo para evitar la Trampa de la Variable Dummy?",
                "choices": ["A) Exactamente 4 variables dummy", "B) Exactamente 3 variables dummy", "C) Ninguna, se deben ingresar las cadenas de texto directamente"],
                "correct_index": 1,
                "feedback": "Incorrecto. Se deben incorporar k-1 variables dummy (4-1 = 3) para evitar colinealidad perfecta con la constante del intercepto."
            }
        },
        {
            "order": 12,
            "title": "[INTERMEDIO] Mercado Inmobiliario",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Modelando Precios Inmobiliarios</h3>
<p>En este laboratorio práctico programamos una regresión lineal múltiple en Python para predecir los precios de venta de apartamentos residenciales. Incorporamos variables continuas como los metros cuadrados de construcción, y variables categóricas cualitativas como el barrio ("Norte", "Sur", "Oeste").</p>
<p>Aplicando las transformaciones estructurales:</p>
<ol>
    <li>Codificamos las categorías del barrio en variables dummy binarias, omitiendo la categoría "Oeste" para que actúe como nivel de referencia base.</li>
    <li>El modelo múltiple ajustado arroja un coeficiente positivo para el barrio "Norte" de $+\$15,000$ dólares en comparación con el barrio base "Oeste", controlando el tamaño de los apartamentos.</li>
    <li>Esto nos permite formular predicciones complejas, analizando cuantitativamente cómo cambia el precio de la propiedad combinando factores espaciales y cualitativos.</li>
</ol>
""",
            "challenge": {
                "prompt": "En nuestro taller de precios de inmuebles, ¿qué nos indica un coeficiente positivo de +$15,000 para el barrio 'Norte' si la categoría base omitida es 'Oeste'?",
                "choices": ["A) Que los apartamentos en el barrio Oeste son 15,000 dólares más caros.", "B) Que un apartamento en el Norte cuesta en promedio 15,000 dólares más que uno equivalente en el barrio de referencia Oeste.", "C) Que el barrio Norte posee 15,000 metros cuadrados de construcción adicionales."],
                "correct_index": 1,
                "feedback": "Incorrecto. El coeficiente dummy mide la diferencia esperada en el precio respecto a la categoría base de referencia (Oeste)."
            }
        },
        {
            "order": 13,
            "title": "[AVANZADO] Regresión Logística",
            "section_type": "explicacion",
            "content": """
<h3>Regresión Logística para Clasificación Binaria</h3>
<p>A pesar de su nombre, la <strong>Regresión Logística</strong> es un algoritmo fundamental supervisado para resolver problemas de **Clasificación Binaria** (donde la variable de respuesta $Y$ toma únicamente dos valores posibles: $0$ o $1$, como Aprobado/Reprobado).</p>
<p>Si intentamos usar una regresión lineal tradicional para predecir clases binarias, nos toparemos con dos problemas severos: el modelo producirá estimaciones de probabilidad absurdas fuera del intervalo válido de $[0, 1]$, y la recta se verá severamente desestabilizada por la presencia de valores extremos.</p>
<p>Para solucionar esto, la regresión logística modela el logaritmo de las probabilidades a favor de la clase activa (log-odds), aplicando la <strong>función de enlace Logística o Sigmoide ($\sigma$)</strong> sobre la combinación lineal predictora:</p>
<p>$$P(Y=1|X) = \sigma(\beta_0 + \beta_1 X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 X)}}$$</p>
<p>Esta transformación comprime determinísticamente cualquier valor numérico real continuo al intervalo cerrado $[0, 1]$, interpretándose de forma directa como la probabilidad de que una muestra pertenezca a la clase objetivo.</p>
""",
            "challenge": {
                "prompt": "¿Por qué se utiliza la función logística (Sigmoide) en lugar de una regresión lineal simple para tareas de clasificación binaria?",
                "choices": ["A) Porque elimina por completo la necesidad de calcular coeficientes beta.", "B) Para comprimir los resultados de la combinación lineal predictora estrictamente en el intervalo continuo [0, 1], interpretándose como probabilidad.", "C) Para poder clasificar múltiples categorías discretas de forma no lineal sin límites."],
                "correct_index": 1,
                "feedback": "Incorrecto. La función sigmoide restringe las predicciones al rango [0,1], transformándolas en probabilidades probabilísticas válidas."
            }
        },
        {
            "order": 14,
            "title": "[AVANZADO] Matriz Confusión",
            "section_type": "explicacion",
            "content": """
<h3>Evaluación con Matriz de Confusión y Métricas Binarias</h3>
<p>En las tareas de clasificación predictiva resueltas mediante regresión logística, la exactitud global (accuracy) es una métrica insuficiente y engañosa si el conjunto de datos está desbalanceado (por ejemplo, detectar fraudes que ocurren en solo el 1% de las transacciones).</p>
<p>La herramienta analítica estándar por excelencia para evaluar estos modelos es la <strong>Matriz de Confusión</strong>, una tabla cruzada bidimensional que clasifica las predicciones reales frente a las estimadas en cuatro cuadrantes estructurales:</p>
<ul>
    <li><strong>Verdaderos Positivos (TP):</strong> Casos positivos clasificados correctamente como positivos.</li>
    <li><strong>Falsos Positivos (FP) - Error Tipo I:</strong> Casos negativos clasificados incorrectamente como positivos.</li>
    <li><strong>Verdaderos Negativos (TN):</strong> Casos negativos clasificados correctamente como negativos.</li>
    <li><strong>Falsos Negativos (FN) - Error Tipo II:</strong> Casos positivos clasificados incorrectamente como negativos.</li>
</ul>
<p>A partir de estos cuatro cuadrantes, calculamos métricas de alta fidelidad diagnóstica:</p>
<p>$$\text{Precisión (Precision)} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$</p>
<p>$$\text{Sensibilidad (Recall / Sensitivity)} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$</p>
""",
            "challenge": {
                "prompt": "¿Qué error tipo representa clasificar incorrectamente un caso negativo como positivo (Falso Positivo) en una matriz de confusión?",
                "choices": ["A) Error de Especificación de Varianza", "B) Error Tipo II", "C) Error Tipo I"],
                "correct_index": 2,
                "feedback": "Incorrecto. Un Falso Positivo se conoce en la estadística clásica inferencial como un Error de Tipo I."
            }
        },
        {
            "order": 15,
            "title": "[AVANZADO] Taller Logístico",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Detección de Abandono de Clientes (Churn)</h3>
<p>En este taller práctico implementamos un modelo de regresión logística en Python para predecir si un suscriptor cancelará su servicio de suscripción mensual basándonos en variables como el uso de datos mensuales y la cantidad de reclamos de soporte.</p>
<p>Evaluando los resultados tras ajustar el clasificador logístico:</p>
<ol>
    <li>Generamos la matriz de confusión sobre el subconjunto de prueba de 200 clientes.</li>
    <li>Identificamos $45$ Verdaderos Positivos (TP) y $5$ Falsos Negativos (FN).</li>
    <li>Calculamos manualmente la sensibilidad o recall del modelo:
        $$\text{Recall} = \frac{45}{45 + 5} = \frac{45}{50} = 90\%$$
    </li>
    <li>Validamos que el modelo captura exitosamente el 90% de los clientes en riesgo de abandono real, demostrando la alta capacidad predictiva de la regresión logística entrenada.</li>
</ol>
""",
            "challenge": {
                "prompt": "Usando los datos del taller (TP = 45, FN = 5), ¿cuál es la sensibilidad (Recall) del modelo entrenado?",
                "choices": ["A) 10%", "B) 90%", "C) 50%"],
                "correct_index": 1,
                "feedback": "Incorrecto. Sensibilidad (Recall) = TP / (TP + FN) = 45 / (45 + 5) = 45 / 50 = 0.90 (90%)."
            }
        },
        {
            "order": 16,
            "title": "[AVANZADO] Multicolinealidad",
            "section_type": "explicacion",
            "content": """
<h3>Multicolinealidad y el Factor de Inflación de la Varianza (VIF)</h3>
<p>En la regresión lineal múltiple, la <strong>Multicolinealidad</strong> es una patología grave de los datos que ocurre cuando dos o más variables predictoras independientes en el modelo están fuertemente correlacionadas de forma lineal entre sí.</p>
<p>La colinealidad desestabiliza críticamente los coeficientes $\beta_j$. Bajo colinealidad, es imposible aislar el impacto de cada variable individual (Ceteris Paribus) y pequeñas variaciones en los datos provocarán saltos drásticos e impredecibles en los valores de los coeficientes, aumentando drásticamente sus errores estándar.</p>
<p>La herramienta cuantitativa estándar para diagnosticar y detectar la colinealidad es el <strong>Factor de Inflación de la Varianza (VIF - Variance Inflation Factor)</strong>. El VIF evalúa qué tanto se infla la varianza de un coeficiente debido al efecto de la colinealidad. La regla heurística estándar indica que:</p>
<ul>
    <li>Un valor de $\text{VIF} = 1$ indica ausencia absoluta de colinealidad.</li>
    <li>Un valor de $\text{VIF}$ entre $1$ y $5$ representa una colinealidad moderada aceptable.</li>
    <li><strong>Un valor de $\text{VIF} \geq 10$ indica una colinealidad severa crítica</strong>, lo que exige mitigar el problema eliminando variables correlacionadas o aplicando técnicas de regularización avanzadas.</li>
</ul>
""",
            "challenge": {
                "prompt": "¿Qué valor umbral del Factor de Inflación de la Varianza (VIF) se considera heurísticamente como señal de multicolinealidad severa que exige intervención?",
                "choices": ["A) VIF = 1", "B) VIF menor a 5", "C) VIF igual o mayor a 10"],
                "correct_index": 2,
                "feedback": "Incorrecto. Un VIF >= 10 es el umbral estándar internacional de multicolinealidad severa y destructiva."
            }
        },
        {
            "order": 17,
            "title": "[AVANZADO] Regularización",
            "section_type": "explicacion",
            "content": """
<h3>Métodos de Regularización Avanzados: Lasso y Ridge</h3>
<p>Cuando un modelo lineal múltiple sufre de sobreajuste (overfitting) o colinealidad severa, el algoritmo OLS tradicional falla al producir coeficientes sobredimensionados e inestables. Para solucionar esto, aplicamos técnicas de **Regularización**, las cuales penalizan los coeficientes de gran magnitud durante el ajuste.</p>
<p>Los dos enfoques de regularización más influyentes en el Machine Learning predictivo son:</p>
<ol>
    <li><strong>Regresión Ridge (Regularización L2):</strong> Añade un término de penalización a la función de pérdida proporcional a la suma de los <strong>coeficientes al cuadrado</strong>:
        $$\text{Pérdida Ridge} = \text{RSS} + \lambda \sum_{j=1}^{p} \beta_j^2$$
        Ridge mitiga la colinealidad reduciendo la magnitud de todos los coeficientes hacia valores cercanos a cero de forma homogénea, pero sin anularlos por completo.
    </li>
    <li><strong>Regresión Lasso (Regularización L1):</strong> Añade una penalización proporcional al <strong>valor absoluto</strong> de la magnitud de los coeficientes:
        $$\text{Pérdida Lasso} = \text{RSS} + \lambda \sum_{j=1}^{p} |\beta_j|$$
        La gran ventaja teórica de Lasso es que su geometría induce a que algunos coeficientes se reduzcan a **exactamente cero**. Por lo tanto, funciona intrínsecamente como un algoritmo automático de <strong>Selección de Características (Feature Selection)</strong>, eliminando por completo las variables irrelevantes del modelo.
    </li>
</ol>
<p>El hiperparámetro de penalización $\lambda$ (lambda) controla la intensidad de la regularización; a mayor $\lambda$, mayor es el encogimiento de los coeficientes hacia cero.</p>
""",
            "challenge": {
                "prompt": "¿Qué técnica de regularización lineal avanzada funciona adicionalmente como método automático de Selección de Características (Feature Selection) al reducir coeficientes irrelevantes a exactamente cero?",
                "choices": ["A) Regresión Ridge (L2)", "B) Regresión Lasso (L1)", "C) Mínimos Cuadrados Ordinarios (OLS)"],
                "correct_index": 1,
                "feedback": "Incorrecto. La penalización L1 de Lasso anula coeficientes irrelevantes a cero, facilitando la selección de variables."
            }
        },
        {
            "order": 18,
            "title": "[AVANZADO] Proyecto Avanzado",
            "section_type": "demo",
            "content": """
<h3>Proyecto Final de Regresión: Consolidación Predictiva de Portafolio</h3>
<p>En este laboratorio final integrador aplicamos los conocimientos estadísticos predictivos adquiridos para modelar y predecir de forma multivariable el riesgo crediticio en una corporación bancaria internacional.</p>
<p>El pipeline del proyecto final requiere:</p>
<ol>
    <li>Importar y limpiar un dataset real con el historial financiero de miles de solicitantes de crédito.</li>
    <li>Construir variables dummy para representar factores categóricos geográficos y de tipo de empleo.</li>
    <li>Calcular la covarianza y evaluar el Factor de Inflación de la Varianza (VIF) de todas las variables predictoras para descartar colinealidad severa.</li>
    <li>Ajustar y comparar un modelo predictivo lineal clásico frente a una regresión regularizada Lasso (L1) para seleccionar las variables óptimas.</li>
    <li>Evaluar el modelo óptimo utilizando una matriz de confusión sobre el conjunto de test independiente, reportando precisión, sensibilidad (recall) y error absoluto medio (MAE).</li>
</ol>
<p>Sube tu archivo entregable (.ipynb o .csv de predicciones de test) para que la nota final de tu proyecto sea calificada por el docente.</p>
""",
            "challenge": {
                "prompt": "¿Qué proceso analítico completo se consolida en el Proyecto Final de Regresión Predictiva?",
                "choices": ["A) Solo se realiza la subida de un archivo sin formatear ni procesar.", "B) El pipeline completo de análisis exploratorio, cálculo de VIF, codificación dummy, ajuste regularizado Lasso y evaluación mediante matriz de confusión.", "C) Únicamente el entrenamiento de una red neuronal profunda sin capas de entrada."],
                "correct_index": 1,
                "feedback": "Incorrecto. El proyecto final consolida de forma integrada todo el pipeline de modelado predictivo multivariable y evaluación lineal avanzada."
            }
        }
    ],

    # COURSE 6: ALGORITMOS GENETICOS
    6: [
        {
            "order": 1,
            "title": "[BASICO] Darwinismo Digital",
            "section_type": "explicacion",
            "content": """
<h3>El Concepto de Darwinismo Digital</h3>
<p>Los <strong>Algoritmos Genéticos (AG)</strong>, creados formalmente por <strong>John Holland en la década de 1970</strong>, son métodos de optimización heurística y búsqueda global inspirados en los mecanismos biológicos de la evolución natural descritos por Charles Darwin.</p>
<p>En la naturaleza, los seres vivos luchan por la supervivencia y la reproducción en entornos competitivos. El <strong>Darwinismo Digital</strong> traslada estos conceptos a la computación lógica, sustituyendo los componentes de la naturaleza con estructuras lógicas computacionales:</p>
<ul>
    <li>Los organismos vivos se representan como **cromosomas (cadenas lógicas de bits o parámetros)**.</li>
    <li>El entorno competitivo y la presión ambiental se modelan mediante una **función de aptitud (fitness)**, la cual evalúa numéricamente la calidad del cromosoma para resolver el problema de optimización.</li>
    <li>La descendencia se genera aplicando operadores probabilísticos de **Cruce (crossover) y Mutación**.</li>
</ul>
<p>El principio rector es la <strong>Supervivencia del Más Apto</strong>; a lo largo de sucesivas generaciones evolutivas virtuales, los peores cromosomas mueren, mientras que los cromosomas óptimos intercambian material genético de alto desempeño, convergiendo paulatinamente hacia la solución óptima del espacio de búsqueda.</p>
""",
            "challenge": {
                "prompt": "¿Quién creó formalmente los Algoritmos Genéticos en la década de 1970 inspirándose en el darwinismo natural?",
                "choices": ["A) Charles Darwin", "B) John Holland", "C) Frank Rosenblatt"],
                "correct_index": 1,
                "feedback": "Incorrecto. Fue John Holland quien formalizó computacionalmente los Algoritmos Genéticos en la década de los 70."
            }
        },
        {
            "order": 2,
            "title": "[BASICO] Cromosomas y Genes",
            "section_type": "explicacion",
            "content": """
<h3>Representación Genotípica y Cromosómica</h3>
<p>Para aplicar un algoritmo genético a un problema de optimización de ingeniería, primero debemos modelar las soluciones físicas potenciales utilizando estructuras de datos biológicas. En este proceso, debemos distinguir dos niveles esenciales:</p>
<ol>
    <li><strong>El Genotipo (Espacio Genético):</strong> Es el código interno de la solución, compuesto por un <strong>Cromosoma (un vector o cadena de datos)</strong>. Cada elemento o parámetro específico dentro del cromosoma representa un <strong>Gen</strong>, y los valores específicos que puede tomar cada gen en una coordenada se denominan <strong>Alelos</strong>.</li>
    <li><strong>El Fenotipo (Espacio Físico):</strong> Es la manifestación física real expresada por la decodificación del cromosoma. Representa la solución real evaluable (como los valores físicos reales de resistencia, peso y tamaño de una viga).</li>
</ol>
<p>La representación cromosómica clásica propuesta por Holland es la <strong>Codificación Binaria</strong>, donde las soluciones potenciales se representan como cadenas compactas de bits binarios (ceros y unos), actuando cada bit individual como un gen único.</p>
""",
            "challenge": {
                "prompt": "En la terminología de los Algoritmos Genéticos, ¿cómo se denomina a la representación o cadena de datos interna que codifica la solución potencial?",
                "choices": ["A) El Fenotipo", "B) El Genotipo (Cromosoma)", "C) El Alelo Físico"],
                "correct_index": 1,
                "feedback": "Incorrecto. El Genotipo o Cromosoma representa el código genético interno que almacena los genes de la solución."
            }
        },
        {
            "order": 3,
            "title": "[BASICO] Población Inicial",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Generación de Diversidad Inicial</h3>
<p>En este laboratorio práctico programamos en Python el primer bloque estructural de un algoritmo genético: la generación de la **Población Inicial** de cromosomas.</p>
<p>Al instanciar la población evolutiva inicial, el tamaño del pool de candidatos ($N$) y la aleatoriedad son hiperparámetros sumamente críticos:</p>
<ul>
    <li>Si la población inicial es <strong>muy pequeña</strong> (por ejemplo, menor a 20 cromosomas), el pool carecerá de suficiente diversidad genética y el algoritmo convergerá prematuramente en un óptimo local pobre.</li>
    <li>Si la población es <strong>demasiado grande</strong> (por ejemplo, mayor a 1,000 cromosomas), el costo de cómputo por generación colapsará los recursos del hardware.</li>
</ul>
<p>Para asegurar una exploración homogénea del espacio de búsqueda, programamos un generador pseudoaleatorio de bits binarios densos, creando una población equilibrada de $N = 100$ cromosomas con longitud uniforme de $16$ genes por cromosoma.</p>
""",
            "challenge": {
                "prompt": "¿Qué consecuencia crítica ocurre en un algoritmo genético si inicializamos la población con un tamaño extremadamente pequeño de cromosomas?",
                "choices": ["A) El algoritmo converge instantáneamente hacia el óptimo global sin costo de cómputo.", "B) El pool genético carece de diversidad y el algoritmo sufre de convergencia prematura en máximos locales pobres.", "C) Se anula por completo la tasa de mutación del sistema."],
                "correct_index": 1,
                "feedback": "Incorrecto. Una población muy reducida restringe la diversidad genética, llevando a una convergencia estéril en óptimos locales."
            }
        },
        {
            "order": 4,
            "title": "[BASICO] Función Fitness",
            "section_type": "explicacion",
            "content": """
<h3>La Función de Aptitud (Fitness Function)</h3>
<p>El motor impulsor de la evolución en los algoritmos genéticos es la evaluación objetiva de cada candidato. Este proceso está gobernado de forma absoluta por la <strong>Función de Aptitud (Fitness Function)</strong>.</p>
<p>La función de aptitud toma el cromosoma de un individuo decodificado en su fenotipo, evalúa su viabilidad para resolver el problema físico, y retorna un único valor numérico real continuo representativo de su calidad. A mayor valor de fitness, mayor es la calidad del individuo y su probabilidad reproductiva.</p>
<p>Un aspecto matemático desafiante es el diseño de funciones de aptitud para problemas con restricciones estrictas (por ejemplo, optimizar la capacidad de una mochila de carga maximizando el valor monetario sin superar un peso límite $W$). En estos escenarios, el fitness matemático incorpora **Penalizaciones**; si un cromosoma supera la restricción de peso límite, se le aplica un castigo aritmético drástico que reduce su fitness al suelo, garantizando que el operador de selección lo elimine de forma rápida de la generación.</p>
""",
            "challenge": {
                "prompt": "En el modelado con restricciones de un Algoritmo Genético, ¿qué mecanismo se integra en la función de aptitud para neutralizar a las soluciones inválidas?",
                "choices": ["A) Se elimina el bias del intercepto del cromosoma.", "B) Se le aplican penalizaciones aritméticas drásticas que reducen el valor de fitness del individuo inválido.", "C) Se le asigna una tasa de mutación del 100% de manera automática."],
                "correct_index": 1,
                "feedback": "Incorrecto. El uso de penalizaciones en el fitness anula la aptitud de los cromosomas que violan los límites físicos del problema."
            }
        },
        {
            "order": 5,
            "title": "[BASICO] Paisaje Fitness",
            "section_type": "explicacion",
            "content": """
<h3>Exploración en el Paisaje de Aptitud (Fitness Landscape)</h3>
<p>Para visualizar cómo opera un algoritmo genético, los matemáticos utilizan el concepto de <strong>Paisaje de Aptitud (Fitness Landscape)</strong>. Consiste en mapear todas las posibles soluciones en un plano bidimensional horizontal, representando el valor de aptitud (fitness) en el eje vertical vertical como montañas y valles tridimensionales.</p>
<p>El objetivo del algoritmo genético es guiar a la población a escalar el paisaje hasta conquistar el pico más alto (el <strong>Máximo Global</strong>).</p>
<p>Los algoritmos basados puramente en gradientes clásicos (como el Descenso de Gradiente) son deterministas y solo exploran puntos geográficos continuos cercanos, lo que los hace altamente propensos a quedar atrapados de por vida en cimas menores (<strong>Máximos Locales</strong>). En cambio, un algoritmo genético mantiene una población dispersa y utiliza mutaciones aleatorias no locales, lo que le permite dar "saltos" geográficos a través de los valles del paisaje y escapar eficientemente de los picos falsos para continuar la búsqueda del máximo global.</p>
""",
            "challenge": {
                "prompt": "¿Qué ventaja conceptual clave posee un Algoritmo Genético frente a los métodos de gradiente clásicos al buscar soluciones en paisajes de fitness complejos?",
                "choices": ["A) Que siempre encuentra la solución exacta de forma analítica en una sola iteración.", "B) Que su población dispersa y mutaciones aleatorias le permiten saltar valles y escapar de máximos locales falsos.", "C) Que elimina por completo el uso de números reales en el plano."],
                "correct_index": 1,
                "feedback": "Incorrecto. La naturaleza probabilística y poblacional de los AG les otorga robustez global contra máximos locales falsos."
            }
        },
        {
            "order": 6,
            "title": "[BASICO] Taller Fitness",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Codificación y Evaluación del Máximo Matemático</h3>
<p>En este laboratorio programamos una función de aptitud para resolver un problema de optimización numérica clásica: maximizar el valor de la función polinomial compleja $f(x) = x \sin(10 \pi x) + 1$ sobre el intervalo real $[-1, 2]$.</p>
<p>Implementando los pasos en Python:</p>
<ol>
    <li>Codificamos el valor continuo de $x$ utilizando un cromosoma binario de 22 bits.</li>
    <li>Decodificamos el cromosoma mapeando la cadena de bits binaria de vuelta al rango continuo $[-1, 2]$.</li>
    <li>Evaluamos la aptitud del fenotipo resultante de forma directa mediante la función matemática $f(x)$.</li>
    <li>Observamos un paisaje de aptitud sumamente escarpado lleno de valles oscilantes y picos agudos, ideal para probar la potencia de los algoritmos evolutivos.</li>
</ol>
""",
            "challenge": {
                "prompt": "En nuestro taller de optimización numérica, ¿cuál es el propósito de decodificar el cromosoma de 22 bits en el rango [-1, 2]?",
                "choices": ["A) Para acelerar el entrenamiento en sistemas expertos.", "B) Para convertir el genotipo binario compacto en su fenotipo (número real continuo) y poder calcular su aptitud real.", "C) Para anular la varianza de la homocedasticidad residual."],
                "correct_index": 1,
                "feedback": "Incorrecto. La decodificación mapea la codificación binaria interna (genotipo) al espacio físico del problema (fenotipo)."
            }
        },
        {
            "order": 7,
            "title": "[INTERMEDIO] Operador de Seleccin",
            "section_type": "explicacion",
            "content": """
<h3>Operadores de Selección: La Presión Selectiva</h3>
<p>El operador de <strong>Selección</strong> tiene como misión fundamental imitar la presión evolutiva del darwinismo natural: seleccionar a los cromosomas con mejor aptitud de la generación actual para actuar como padres de la siguiente generación.</p>
<p>Los métodos de selección más influyentes en los algoritmos genéticos son:</p>
<ol>
    <li><strong>Selección de Ruleta (Proporcional):</strong> A cada individuo se le asigna una probabilidad de selección proporcional a su fitness. Matemáticamente, la probabilidad de selección del individuo $i$ se define como:
        $$P(i) = \frac{\text{Fitness}_i}{\sum_{j=1}^{N} \text{Fitness}_j}$$
        Graficamente, funciona como una ruleta de casino donde los individuos con mejor aptitud ocupan los sectores circulares más grandes, manteniendo una oportunidad para que especímenes débiles sobrevivan y aporten diversidad.
    </li>
    <li><strong>Selección de Torneo:</strong> Se eligen aleatoriamente $k$ individuos de la población y el que posea mejor fitness gana el derecho a reproducirse de forma absoluta. Es muy popular por su facilidad de implementación y eficiencia.
    </li>
</ol>
""",
            "challenge": {
                "prompt": "En el operador de Selección de Ruleta, ¿cómo se determina la probabilidad de que un cromosoma individual sea elegido como padre reproductivo?",
                "choices": ["A) Todos los individuos poseen exactamente la misma probabilidad aleatoria uniforme.", "B) De forma proporcional a su valor de fitness individual frente a la sumatoria total de fitness de la población.", "C) Seleccionando únicamente al peor individuo para incentivar su mutación extrema."],
                "correct_index": 1,
                "feedback": "Incorrecto. En la Ruleta, la probabilidad es directamente proporcional a la fracción del fitness del individuo sobre el total."
            }
        },
        {
            "order": 8,
            "title": "[INTERMEDIO] Cruce (Crossover)",
            "section_type": "explicacion",
            "content": """
<h3>El Operador de Cruce (Crossover): Explotación Genética</h3>
<p>El <strong>Cruce (Crossover)</strong> es el operador genético principal encargado del proceso de **Explotación** en el espacio de búsqueda. Su objetivo es combinar el material genético de dos padres seleccionados de alta aptitud para producir hijos descendientes que hereden sus mejores características.</p>
<p>El método clásico es el <strong>Cruce de un Solo Punto (Single-Point Crossover)</strong>. El proceso fluye de la siguiente forma:</p>
<ol>
    <li>Se elige probabilísticamente un punto de corte aleatorio a lo largo del cromosoma (por ejemplo, entre el tercer y cuarto gen).</li>
    <li>El Hijo 1 hereda los genes del Padre 1 que están antes de la línea de corte, y los genes del Padre 2 que están después de la línea de corte.</li>
    <li>El Hijo 2 se genera a la inversa, combinando la porción inicial del Padre 2 con la porción terminal del Padre 1.</li>
</ol>
<p>Este intercambio físico estructurado permite consolidar "bloques constructivos de alta aptitud", logrando que la descendencia supere el desempeño de sus progenitores.</p>
""",
            "challenge": {
                "prompt": "¿Cómo se estructuran las soluciones descendientes al aplicar el operador de Cruce de un Solo Punto?",
                "choices": ["A) Mutando aleatoriamente el 100% de los bits del primer padre.", "B) Dividiendo los cromosomas de los padres por un punto de corte aleatorio e intercambiando de forma cruzada sus segmentos genéticos.", "C) Promediando aritméticamente las matrices de covarianzas de entrada."],
                "correct_index": 1,
                "feedback": "Incorrecto. El cruce fragmenta y recombina de forma alternada la información genotípica de ambos progenitores."
            }
        },
        {
            "order": 9,
            "title": "[INTERMEDIO] Taller Cruce",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Recombinación de Bloques Genéticos</h3>
<p>En este taller práctico programamos el operador de cruce de un solo punto en Python. Evaluamos la recombinación cromosómica utilizando dos padres binarios de longitud 8:</p>
<ul>
    <li>Padre 1: <code>[1, 1, 1, 1, 0, 0, 0, 0]</code></li>
    <li>Padre 2: <code>[0, 0, 0, 0, 1, 1, 1, 1]</code></li>
</ul>
<p>Fijando de forma didáctica la línea de corte en el índice 4 (mitad del cromosoma), programamos el cruce y obtenemos:</p>
<ul>
    <li>Hijo 1: <code>[1, 1, 1, 1, 1, 1, 1, 1]</code></li>
    <li>Hijo 2: <code>[0, 0, 0, 0, 0, 0, 0, 0]</code></li>
</ul>
<p>Validamos que el Hijo 1 consolidó de forma exitosa los bloques activos más aptos de ambos padres en un único cromosoma óptimo densamente poblado de alelos dominantes.</p>
""",
            "challenge": {
                "prompt": "Dados los padres P1 = [1,1,1,1,0,0,0,0] y P2 = [0,0,0,0,1,1,1,1], ¿qué hijo hereda los mejores bloques si cruzamos exactamente en el cuarto índice?",
                "choices": ["A) El Hijo con la secuencia [0, 0, 0, 0, 0, 0, 0, 0]", "B) El Hijo con la secuencia [1, 1, 1, 1, 1, 1, 1, 1]", "C) Ninguno, se genera una secuencia vacía de error de bits."],
                "correct_index": 1,
                "feedback": "Incorrecto. El cruzamiento en el cuarto índice combina la primera mitad de P1 ([1,1,1,1]) con la segunda de P2 ([1,1,1,1]), dando [1,1,1,1,1,1,1,1]."
            }
        },
        {
            "order": 10,
            "title": "[INTERMEDIO] Mutación",
            "section_type": "explicacion",
            "content": """
<h3>El Operador de Mutación: Exploración Genética</h3>
<p>Mientras que el cruce se encarga de explotar la información existente, el operador de <strong>Mutación</strong> tiene como misión fundamental la **Exploración** del espacio de búsqueda. Su objetivo es inyectar diversidad genética y prevenir que la población se estanque en óptimos locales.</p>
<p>En el caso clásico de cromosomas binarios, implementamos la <strong>Mutación por Inversión de Bit (Bit Flip Mutation)</strong>. Consiste en recorrer gen por gen cada cromosoma de la población y, con una probabilidad muy baja definida por la **Tasa de Mutación ($p_m$)**, invertir su valor lógico (cambiar un 0 por un 1, o un 1 por un 0).</p>
<p>El ajuste de la tasa de mutación ($p_m$) exige una calibración de precisión extrema:</p>
<ul>
    <li>Si la tasa de mutación es <strong>demasiado pequeña</strong>, el algoritmo será incapaz de escapar de óptimos locales al no generar nuevos alelos.</li>
    <li>Si es <strong>demasiado grande (por ejemplo, del 100%)</strong>, el algoritmo genético perderá toda memoria selectiva y degenerará en una ineficiente <strong>Búsqueda Aleatoria Pura (Random Search)</strong>, destruyendo los bloques constructivos óptimos heredados por el cruce.</li>
</ul>
""",
            "challenge": {
                "prompt": "¿Qué consecuencia destructiva ocurre en un algoritmo genético si fijamos una Tasa de Mutación (pm) extremadamente alta del 100%?",
                "choices": ["A) El algoritmo converge al óptimo global de manera instantánea y libre de errores.", "B) El algoritmo pierde la memoria selectiva e histórica y degenera en una ineficiente Búsqueda Aleatoria Pura.", "C) Se cancela por completo el operador reproductivo de cruce."],
                "correct_index": 1,
                "feedback": "Incorrecto. Una tasa de mutación excesivamente alta destruye el conocimiento acumulado en los genes más aptos de la población."
            }
        },
        {
            "order": 11,
            "title": "[INTERMEDIO] Elitismo",
            "section_type": "explicacion",
            "content": """
<h3>El Operador de Elitismo: Conservación Óptima</h3>
<p>Dado que los operadores de selección, cruce y mutación son inherentemente probabilísticos, siempre existe el riesgo latente de que el individuo óptimo de una generación (aquel que posee el mejor valor de fitness histórico) sea destruido o alterado negativamente, perdiéndose sus genes excepcionales.</p>
<p>Para contrarrestar esto, los ingenieros implementan el <strong>Elitismo</strong>.</p>
<p>El Elitismo consiste en **copiar o clonar intactos a los mejores individuos** de la generación actual de forma directa y prioritaria a la siguiente generación, protegiéndolos de los operadores de cruce y mutación.</p>
<p>El gran aporte matemático del elitismo es que <strong>garantiza que la aptitud máxima de la población sea estrictamente no decreciente</strong> a lo largo de las generaciones. Esto acelera drásticamente la tasa de convergencia del sistema al resguardar en todo momento el avance genético óptimo alcanzado por la población.</p>
""",
            "challenge": {
                "prompt": "¿Cuál es el principal beneficio matemático que aporta implementar el Elitismo en un Algoritmo Genético?",
                "choices": ["A) Aumentar drásticamente el tamaño del pool cromosómico inicial.", "B) Garantizar que la aptitud (fitness) máxima de la población sea estrictamente no decreciente a lo largo de las generaciones.", "C) Eliminar por completo el operador probabilístico de selección."],
                "correct_index": 1,
                "feedback": "Incorrecto. El elitismo resguarda al individuo más apto, garantizando que el mejor fitness evolutivo sea monótono no decreciente."
            }
        },
        {
            "order": 12,
            "title": "[INTERMEDIO] Taller Ciclo Completo",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Integración del Ciclo Evolutivo Completo</h3>
<p>En este laboratorio práctico integramos en un único script de Python el ciclo de vida evolutivo completo: inicializamos una población aleatoria, calculamos el fitness de los candidatos, aplicamos selección de ruleta, realizamos el cruce de un solo punto, ejecutamos la mutación de bits por inversión e implementamos elitismo estricto conservando al mejor candidato intacto.</p>
<p>Al ejecutar la simulación a lo largo de $100$ generaciones:</p>
<ol>
    <li>Monitoreamos cómo la aptitud promedio de la población se eleva de forma constante generación tras generación.</li>
    <li>Gracias al elitismo, la aptitud máxima avanza de manera constante y libre de caídas.</li>
    <li>La población converge finalmente de manera unificada hacia el óptimo global del problema matemático, demostrando la alta efectividad del ciclo evolutivo integrado.</li>
</ol>
""",
            "challenge": {
                "prompt": "Al integrar todos los operadores evolutivos en el taller práctico, ¿qué comportamiento se observa en el fitness promedio de la población a través de las generaciones?",
                "choices": ["A) Se reduce a cero de forma drástica e irreversible.", "B) Incrementa y se estabiliza de forma constante a lo largo del tiempo debido a la presión selectiva.", "C) Oscila violentamente de forma aleatoria infinita sin convergencia."],
                "correct_index": 1,
                "feedback": "Incorrecto. La combinación coordinada de selección, cruce, mutación y elitismo eleva la aptitud promedio del pool genético hacia el óptimo."
            }
        },
        {
            "order": 13,
            "title": "[AVANZADO] Problema del Viajero",
            "section_type": "explicacion",
            "content": """
<h3>El Problema del Viajante de Comercio (TSP)</h3>
<p>El <strong>Problema del Viajante de Comercio (TSP - Traveling Salesperson Problem)</strong> es uno de los problemas de optimización combinatoria **NP-hard** más célebres de la computación. Consiste en encontrar la ruta óptima más corta que permita a un vendedor visitar un conjunto de $n$ ciudades exactamente una sola vez y retornar al origen.</p>
<p>Si intentamos usar una codificación binaria clásica para resolver el TSP, nos toparemos con un escollo metodológico grave. En el TSP, una solución válida debe representarse como un <strong>Cromosoma de Permutación</strong> (por ejemplo, el orden de ciudades $[1, 3, 2, 4]$).</p>
<p>Si aplicamos el operador de cruce de un solo punto clásico sobre estos cromosomas de permutación, la descendencia resultante heredará alelos duplicados (por ejemplo, un hijo $[1, 3, 3, 4]$ y otro $[1, 2, 2, 4]$), lo que representa **rutas inválidas** (ciudades no visitadas o visitadas dos veces).</p>
<p>Para resolver esto sin colapsar el sistema, los científicos desarrollaron codificaciones de orden especializadas y operadores de recombinación permutacionales no destructivos.</p>
""",
            "challenge": {
                "prompt": "¿Por qué los operadores de Cruce clásicos (como el cruce de un solo punto) fallan al aplicarse en problemas como el TSP?",
                "choices": ["A) Porque requieren transformarse en redes neuronales profundas.", "B) Porque producen cromosomas inválidos con rutas que contienen ciudades duplicadas o ausentes al no respetar la permutación.", "C) Porque desactivan por completo el cálculo de la función fitness."],
                "correct_index": 1,
                "feedback": "Incorrecto. Los cruces clásicos cortan a ciegas las posiciones, destruyendo la naturaleza permutacional exigida en el TSP."
            }
        },
        {
            "order": 14,
            "title": "[AVANZADO] Cruce de Orden (OX)",
            "section_type": "explicacion",
            "content": """
<h3>El Operador de Cruce de Orden (OX - Order Crossover)</h3>
<p>Para solucionar la generación de soluciones inválidas en problemas combinatorios permutacionales como el TSP, los científicos diseñaron el <strong>Cruce de Orden (OX - Order Crossover)</strong>. El operador OX garantiza la conservación de secuencias y el orden relativo de las ciudades sin generar duplicados.</p>
<p>El flujo del algoritmo Cruce OX para generar al Hijo 1 opera de la siguiente forma:</p>
<ol>
    <li>Se seleccionan aleatoriamente dos puntos de corte sobre los padres (creando un segmento central).</li>
    <li>Se copia intacto el segmento central del Padre 1 directamente en la misma posición central del Hijo 1.</li>
    <li>Comenzando desde el segundo punto de corte, se recorren en orden circular las ciudades del Padre 2.</li>
    <li>Se rellenan las posiciones vacías restantes del Hijo 1 con estas ciudades del Padre 2, <strong>omitiendo aquellas que ya se encuentren presentes en el segmento central heredado del Padre 1</strong>.</li>
</ol>
<p>Este ingenioso flujo garantiza de forma determinista que cada ciudad sea visitada exactamente una vez en la ruta descendiente.</p>
""",
            "challenge": {
                "prompt": "¿Cómo soluciona el operador de Cruce de Orden (OX) la invalidez de rutas al generar la descendencia?",
                "choices": ["A) Añadiendo variables dummy a las ciudades visitadas.", "B) Heredando un segmento central intacto de un padre y rellenando las posiciones restantes con las ciudades del otro padre sin duplicar elementos ya existentes.", "C) Cancelando por completo la presión selectiva del torneo."],
                "correct_index": 1,
                "feedback": "Incorrecto. Al omitir las ciudades ya presentes en el segmento heredado, OX previene duplicados y asegura permutaciones válidas."
            }
        },
        {
            "order": 15,
            "title": "[AVANZADO] Taller Rutas",
            "section_type": "demo",
            "content": """
<h3>Taller Práctico: Resolviendo el TSP con Cruce OX</h3>
<p>En este laboratorio programamos el operador de Cruce de Orden (OX) en Python para optimizar una ruta de despacho logístico que recorre $8$ ciudades distintas.</p>
<p>Simulando la recombinación de rutas con dos padres ordenados:</p>
<ul>
    <li>Padre 1: <code>[1, 2, 3, 4, 5, 6, 7, 8]</code></li>
    <li>Padre 2: <code>[8, 7, 4, 1, 2, 3, 5, 6]</code></li>
</ul>
<p>Fijando los cortes entre las posiciones 2-3 y 5-6:</p>
<ol>
    <li>Heredamos el segmento central del Padre 1: <code>[x, x, 3, 4, 5, x, x, x]</code>.</li>
    <li>Rellenamos de forma circular con las ciudades restantes del Padre 2 omitiendo duplicados.</li>
    <li>Obtenemos una ruta descendiente válida e intacta sin duplicación alguna.</li>
    <li>El modelo evolutivo converge exitosamente hacia la ruta con el menor kilometraje de viaje acumulado.</li>
</ol>
""",
            "challenge": {
                "prompt": "En nuestro taller de TSP con Cruce OX, ¿cuál es el resultado de la recombinación con corte central en el Hijo 1?",
                "choices": ["A) Una ruta de despacho válida que contiene exactamente una copia de cada una de las 8 ciudades.", "B) Un vector de bits binarios densos repleto de ceros.", "C) Un error de ejecución por redundancia de alelos repetidos."],
                "correct_index": 0,
                "feedback": "Incorrecto. El Cruce OX entrega un cromosoma de permutación estructuralmente válido con todas las ciudades únicas."
            }
        },
        {
            "order": 16,
            "title": "[AVANZADO] Inteligencia de Enjambre",
            "section_type": "explicacion",
            "content": """
<h3>Fundamentos de la Inteligencia de Enjambre (Swarm Intelligence)</h3>
<p>Los algoritmos evolutivos compartieron escenario con otra gran rama de la optimización metaheurística bio-inspirada conocida como <strong>Inteligencia de Enjambre (Swarm Intelligence)</strong>.</p>
<p>La Inteligencia de Enjambre modela el comportamiento colectivo coordinado y descentralizado de sistemas autoorganizados (como bandadas de aves en vuelo continuo o colonias de hormigas en busca de alimentos).</p>
<p>A diferencia del darwinismo clásico donde los peores mueren, en los sistemas de enjambre **ningún individuo es sacrificado**. En cambio, el grupo está compuesto por agentes simples que interactúan de forma cooperativa entre sí y con su entorno local. La inteligencia surge de forma emergente a partir de la comunicación y el intercambio social continuo de información de éxito de coordenadas, logrando que el colectivo resuelva problemas de optimización multidimensional de extrema complejidad matemática.</p>
""",
            "challenge": {
                "prompt": "¿Cuál es la característica principal de los algoritmos de Inteligencia de Enjambre a diferencia del darwinismo digital clásico?",
                "choices": ["A) Se elimina por completo el uso de computadoras en la optimización.", "B) Ningún agente o individuo del grupo es sacrificado; la solución surge de la comunicación cooperativa y social continua entre los miembros.", "C) Todos los agentes son reiniciados de forma aleatoria en cada iteración."],
                "correct_index": 1,
                "feedback": "Incorrecto. En los enjambres, el aprendizaje colectivo cooperativo sustituye a la selección de muerte/supervivencia darwiniana."
            }
        },
        {
            "order": 17,
            "title": "[AVANZADO] PSO en Accin",
            "section_type": "explicacion",
            "content": """
<h3>Algoritmo de Optimización por Enjambre de Partículas (PSO)</h3>
<p>Presentado por James Kennedy y Russell Eberhart en 1995, la <strong>Optimización por Enjambre de Partículas (PSO - Particle Swarm Optimization)</strong> es el algoritmo líder de la Inteligencia de Enjambre para optimizar espacios continuos.</p>
<p>En el algoritmo PSO, cada candidato se modela como una **partícula (un punto con masa nula que vuela en un espacio tridimensional o multidimensional)**. Cada partícula $i$ posee una posición actual $\mathbf{x}_i$ y un vector de velocidad de vuelo $\mathbf{v}_i$. En cada iteración, la partícula actualiza su velocidad y posición utilizando dos ecuaciones fundamentales:</p>
<p>$$\mathbf{v}_i^{(t+1)} = w \mathbf{v}_i^{(t)} + c_1 r_1 (\mathbf{p}_i - \mathbf{x}_i^{(t)}) + c_2 r_2 (\mathbf{g} - \mathbf{x}_i^{(t)})$$</p>
<p>$$\mathbf{x}_i^{(t+1)} = \mathbf{x}_i^{(t)} + \mathbf{v}_i^{(t+1)}$$</p>
<p>Donde los coeficientes de las ecuaciones representan:</p>
<ul>
    <li><strong>$w$ (Inercia):</strong> Peso físico que conserva la dirección del vector de vuelo actual.</li>
    <li><strong>$c_1$ (Coeficiente Cognitivo) y $\mathbf{p}_i$:</strong> Peso de aprendizaje individual que atrae a la partícula hacia la mejor posición que ella misma ha visitado en el historial de su vuelo.</li>
    <li><strong>$c_2$ (Coeficiente Social) y $\mathbf{g}$:</strong> Peso de aprendizaje colectivo que atrae a la partícula hacia la mejor coordenada de éxito absoluto conquistada por cualquier miembro del enjambre entero.</li>
    <li><strong>$r_1, r_2$:</strong> Números aleatorios uniformes independientes en el rango $[0, 1]$ que inyectan estocasticidad exploratoria.</li>
</ul>
""",
            "challenge": {
                "prompt": "En la ecuación de velocidad del algoritmo PSO, ¿qué componente describe la atracción de una partícula hacia la mejor posición lograda por el enjambre entero?",
                "choices": ["A) Coeficiente Cognitivo (c1)", "B) Coeficiente de Inercia física (w)", "C) Coeficiente Social colectivo (c2)"],
                "correct_index": 2,
                "feedback": "Incorrecto. El coeficiente social (c2) pondera la atracción hacia el mejor punto global (g) alcanzado por todo el colectivo."
            }
        },
        {
            "order": 18,
            "title": "[AVANZADO] Proyecto Bio-IA",
            "section_type": "demo",
            "content": """
<h3>Proyecto Final Bio-IA: Optimización de Diseño Estructural</h3>
<p>En este laboratorio final integrador consolidamos el estudio evolutivo y de enjambres. Diseñamos un script completo en Python para optimizar la geometría de un puente colgante, minimizando el peso de las vigas estructurales sin comprometer su tolerancia al peso de carga.</p>
<p>El pipeline del proyecto final requiere:</p>
<ol>
    <li>Definir el espacio geométrico de parámetros continuos para las vigas.</li>
    <li>Ajustar una función de aptitud con penalizaciones drásticas ante fallas por deformación estructural.</li>
    <li>Implementar una simulación de vuelo continuo mediante optimización por Enjambre de Partículas (PSO).</li>
    <li>Configurar los pesos de inercia ($w$), cognitivo ($c_1$) y social ($c_2$) para guiar el enjambre hacia la convergencia estable.</li>
    <li>Visualizar la convergencia de la aptitud óptima a lo largo de las iteraciones.</li>
</ol>
<p>Sube tu archivo entregable (.ipynb o reporte de optimización con el vector de coordenadas óptimas) para ser calificado por el instructor.</p>
""",
            "challenge": {
                "prompt": "¿Qué proceso integrador se consolida en el Proyecto Final de Algoritmos Genéticos y Bio-IA?",
                "choices": ["A) Solo se exporta un gráfico sin validación de código.", "B) El modelado geométrico de vigas, formulación de fitness con penalizaciones estructurales, y optimización continua adaptativa mediante Enjambre de Partículas (PSO).", "C) La regresión polinomial OLS con variables categóricas dummy binarias."],
                "correct_index": 1,
                "feedback": "Incorrecto. El proyecto final consolida la aplicación integrada de optimización bio-inspirada robusta combinando fitness restrictivo y control cooperativo PSO."
            }
        }
    ]
}

# Clear any existing InteractiveChallenge objects to clean-up
InteractiveChallenge.objects.all().delete()
print("Cleaned up existing InteractiveChallenges.")

# Overwrite / Populate
for course_id, lessons_list in data.items():
    try:
        course = Course.objects.get(id=course_id)
        print(f"\nProcessing Course: {course.title} (ID: {course_id})")
    except Course.DoesNotExist:
        print(f"Error: Course ID {course_id} does not exist!")
        continue

    for les_data in lessons_list:
        order = les_data["order"]
        title = les_data["title"]
        section_type = les_data["section_type"]
        content_html = les_data["content"]
        chal_data = les_data["challenge"]

        # Find or create CourseContent
        lesson, created = CourseContent.objects.update_or_create(
            course=course,
            order=order,
            title=title,
            defaults={
                "section_type": section_type,
                "content": content_html.strip()
            }
        )
        status_str = "Created" if created else "Updated"
        print(f"  {status_str} Lesson: {title} (Order: {order})")

        # Create corresponding InteractiveChallenge
        challenge = InteractiveChallenge.objects.create(
            content=lesson,
            prompt=chal_data["prompt"],
            choices_json=json.dumps(chal_data["choices"], ensure_ascii=False),
            correct_index=chal_data["correct_index"],
            feedback=chal_data["feedback"]
        )
        print(f"    -> Created Challenge ID: {challenge.id} for Lesson: {lesson.title}")

print("\nSUCCESS: SUCCESSFULLY POPULATED 54 ENRICHED LESSONS AND 54 LESSON-SPECIFIC INTERACTIVE CHALLENGES!")
