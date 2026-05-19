import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_project.settings')
django.setup()

from enrollment.models import Course, CourseContent

def run():
    print("Iniciando purga de lecciones existentes...")
    CourseContent.objects.all().delete()
    print("Purga completada exitosamente.")

    courses_info = [
        {
            'id': 4,
            'title': 'IA y Machine Learning Academy',
            'lessons': [
                # BASICO
                ('Historia de la IA', 'explicacion', 
                 '<h3>Fundamentos Históricos y Evolución Conceptual de la Inteligencia Artificial</h3>'
                 '<p>La Inteligencia Artificial (IA) no es una disciplina moderna de computación, sino el resultado de siglos de evolución filosófica y matemática. El paradigma comenzó formalmente en 1956 durante la legendaria <strong>Conferencia de Dartmouth</strong> organizada por John McCarthy, Marvin Minsky, Nathaniel Rochester y Claude Shannon. En este hito fundacional, se acuñó el término oficial y se planteó la conjetura de que todo aspecto del aprendizaje o cualquier otra característica de la inteligencia puede ser en principio descrito con tanta precisión que una máquina pueda ser construida para simularlo.</p>'
                 '<h4>El Paradigma Simbólico vs Conexionista</h4>'
                 '<p>A lo largo de los años, la IA se dividió en dos grandes corrientes:</p>'
                 '<ul>'
                 '  <li><strong>IA Simbólica (Top-Down):</strong> Basada en la manipulación formal de símbolos y reglas lógicas. Se argumentaba que el pensamiento racional consistía en aplicar reglas inferenciales sobre hechos estructurados.</li>'
                 '  <li><strong>IA Conexionista (Bottom-Up):</strong> Basada en la emulación de la estructura biológica del cerebro, utilizando neuronas artificiales interconectadas que aprenden a partir de la experiencia y los datos estadísticos.</li>'
                 '</ul>'
                 '<p>Este curso abordará el auge y la convergencia de ambos enfoques, analizando los llamados "Inviernos de la IA" ocurridos en las décadas de 1970 y 1980 debido a limitaciones de hardware y sobreexpectativas, y su renacimiento contemporáneo gracias al Big Data y las unidades de procesamiento gráfico aceleradas (GPUs).</p>'),
                
                ('El Test de Turing', 'explicacion',
                 '<h3>El Juego de la Imitación de Alan Turing: Fundamentos y Límites de la Cognición Artificial</h3>'
                 '<p>En su trascendental artículo de 1950 titulado <em>"Computing Machinery and Intelligence"</em>, el matemático británico Alan Turing formuló la famosa pregunta: <strong>"¿Pueden pensar las máquinas?"</strong>. Ante la dificultad metafísica de definir qué es el pensamiento o la conciencia, Turing propuso un desvío conductista y operativo: el <strong>Juego de la Imitación</strong>, conocido hoy en día como el <strong>Test de Turing</strong>.</p>'
                 '<h4>Dinámica del Protocolo de Evaluación</h4>'
                 '<p>El test se realiza mediante un protocolo ciego:</p>'
                 '<ol>'
                 '  <li>Un evaluador humano se comunica a través de terminales de texto neutro con dos entidades en salas separadas: otro ser humano y una máquina de cómputo.</li>'
                 '  <li>El evaluador tiene libertad absoluta de realizar cualquier clase de pregunta: desde problemas lógicos hasta reflexiones poéticas o dudas existenciales.</li>'
                 '  <li>Si al cabo de un período determinado (por ejemplo, 5 minutos de interacción libre), el evaluador es incapaz de discriminar con fiabilidad estadística cuál de los dos interlocutores es el sistema artificial, la máquina aprueba el test de Turing.</li>'
                 '</ol>'
                 '<p>A pesar de su elegancia conductista, el test ha recibido críticas monumentales, entre ellas el célebre experimento mental de la <strong>Habitación China de John Searle</strong>. Searle demostró que la manipulación puramente sintáctica de símbolos no presupone en ningún caso comprensión semántica, redefiniendo las diferencias conceptuales fundamentales entre una <em>IA Débil</em> y una <em>IA Fuerte</em>.</p>'),
                
                ('Clasificación Base', 'demo',
                 '<h3>Laboratorio Experimental: Fundamentos de la Clasificación de Información</h3>'
                 '<p>La clasificación constituye uno de los pilares del aprendizaje automático supervisado. En esencia, consiste en asignar una etiqueta categórica discreta $y$ a un vector de entrada continuo o categórico $\mathbf{x} = [x_1, x_2, \dots, x_n]$. A nivel geométrico, los algoritmos de clasificación buscan construir límites de decisión (hiperplanos o superficies complejas) capaces de compartimentar el espacio muestral con el mínimo margen de error.</p>'
                 '<h4>Procedimiento del Laboratorio de Datos</h4>'
                 '<p>En este laboratorio práctico de clasificación, trabajarás con un dataset clásico de variables estructuradas. Tu objetivo es estructurar y limpiar el conjunto de datos aplicando el siguiente protocolo:</p>'
                 '<pre><code># Estructura del dataset de clasificación base\n'
                 'import pandas as pd\n'
                 'data = {\n'
                 '    "id": [1, 2, 3, 4, 5],\n'
                 '    "caracteristica_1": [2.5, 1.3, 8.9, 0.4, 7.8],\n'
                 '    "caracteristica_2": [5.1, 0.2, 9.1, 1.2, 8.4],\n'
                 '    "clase_objetivo": [0, 0, 1, 0, 1]\n'
                 '}\n'
                 'df = pd.DataFrame(data)\n'
                 'print("Estructura de Datos Cargada:")\n'
                 'print(df.head())</code></pre>'
                 '<p>Sube tu notebook conteniendo la partición de datos en entrenamiento (train) y prueba (test) junto con el ploteo de dispersión en 2D donde se distinga claramente la separación lineal de las dos clases.</p>'),
                
                ('Sistemas Expertos', 'explicacion',
                 '<h3>Sistemas Expertos: Ingeniería del Conocimiento y Reglas Lógicas de Producción</h3>'
                 '<p>En los años 70 y 80, la IA Simbólica alcanzó su cénit con el desarrollo de los <strong>Sistemas Expertos</strong>. Estos programas emulan el comportamiento y la toma de decisiones de un experto humano especializado en un dominio específico. El ejemplo más histórico fue <strong>MYCIN</strong>, un sistema experto pionero diseñado para diagnosticar infecciones bacterianas de la sangre y recomendar dosis precisas de antibióticos.</p>'
                 '<h4>Arquitectura de un Sistema Experto Basado en Reglas</h4>'
                 '<p>Un sistema experto moderno consta de tres componentes nucleares:</p>'
                 '<ul>'
                 '  <li><strong>Base de Conocimientos:</strong> Conjunto estructurado de hechos y reglas de inferencia en formato declarativo, típicamente representados mediante la estructura condicional <code>IF (Antecedente) THEN (Consecuente)</code>.</li>'
                 '  <li><strong>Motor de Inferencia:</strong> El cerebro algorítmico encargado de enlazar las reglas de la base de conocimientos con los hechos ingresados por el usuario. Utiliza dos estrategias fundamentales: Enlazamiento hacia Adelante (Forward Chaining) y Enlazamiento hacia Atrás (Backward Chaining).</li>'
                 '  <li><strong>Módulo de Explicación:</strong> Sección que justifica al usuario la cadena de razonamiento y por qué se activó una regla específica.</li>'
                 '</ul>'
                 '<p>Analizaremos las limitaciones existenciales de estos sistemas, las cuales desencadenaron el segundo invierno de la IA: el "cuello de botella de la adquisición del conocimiento" y la extrema fragilidad de los sistemas lógicos puros ante inconsistencias o datos ausentes en el mundo real.</p>'),
                
                ('Lógica Difusa', 'explicacion',
                 '<h3>Lógica Difusa: Matematización de la Incertidumbre y la Vaguedad Lingüística</h3>'
                 '<p>La lógica formal clásica opera sobre valores de verdad estrictamente binarios: una proposición es verdadera (1) o falsa (0). Sin embargo, el razonamiento humano común maneja conceptos continuos y matizados: un clima no es "frío" o "caliente" de forma binaria, sino que posee un grado matizado de temperatura. En 1965, el matemático de origen azerbaiyano <strong>Lotfi A. Zadeh</strong> formuló la teoría de la <strong>Lógica Difusa (Fuzzy Logic)</strong> para formalizar esta transición gradual.</p>'
                 '<h4>Matemáticas de los Conjuntos Difusos</h4>'
                 '<p>A diferencia de los conjuntos clásicos definidos por una función característica dicotómica, un conjunto difuso $A$ se define por una <strong>función de pertenencia</strong> $\mu_A(x)$, que asigna a cada elemento del dominio un valor real continuo comprendido estrictamente en el intervalo $[0, 1]$:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\mu_A(x): X \rightarrow [0, 1]$$</p>'
                 '<p>Esto permite a las variables lingüísticas pasar suavemente por múltiples estados superpuestos (como "Frenado Suave", "Frenado Moderado" y "Frenado de Emergencia"), facilitando el control de sistemas mecánicos complejos como trenes de alta velocidad, lavadoras inteligentes o sistemas de navegación de automóviles con transiciones fluidas de control.</p>'),
                
                ('Taller Lógico', 'demo',
                 '<h3>Taller Práctico: Diseño e Implementación de un Sistema de Control Lógico Difuso</h3>'
                 '<p>En este laboratorio técnico, diseñarás e implementarás un controlador de lógica difusa utilizando Python para resolver un problema típico de ingeniería: regular la velocidad de frenado de un vehículo autónomo en base a la distancia de proximidad al coche delantero y la velocidad de aceleración actual.</p>'
                 '<h4>Pipeline de Desarrollo Requerido</h4>'
                 '<ol>'
                 '  <li><strong>Fuzzificación:</strong> Definir las funciones de pertenencia triangulares y trapezoidales para las variables de entrada (distancia en metros y velocidad en km/h) y de salida (presión del freno de 0% a 100%).</li>'
                 '  <li><strong>Base de Reglas Difusas:</strong> Estructurar un juego mínimo de 5 reglas lingüísticas de control (por ejemplo: <code>IF Distancia es Corta AND Velocidad es Alta THEN Presión es Máxima</code>).</li>'
                 '  <li><strong>Defuzzificación:</strong> Aplicar el método del Centroide (Centro de Gravedad) para convertir la distribución agregada difusa de salida en un valor numérico nítido y accionable de frenado.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto base para simular variables difusas\n'
                 'def calculate_fuzzy_centroid(area_distribution):\n'
                 '    # Método de integración numérica para hallar el centroide\n'
                 '    numerator = sum([x * y for x, y in area_distribution])\n'
                 '    denominator = sum([y for x, y in area_distribution])\n'
                 '    return numerator / max(1e-9, denominator)</code></pre>'
                 '<p>Entrega tu notebook completo con los gráficos correspondientes a las funciones de pertenencia y un caso de prueba donde el centroide devuelva la presión óptima de frenado.</p>'),
                
                # INTERMEDIO
                ('Perceptrón Simple', 'explicacion',
                 '<h3>El Perceptrón de Rosenblatt: La Célula Computacional Básica y el Límite de Separabilidad Lineal</h3>'
                 '<p>En 1958, el neurobiólogo Frank Rosenblatt propuso el <strong>Perceptrón</strong>, el modelo matemático formal de una neurona biológica que sentó los cimientos del conexionismo. El perceptrón simple es una unidad lineal de procesamiento que toma múltiples entradas numéricas continuas, calcula su suma ponderada agregando un término de sesgo (bias) para desplazar el origen de la frontera de decisión, y pasa el resultado a través de una función de activación no lineal de umbral (función escalón de Heaviside).</p>'
                 '<h4>Formulación Matemática y Arquitectura de Cómputo</h4>'
                 '<p>La salida del perceptrón simple se formaliza algebraicamente como:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$y = f\left( \sum_{i=1}^n w_i x_i + b \right) = f(\mathbf{w}^T \mathbf{x} + b)$$</p>'
                 '<p>Donde $\mathbf{x}$ representa el vector de entradas, $\mathbf{w}$ el vector de pesos sinápticos que controlan la fuerza de la señal, y $b$ el sesgo o umbral. La función de paso de Heaviside $f(z)$ se define como:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$f(z) = \\begin{cases} 1 & \\text{si } z \\ge 0 \\\\ 0 & \\text{si } z < 0 \\end{cases}$$</p>'
                 '<p>Aprenderemos cómo la regla de aprendizaje del perceptrón actualiza interativamente sus pesos cuando hay un error de predicción, y por qué el célebre libro de Minsky y Papert de 1969 sepultó esta tecnología al demostrar matemáticamente que el perceptrón simple es incapaz de resolver problemas no lineales simples, como la compuerta lógica XOR.</p>'),
                
                ('Compuertas Lógicas', 'explicacion',
                 '<h3>Aprendizaje de Compuertas Booleanas mediante el Perceptrón Simple</h3>'
                 '<p>Para entender de forma clara el funcionamiento interno de las neuronas artificiales, se suele estudiar su capacidad para aprender funciones lógicas booleanas clásicas como AND, OR y NAND. Dado que estas compuertas son linealmente separables en un espacio cartesiano bidimensional, es posible encontrar un único hiperplano (recta) capaz de segregar las salidas 0 y 1.</p>'
                 '<h4>Fronteras de Decisión para AND y OR</h4>'
                 '<p>Por ejemplo, para modelar la compuerta lógica AND:</p>'
                 '<table style="width:100%; border-collapse:collapse; margin:1rem 0; font-size:0.85rem; border:1px solid rgba(255,255,255,0.1);">'
                 '  <thead>'
                 '    <tr style="background:rgba(255,255,255,0.05);">'
                 '      <th style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1);">Entrada x1</th>'
                 '      <th style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1);">Entrada x2</th>'
                 '      <th style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1);">Salida Esperada y</th>'
                 '    </tr>'
                 '  </thead>'
                 '  <tbody>'
                 '    <tr><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">0</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">0</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center; color:#ff3333;">0</td></tr>'
                 '    <tr><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">0</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">1</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center; color:#ff3333;">0</td></tr>'
                 '    <tr><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">1</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">0</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center; color:#ff3333;">0</td></tr>'
                 '    <tr><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">1</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center;">1</td><td style="padding:0.5rem; border:1px solid rgba(255,255,255,0.1); text-align:center; color:#00ff80;">1</td></tr>'
                 '  </tbody>'
                 '</table>'
                 '<p>Demostraremos matemáticamente que configurando pesos como $w_1 = 1.0, w_2 = 1.0$ y un sesgo $b = -1.5$, la ecuación lineal del perceptrón $\mathbf{w}^T \mathbf{x} + b$ es negativa para los tres primeros estados e igual a $+0.5$ para el último estado, separando el espacio de forma perfecta. En cambio, para XOR no existe ninguna recta en 2D que pueda separar las clases, forzándonos a migrar a arquitecturas multicapa.</p>'),
                
                ('Tu Primera Neurona', 'demo',
                 '<h3>Taller de Programación Neural: Entrenamiento de un Perceptrón en Python</h3>'
                 '<p>En este laboratorio implementarás el bucle de entrenamiento básico de un perceptrón simple en Python utilizando el algoritmo clásico de descenso de gradiente discreto o regla de actualización de Rosenblatt.</p>'
                 '<h4>Regla de Actualización de Pesos</h4>'
                 '<p>Para cada ejemplo de entrenamiento en la época, el error se calcula como $e = y_{esperada} - y_{predicha}$. Los parámetros se actualizan según:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$w_i \\leftarrow w_i + \eta \cdot e \cdot x_i$$</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$b \\leftarrow b + \eta \cdot e$$</p>'
                 '<p>Donde $\eta$ es la tasa de aprendizaje (learning rate).</p>'
                 '<pre><code># Algoritmo de entrenamiento elemental\n'
                 'def train_perceptron(X, y, epochs=10, lr=0.1):\n'
                 '    weights = [0.0, 0.0]\n'
                 '    bias = 0.0\n'
                 '    for epoch in range(epochs):\n'
                 '        for inputs, target in zip(X, y):\n'
                 '            # Cómputo lineal\n'
                 '            z = sum([w * x for w, x in zip(weights, inputs)]) + bias\n'
                 '            pred = 1.0 if z >= 0 else 0.0\n'
                 '            error = target - pred\n'
                 '            if error != 0:\n'
                 '                weights = [w + lr * error * x for w, x in zip(weights, inputs)]\n'
                 '                bias += lr * error\n'
                 '    return weights, bias</code></pre>'
                 '<p>Entrega un informe en formato notebook con el histórico de errores por época y el hiperplano final graficado separando los puntos lógicos.</p>'),
                
                ('Redes Multicapa', 'explicacion',
                 '<h3>Redes Neuronales Multicapa (Perceptrón Multicapa - MLP) y Representación Universal</h3>'
                 '<p>Para resolver fronteras de decisión no lineales complejas, es preciso apilar perceptrones individuales en múltiples capas ordenadas de procesamiento, estructurando el denominado <strong>Perceptrón Multicapa (MLP)</strong>. Una red neuronal densa (Fully Connected) típica consta de una capa de entrada, una o más capas ocultas interconectadas, y una capa de salida.</p>'
                 '<h4>El Teorema de Aproximación Universal</h4>'
                 '<p>La adición de capas ocultas dota al sistema de propiedades sorprendentes formalizadas por Kurt Hornik y George Cybenko en el <strong>Teorema de Aproximación Universal</strong>:</p>'
                 '<blockquote>Una red neuronal prealimentada con una única capa oculta que contenga un número finito de neuronas y funciones de activación continuas y no lineales, puede aproximar cualquier función matemática continua en subconjuntos compactos de $\mathbb{R}^n$ con cualquier precisión deseada.</blockquote>'
                 '<p>Esta capacidad de transformar espacios cartesianos se debe al hecho de que cada capa oculta actúa como un extractor de características no lineales, doblando y estirando el espacio de características original para que la capa final pueda trazar un hiperplano simple y separar los datos.</p>'),
                
                ('Funciones Activación', 'explicacion',
                 '<h3>Funciones de Activación: No-Linealidad y el Flujo de Gradiente en Capas Ocultas</h3>'
                 '<p>Si una red neuronal no tuviera funciones de activación entre sus capas, la composición sucesiva de capas lineales no sería más que una única gran transformación lineal (la composición de operadores lineales es lineal). Para dotar de expresividad no lineal a la red, aplicamos transformaciones no lineales denominadas <strong>Funciones de Activación</strong>.</p>'
                 '<h4>Fórmulas Matemáticas de Funciones Clave</h4>'
                 '<ul>'
                 '  <li><strong>Sigmoide:</strong> Transforma cualquier valor continuo al intervalo probabilístico $[0, 1]$. Es ideal para capas de salida de clasificación binaria.'
                 '      <p style="color:var(--neon-blue);">$$\sigma(z) = \\frac{1}{1 + e^{-z}}$$</p>'
                 '  </li>'
                 '  <li><strong>Relu (Rectified Linear Unit):</strong> La función más utilizada en redes convolucionales y profundas por su simplicidad y velocidad computacional. Evita el desvanecimiento de gradiente para valores positivos.'
                 '      <p style="color:var(--neon-blue);">$$f(z) = \max(0, z)$$</p>'
                 '  </li>'
                 '  <li><strong>Tangente Hiperbólica (tanh):</strong> Escala los valores al rango $[-1, 1]$, logrando salidas centradas en cero.'
                 '      <p style="color:var(--neon-blue);">$$\\tanh(z) = \\frac{e^z - e^{-z}}{e^z + e^{-z}}$$</p>'
                 '  </li>'
                 '</ul>'
                 '<p>Analizaremos las ventajas y desventajas de cada función, detallando el problema del desvanecimiento del gradiente (vanishing gradient problem) en funciones sigmoideas y tangentes hiperbólicas a medida que apilamos muchas capas.</p>'),
                
                ('Taller Multicapa', 'demo',
                 '<h3>Taller Práctico: Construcción y Entrenamiento de una Red Multicapa Densas</h3>'
                 '<p>En esta sesión práctica, construirás y entrenarás una red neuronal de capas ocultas densas (Multi-Layer Perceptron) para clasificar un conjunto clásico no lineal, como el dataset Iris o el problema de clasificación en espiral bidimensional.</p>'
                 '<h4>Pipeline de Desarrollo</h4>'
                 '<ol>'
                 '  <li><strong>Arquitectura:</strong> Configura una arquitectura de 2 entradas, una capa oculta de 4 neuronas con activación sigmoide, y una capa de salida de 1 neurona (activación sigmoide para salida binaria).</li>'
                 '  <li><strong>Paso Forward:</strong> Codifica de forma matricial la propagación del vector de entradas a través de la matriz de pesos $\mathbf{W}^{(1)}$ de la capa oculta y la matriz de pesos $\mathbf{W}^{(2)}$ de la capa de salida.</li>'
                 '  <li><strong>Evaluación de Error:</strong> Calcula la pérdida acumulada de clasificación binaria (Binary Cross-Entropy Loss).</li>'
                 '</ol>'
                 '<pre><code># Cómputo forward vectorizado en numpy\n'
                 'import numpy as np\n'
                 'def forward_pass(X, W1, b1, W2, b2):\n'
                 '    # Capa oculta\n'
                 '    Z1 = np.dot(X, W1) + b1\n'
                 '    A1 = 1.0 / (1.0 + np.exp(-Z1))\n'
                 '    # Capa de salida\n'
                 '    Z2 = np.dot(A1, W2) + b2\n'
                 '    A2 = 1.0 / (1.0 + np.exp(-Z2))\n'
                 '    return A1, A2</code></pre>'
                 '<p>Entrega el notebook con la implementación del paso forward completo y una gráfica que muestre la frontera de decisión curva lograda al clasificar el dataset.</p>'),
                
                # AVANZADO
                ('Backpropagation', 'explicacion',
                 '<h3>El Algoritmo de Retropropagación (Backpropagation): Cálculo de Gradientes mediante Regla de la Cadena</h3>'
                 '<p>El entrenamiento de redes neuronales profundas requiere un mecanismo eficiente para calcular las derivadas de la función de coste con respecto a cada peso y sesgo de la red. Esto se logra mediante el algoritmo de <strong>Retropropagación (Backpropagation)</strong>, concebido por Paul Werbos y popularizado por Rumelhart, Hinton y Williams en 1986. Consiste en la aplicación sucesiva de la <strong>Regla de la Cadena</strong> del cálculo diferencial en un grafo de cómputo.</p>'
                 '<h4>Fundamentación Matemática del Algoritmo</h4>'
                 '<p>Para un peso $w_{ij}^{(l)}$ en la capa $l$, la derivada de la pérdida total $E$ se calcula hacia atrás partiendo de la capa de salida:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\\frac{\\partial E}{\\partial w_{ij}^{(l)}} = \\frac{\\partial E}{\\partial z_i^{(l)}} \\cdot \\frac{\\partial z_i^{(l)}}{\\partial w_{ij}^{(l)}} = \\delta_i^{(l)} \\cdot a_j^{(l-1)}$$</p>'
                 '<p>Donde el término de error retropropagado $\delta_i^{(l)}$ para una capa oculta se calcula de forma recurrente en función del error de la capa posterior $l+1$:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\\delta_i^{(l)} = \left( \\sum_k \delta_k^{(l+1)} w_{ki}^{(l+1)} \\right) \cdot f\'\left( z_i^{(l)} \right)$$</p>'
                 '<p>Esto permite actualizar todos los millones de pesos en un único paso hacia atrás (backward pass) con el mismo orden de complejidad computacional que el paso hacia adelante (forward pass), haciendo viable el aprendizaje profundo.</p>'),
                
                ('Gradient Descent', 'explicacion',
                 '<h3>Descenso del Gradiente: Optimización de Superficies de Pérdida Multidimensionales</h3>'
                 '<p>El <strong>Descenso del Gradiente (Gradient Descent)</strong> es el algoritmo básico de optimización utilizado en el entrenamiento de modelos de Machine Learning. Su objetivo es encontrar el conjunto de parámetros (pesos $\mathbf{w}$ y sesgos $b$) que minimice una función de pérdida o coste $J(\mathbf{w}, b)$, que representa el error global de predicción sobre los datos.</p>'
                 '<h4>Geometría de la Optimización</h4>'
                 '<p>El gradiente $\\nabla J(\\mathbf{w})$ es un vector que apunta en la dirección de máximo crecimiento local de la función. Por ende, para minimizar la función debemos desplazarnos exactamente en la dirección opuesta al gradiente:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\\mathbf{w} \\leftarrow \\mathbf{w} - \\eta \\nabla J(\\mathbf{w})$$</p>'
                 '<p>Donde $\\eta$ es el hiperparámetro de la <strong>Tasa de Aprendizaje (Learning Rate)</strong>. Analizaremos las variantes fundamentales del algoritmo:</p>'
                 '<ul>'
                 '  <li><strong>Batch Gradient Descent:</strong> Calcula el gradiente usando todo el dataset. Es lento y computacionalmente inviable para Big Data.</li>'
                 '  <li><strong>Stochastic Gradient Descent (SGD):</strong> Actualiza los pesos usando un único ejemplo aleatorio a la vez. Es rápido pero muy ruidoso.</li>'
                 '  <li><strong>Mini-batch Gradient Descent:</strong> El estándar industrial, que calcula el gradiente sobre un pequeño subconjunto de datos (tamaño de lote típico: 32, 64 o 128).</li>'
                 '</ul>'),
                
                ('Taller Optimización', 'demo',
                 '<h3>Taller Avanzado: Implementación de Descenso del Gradiente con Backpropagation</h3>'
                 '<p>En este laboratorio técnico, implementarás desde cero el bucle completo de entrenamiento (Forward, Backward y actualización de pesos por Descenso de Gradiente) en Python sin utilizar librerías de autodiferenciación como TensorFlow o PyTorch.</p>'
                 '<h4>Matemáticas de los Gradientes de Pérdida</h4>'
                 '<p>Para una función de pérdida por mínimos cuadrados $J = \\frac{1}{2} (y - a)^2$ y una neurona con activación sigmoide $a = \sigma(z)$:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\\frac{\\partial J}{\\partial w_i} = (a - y) \cdot a(1 - a) \cdot x_i$$</p>'
                 '<pre><code># Algoritmo de retropropagación básico para 1 neurona\n'
                 'def update_weights(x, y, w, b, lr):\n'
                 '    # Forward\n'
                 '    z = sum([wi * xi for wi, xi in zip(w, x)]) + b\n'
                 '    a = 1.0 / (1.0 + np.exp(-z))\n'
                 '    # Backpropagation de gradientes\n'
                 '    da_dz = a * (1.0 - a)\n'
                 '    dj_dw = [(a - y) * da_dz * xi for xi in x]\n'
                 '    dj_db = (a - y) * da_dz\n'
                 '    # Actualización\n'
                 '    new_w = [wi - lr * dw for wi, dw in zip(w, dj_dw)]\n'
                 '    new_b = b - lr * dj_db\n'
                 '    return new_w, new_b</code></pre>'
                 '<p>Sube tu código implementado para una red de 2 capas con el gráfico de la curva de coste convergiendo a cero a medida que transcurren las épocas.</p>'),
                
                ('Deep Learning', 'explicacion',
                 '<h3>Fundamentos de Deep Learning: Redes Convolucionales (CNN) y Visión por Computadora</h3>'
                 '<p>El **Deep Learning** o Aprendizaje Profundo surge de la capacidad de apilar decenas o cientos de capas de representación para aprender abstracciones jerárquicas complejas a partir de datos crudos (imágenes, audio, texto). En el campo de la visión artificial, la arquitectura estándar son las **Redes Neuronales Convolucionales (CNN)**, introducidas por Yann LeCun en 1989 con LeNet-5.</p>'
                 '<h4>Operadores Clave de una CNN</h4>'
                 '<ul>'
                 '  <li>**Capas Convolucionales:** Utilizan filtros (kernels) que se deslizan sobre la imagen multiplicando matricialmente valores locales para extraer características como bordes, texturas o contornos, preservando la coherencia espacial y reduciendo drásticamente los pesos mediante compartición de parámetros.</li>'
                 '  <li>**Capas de Pooling (Submuestreo):** Reducen la dimensionalidad espacial de los mapas de características (típicamente mediante Max-Pooling), introduciendo invariabilidad a pequeñas traslaciones.</li>'
                 '  <li>**Capas Densas Finales:** Reciben el vector aplanado de características de alto nivel y clasifican la imagen en la categoría correspondiente.</li>'
                 '</ul>'
                 '<p>Analizaremos cómo arquitecturas profundas icónicas (como AlexNet, VGG, ResNet) revolucionaron el estado del arte y cómo resuelven el problema del desvanecimiento del gradiente mediante conexiones de salto (residual connections).</p>'),
                
                ('Procesamiento Texto', 'explicacion',
                 '<h3>Procesamiento de Lenguaje Natural (NLP): De Representaciones Estáticas a Arquitecturas de Atención</h3>'
                 '<p>El Procesamiento de Lenguaje Natural (NLP) es el área de la IA dedicada a permitir que los ordenadores comprendan, interpreten y generen lenguaje humano. La representación del texto ha evolucionado radicalmente en la última década, pasando de enfoques puramente sintácticos a complejas estructuras semánticas.</p>'
                 '<h4>Evolución Histórica de la Codificación Semántica</h4>'
                 '<ol>'
                 '  <li>**Bolsa de Palabras (Bag of Words) / TF-IDF:** Representación basada puramente en la frecuencia de las palabras, ignorando por completo el orden sintáctico y el contexto semántico.</li>'
                 '  <li>**Word Embeddings Estáticos (Word2Vec, GloVe):** Vectores densos de baja dimensión donde palabras con significados similares se ubican en regiones cercanas en un espacio geométrico continuo (ej. el famoso vector "Rey - Hombre + Mujer = Reina").</li>'
                 '  <li>**Redes Recurrentes (RNN/LSTM):** Modelos secuenciales capaces de recordar información contextual de palabras anteriores mediante un estado interno de memoria.</li>'
                 '  <li>**Arquitectura Transformer y Atención:** Introducida en 2017 por Vaswani et al., elimina la secuencialidad permitiendo procesar todo el texto en paralelo, usando el mecanismo de Auto-Atención para sopesar la relevancia contextual de cada palabra con respecto a todas las demás.</li>'
                 '</ol>'),
                
                ('Proyecto Final IA', 'demo',
                 '<h3>Proyecto Final de Graduación: Clasificación de Imágenes MNIST en Python</h3>'
                 '<p>El proyecto de graduación de esta academia de Inteligencia Artificial consiste en la implementación y entrenamiento completo de una arquitectura de red profunda convolucional para clasificar imágenes digitales del famoso dataset **MNIST** (dígitos del 0 al 9 escritos a mano por seres humanos).</p>'
                 '<h4>Requerimientos Técnicos Obligatorios</h4>'
                 '<ul>'
                 '  <li>Carga de datos MNIST divididos en train (60,000 imágenes) y test (10,000 imágenes) normalizando las intensidades de píxeles al rango $[0, 1]$.</li>'
                 '  <li>Diseñar una arquitectura con al menos 1 capa convolucional en 2D, 1 capa de Max-Pooling, una capa de aplanado (Flatten), y una capa densa de salida con activación Softmax para 10 clases.</li>'
                 '  <li>Entrenar utilizando optimización por Descenso de Gradiente o Adam, calculando la pérdida de entropía cruzada categórica (Categorical Cross-Entropy).</li>'
                 '  <li>Entregar el informe académico con la curva de pérdida de entrenamiento y la **Matriz de Confusión** final evaluada en el conjunto de prueba para certificar una precisión mínima del 95%.</li>'
                 '</ul>'
                 '<p>Sube tu script de Python o enlace al notebook con tu arquitectura documentada e informe para evaluación por el tribunal neural.</p>'),
            ]
        },
        {
            'id': 5,
            'title': 'Regresión Lineal Predictiva',
            'lessons': [
                # BASICO
                ('Estadística Predictiva', 'explicacion',
                 '<h3>Fundamentos de Estadística Descriptiva para Modelado de Datos Continuos</h3>'
                 '<p>Antes de estructurar modelos de predicción complejos, es estrictamente obligatorio entender la naturaleza matemática de las distribuciones de datos continuos. La estadística predictiva se sustenta en tres métricas descriptivas iniciales que cuantifican la tendencia central y la dispersión de una muestra o población: la Media Aritmética, la Varianza y la Desviación Estándar.</p>'
                 '<h4>Fórmulas Matemáticas de Dispersión</h4>'
                 '<p>Dada una muestra de $N$ observaciones continuas $X = \{x_1, x_2, \dots, x_N\}$:</p>'
                 '<ul>'
                 '  <li><strong>Media Aritmética ($\mu$ o $\\bar{x}$):</strong> El promedio central de los valores.'
                 '      <p style="color:var(--neon-purple);">$$\\bar{x} = \\frac{1}{N} \\sum_{i=1}^N x_i$$</p>'
                 '  </li>'
                 '  <li><strong>Varianza Muestral ($s^2$ o $\sigma^2$):</strong> Cuantifica la dispersión cuadrática promedio de los datos con respecto a su valor de tendencia central.'
                 '      <p style="color:var(--neon-purple);">$$s^2 = \\frac{1}{N-1} \\sum_{i=1}^N (x_i - \\bar{x})^2$$</p>'
                 '  </li>'
                 '  <li><strong>Desviación Estándar ($s$ o $\sigma$):</strong> Expresa la dispersión en las mismas unidades físicas que los datos originales, calculándose como la raíz cuadrada de la varianza.'
                 '      <p style="color:var(--neon-purple);">$$s = \\sqrt{s^2}$$</p>'
                 '  </li>'
                 '</ul>'
                 '<p>Comprenderemos la importancia de estas métricas al estandarizar y normalizar datos, previniendo que variables con rangos numéricos elevados dominen artificialmente los modelos de regresión lineal.</p>'),
                
                ('Covarianza', 'explicacion',
                 '<h3>La Covarianza y el Coeficiente de Correlación de Pearson: Dirección y Fuerza Lineal</h3>'
                 '<p>Cuando trabajamos con múltiples variables continuas, necesitamos cuantificar el grado de asociación y dependencia lineal entre ellas. La primera herramienta estadística para este fin es la <strong>Covarianza</strong>, que evalúa si dos variables se mueven en la misma dirección o en direcciones opuestas.</p>'
                 '<h4>Ecuación Matemática de la Covarianza Muestral</h4>'
                 '<p>Dadas dos muestras pareadas de tamaño $N$, denotadas por $X$ e $Y$:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$Cov(X, Y) = s_{xy} = \\frac{1}{N-1} \\sum_{i=1}^N (x_i - \\bar{x})(y_i - \\bar{y})$$</p>'
                 '<p>El signo del resultado determina la dirección del comportamiento conjunto:</p>'
                 '<ul>'
                 '  <li><strong>$Cov(X, Y) > 0$:</strong> Relación lineal directa. Cuando $X$ se incrementa, $Y$ tiende a incrementarse.</li>'
                 '  <li><strong>$Cov(X, Y) < 0$:</strong> Relación lineal inversa. Cuando $X$ aumenta, $Y$ disminuye.</li>'
                 '  <li><strong>$Cov(X, Y) \approx 0$:</strong> Ausencia de correlación lineal.</li>'
                 '</ul>'
                 '<p>Dado que el valor numérico de la covarianza depende de las escalas de las variables, introduciremos el <strong>Coeficiente de Correlación de Pearson ($r$)</strong>, que normaliza la covarianza dividiéndola entre las desviaciones estándar de ambas variables, acotando el resultado estrictamente en el intervalo $[-1, 1]$.</p>'),
                
                ('Taller Estadístico', 'demo',
                 '<h3>Taller de Cálculo Estadístico: Programación de Métricas Descriptivas y de Asociación</h3>'
                 '<p>En este laboratorio práctico de programación, codificarás en Python las rutinas manuales para calcular la media, varianza, covarianza y el coeficiente de correlación de Pearson a partir de un conjunto de datos estructurado en formato CSV de rendimiento académico de estudiantes.</p>'
                 '<h4>Procedimiento del Taller</h4>'
                 '<ol>'
                 '  <li>Lee el conjunto de datos de prueba y extrae los vectores de horas de estudio y notas del examen final.</li>'
                 '  <li>Codifica las funciones estadísticas puras utilizando únicamente bucles nativos de Python (sin utilizar librerías comerciales como numpy o pandas para el cálculo matemático).</li>'
                 '  <li>Interpreta el coeficiente de correlación de Pearson resultante (por ejemplo, si es $+0.85$, se establece una correlación lineal directa fuerte).</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de cálculo de correlación de Pearson\n'
                 'def pearson_correlation(x, y):\n'
                 '    mean_x, mean_y = sum(x)/len(x), sum(y)/len(y)\n'
                 '    cov = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)]) / (len(x) - 1)\n'
                 '    var_x = sum([(xi - mean_x)**2 for xi in x]) / (len(x) - 1)\n'
                 '    var_y = sum([(yi - mean_y)**2 for yi in y]) / (len(x) - 1)\n'
                 '    return cov / ((var_x * var_y) ** 0.5)</code></pre>'
                 '<p>Sube tu notebook con las funciones ejecutadas y el reporte indicando detalladamente el grado de correlación lineal de las variables.</p>'),
                
                ('Regresión Simple', 'explicacion',
                 '<h3>Regresión Lineal Simple: Modelado Predictivo Bivariado y Trazado Óptimo</h3>'
                 '<p>La <strong>Regresión Lineal Simple</strong> es un método estadístico supervisado que busca modelar la relación lineal existente entre una única variable independiente explicativa $X$ (predictora) y una variable dependiente continua $Y$ (criterio). El objetivo es trazar una recta óptima a través de la nube de puntos muestrales que permita estimar nuevos valores de $Y$ a partir de observaciones inéditas de $X$.</p>'
                 '<h4>Ecuación del Modelo Lineal Poblacional</h4>'
                 '<p>La recta teórica de regresión se modela matemáticamente como:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$Y = \beta_0 + \beta_1 X + \epsilon$$</p>'
                 '<p>Donde $\beta_0$ representa el <strong>intercepto con el eje Y</strong> (valor esperado de Y cuando X es cero), $\beta_1$ es la <strong>pendiente de la recta</strong> (cambio esperado en Y por cada unidad de incremento en X), y $\epsilon$ es el término de error aleatorio o perturbación (residuo) que absorbe la variabilidad no explicada por el modelo.</p>'
                 '<p>Estudiaremos detalladamente los supuestos fundamentales del modelo lineal clásico (homocedasticidad, normalidad de los errores, linealidad e independencia) necesarios para certificar la validez y el carácter insesgado de nuestras predicciones.</p>'),
                
                ('Minimos Cuadrados', 'explicacion',
                 '<h3>El Método de Mínimos Cuadrados Ordinarios (OLS): Deducción Analítica de Parámetros</h3>'
                 '<p>Para encontrar la recta óptima de regresión bivariada, necesitamos un criterio matemático objetivo para definir qué significa ser "la mejor línea". El método estándar es el de **Mínimos Cuadrados Ordinarios (OLS)**, desarrollado de forma independiente por Carl Friedrich Gauss y Adrien-Marie Legendre a principios del siglo XIX.</p>'
                 '<h4>Criterio de Minimización</h4>'
                 '<p>El método busca minimizar la suma de los residuos al cuadrado (SSR), es decir, la suma de las distancias verticales al cuadrado entre los puntos reales observados $y_i$ y los estimados por la recta $\hat{y}_i$:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$Minimizar \\quad S(\\beta_0, \\beta_1) = \\sum_{i=1}^N (y_i - \\hat{y}_i)^2 = \\sum_{i=1}^N (y_i - (\\beta_0 + \\beta_1 x_i))^2$$</p>'
                 '<h4>Fórmulas Analíticas de Estimación</h4>'
                 '<p>Al aplicar derivadas parciales con respecto a $\beta_0$ y $\beta_1$ e igualarlas a cero (ecuaciones normales), se deducen analíticamente las fórmulas directas para calcular los coeficientes óptimos a partir de la covarianza y la varianza muestral:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$\\hat{\\beta}_1 = \\frac{Cov(X, Y)}{Var(X)} = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2}$$</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$\\hat{\\beta}_0 = \\bar{y} - \\hat{\\beta}_1 \\bar{x}$$</p>'),
                
                ('Predicción Salarial', 'demo',
                 '<h3>Laboratorio Práctico: Estimación y Predicción Salarial mediante Mínimos Cuadrados</h3>'
                 '<p>En este laboratorio empírico, aplicarás las ecuaciones analíticas de mínimos cuadrados ordinarios (OLS) para resolver un problema de contratación laboral: estimar el salario justo de un nuevo programador basado en sus años de experiencia laboral previa.</p>'
                 '<h4>Procedimiento del Experimento</h4>'
                 '<ol>'
                 '  <li>Descarga el dataset estructurado de salarios de la corporación.</li>'
                 '  <li>Calcula analíticamente los coeficientes óptimos $\beta_1$ (pendiente) y $\beta_0$ (intercepto) utilizando los datos cargados.</li>'
                 '  <li>Formula la ecuación predictiva final (ej. $Salario = 1500 \cdot Experiencia + 22000$).</li>'
                 '  <li>Estima el salario esperado para perfiles con 3.5, 7 y 12 años de experiencia.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto analítico para estimar la recta de regresión\n'
                 'def fit_ols_simple(x, y):\n'
                 '    mean_x, mean_y = np.mean(x), np.mean(y)\n'
                 '    numerator = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)])\n'
                 '    denominator = sum([(xi - mean_x)**2 for xi in x])\n'
                 '    beta_1 = numerator / denominator\n'
                 '    beta_0 = mean_y - beta_1 * mean_x\n'
                 '    return beta_0, beta_1</code></pre>'
                 '<p>Entrega tu notebook completo con el trazado de la recta OLS superpuesto a la dispersión de puntos originales y los salarios predichos explicados paso a paso.</p>'),
                
                # INTERMEDIO
                ('Métricas de Error', 'explicacion',
                 '<h3>Evaluación de Modelos de Regresión: MSE, RMSE y el Coeficiente de Determinación R-Cuadrado</h3>'
                 '<p>Una vez entrenado un modelo predictivo continuo, es indispensable evaluar cuantitativamente su capacidad de generalización y nivel de precisión. No basta con trazar una recta; requerimos métricas que nos informen del error absoluto del modelo y del porcentaje de variabilidad de los datos que nuestra ecuación lineal es capaz de explicar.</p>'
                 '<h4>Métricas de Pérdida Continua</h4>'
                 '<ul>'
                 '  <li><strong>Error Cuadrático Medio (MSE):</strong> Mide el promedio de los errores al cuadrado, penalizando severamente las desviaciones grandes (outliers).'
                 '      <p style="color:var(--neon-purple);">$$MSE = \\frac{1}{N} \\sum_{i=1}^N (y_i - \\hat{y}_i)^2$$</p>'
                 '  </li>'
                 '  <li><strong>Raíz del Error Cuadrático Medio (RMSE):</strong> Expresa la magnitud del error de predicción en las mismas unidades físicas que la variable dependiente Y.'
                 '      <p style="color:var(--neon-purple);">$$RMSE = \\sqrt{MSE}$$</p>'
                 '  </li>'
                 '  <li><strong>Coeficiente de Determinación ($R^2$):</strong> Cuantifica la proporción de la varianza total de $Y$ explicada por el modelo de regresión. Se acota entre 0 y 1, donde 1 representa un ajuste lineal perfecto.'
                 '      <p style="color:var(--neon-purple);">$$R^2 = 1 - \\frac{SS_{res}}{SS_{tot}} = 1 - \\frac{\\sum(y_i - \\hat{y}_i)^2}{\\sum(y_i - \\bar{y})^2}$$</p>'
                 '  </li>'
                 '</ul>'),
                
                ('Análisis Residual', 'explicacion',
                 '<h3>Análisis Residual: Validación de los Supuestos del Modelo Lineal Clásico</h3>'
                 '<p>El **Análisis Residual** es el método de diagnóstico fundamental para determinar si un modelo de regresión lineal simple es apropiado para modelar los datos analizados. Un residuo o error $e_i$ es la diferencia directa entre el valor real observado y la predicción de la recta: $e_i = y_i - \hat{y}_i$.</p>'
                 '<h4>Supuestos Críticos a Validar mediante Gráficos de Residuos</h4>'
                 '<ol>'
                 '  <li><strong>Linealidad:</strong> El gráfico de residuos frente a los valores ajustados ($\hat{y}_i$) debe mostrar puntos dispersos al azar alrededor de la línea cero, sin ningún patrón geométrico (como una curva en U, que indicaría que la relación real es no lineal).</li>'
                 '  <li><strong>Homocedasticidad (Varianza Constante):</strong> La dispersión de los residuos debe permanecer relativamente uniforme en todos los niveles de predicción. Si la dispersión tiene forma de "embudo", se viola este supuesto (heterocedasticidad).</li>'
                 '  <li><strong>Independencia:</strong> Los residuos no deben correlacionarse entre sí (ausencia de autocorrelación, común en series de tiempo).</li>'
                 '  <li><strong>Normalidad:</strong> La distribución de los errores debe aproximarse a una distribución normal con media cero, típicamente evaluada mediante un gráfico Q-Q (Quantile-Quantile).</li>'
                 '</ol>'),
                
                ('Taller Evaluación', 'demo',
                 '<h3>Taller de Evaluación de Desempeño: Análisis de Errores y Diagnóstico de Residuos</h3>'
                 '<p>En esta sesión práctica, utilizarás herramientas de diagnóstico en Python para evaluar el modelo de predicción salarial que construiste previamente. Aprenderás a computar las métricas de error y a graficar los residuos para validar la homocedasticidad y la normalidad.</p>'
                 '<h4>Objetivos del Taller</h4>'
                 '<ol>'
                 '  <li>Calcula manualmente los vectores de predicción $\hat{y}$ y el vector de residuos $e$.</li>'
                 '  <li>Calcula el MSE, RMSE y el coeficiente de determinación $R^2$ para certificar el rendimiento predictivo del modelo.</li>'
                 '  <li>Realiza un ploteo de residuos vs predicciones y describe si se visualizan indicios de heterocedasticidad.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto para calcular métricas de bondad de ajuste\n'
                 'def calculate_goodness_metrics(y_real, y_pred):\n'
                 '    ssr = sum([(yr - yp)**2 for yr, yp in zip(y_real, y_pred)])\n'
                 '    mean_y = sum(y_real)/len(y_real)\n'
                 '    sst = sum([(yr - mean_y)**2 for yr in y_real])\n'
                 '    r2 = 1.0 - (ssr / sst)\n'
                 '    mse = ssr / len(y_real)\n'
                 '    return mse, (mse**0.5), r2</code></pre>'
                 '<p>Sube tu notebook conteniendo las tres métricas calculadas y los gráficos de residuos analizados e interpretados conceptualmente.</p>'),
                
                ('Regresión Múltiple', 'explicacion',
                 '<h3>Regresión Lineal Múltiple: Predicción Multivariada y Álgebra Matricial de OLS</h3>'
                 '<p>Cuando la variable de interés dependiente Y se ve influenciada por dos o más variables independientes o explicativas, es imperativo generalizar el modelo a una <strong>Regresión Lineal Múltiple</strong>. Esto nos permite controlar simultáneamente múltiples efectos causales en las predicciones.</p>'
                 '<h4>Formulación Algebraica y Representación Matricial</h4>'
                 '<p>El modelo para $k$ variables explicativas y $N$ observaciones se formula matemáticamente como:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \dots + \beta_k x_{ik} + \epsilon_i$$</p>'
                 '<p>Utilizando álgebra lineal y notación matricial, el sistema de ecuaciones completo para todo el dataset se simplifica de forma sumamente elegante:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$\mathbf{y} = \mathbf{X}\mathbf{\beta} + \mathbf{\epsilon}$$</p>'
                 '<p>Donde $\mathbf{y}$ es un vector de $N \times 1$, $\mathbf{X}$ es la matriz de diseño de tamaño $N \times (k+1)$ (la primera columna está llena de unos para modelar el término del intercepto $\beta_0$), $\mathbf{\beta}$ es el vector de coeficientes de $(k+1) \times 1$, y $\mathbf{\epsilon}$ es el vector de errores. La solución óptima por mínimos cuadrados ordinarios en formato matricial se formula de forma icónica como:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$\mathbf{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$</p>'),
                
                ('Variables Dummy', 'explicacion',
                 '<h3>Codificación de Variables Categóricas: One-Hot Encoding y Variables Dummy</h3>'
                 '<p>Los algoritmos matemáticos de regresión lineal operan exclusivamente con coeficientes numéricos continuos. Sin embargo, en bases de datos del mundo real abundan las variables categóricas o nominales (como género, ciudad, nivel de estudios o marcas). Para integrar texto y categorías al modelo de regresión, aplicamos el concepto de **Variables Dummy (One-Hot Encoding)**.</p>'
                 '<h4>El Protocolo de Codificación y la Trampa de la Multicolinealidad</h4>'
                 '<p>Consiste en crear una nueva columna binaria (0 o 1) para cada una de las categorías exclusivas presentes en la variable original. Sin embargo, para evitar la denominada <strong>Trampa de la Variable Dummy</strong> (que genera multicolinealidad perfecta al ser la suma de todas las columnas binarias igual a 1, colisionando con el vector constante del intercepto), es estrictamente obligatorio omitir una de las variables binarias, la cual actuará como la <strong>categoría de referencia basal</strong> del modelo.</p>'
                 '<p>Analizaremos cómo se interpretan los coeficientes asociados a las variables dummy en los resultados de la regresión, representando el cambio esperado en la variable dependiente Y en comparación con la categoría de referencia basal omitida.</p>'),
                
                ('Mercado Inmobiliario', 'demo',
                 '<h3>Proyecto Inmobiliario: Predicción del Precio de Viviendas mediante Regresión Múltiple</h3>'
                 '<p>En este laboratorio avanzado, construirás un modelo predictivo multivariante de regresión lineal para estimar el valor comercial de bienes raíces en base a los metros cuadrados construidos, número de habitaciones, y una variable categórica correspondiente a la zona de ubicación (norte, centro, sur).</p>'
                 '<h4>Procedimiento Requerido</h4>'
                 '<ol>'
                 '  <li>Aplica One-Hot Encoding a la variable de zona geográfica omitiendo una columna para evitar la trampa de la variable dummy.</li>'
                 '  <li>Estructura la matriz de diseño $\mathbf{X}$ e integra la columna constante para el intercepto $\beta_0$.</li>'
                 '  <li>Calcula analíticamente los coeficientes estimadores utilizando la ecuación matricial de OLS: $\mathbf{\beta} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$.</li>'
                 '  <li>Evalúa el impacto individual de cada coeficiente e interpreta la métrica $R^2$ ajustada.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de OLS matricial puro en numpy\n'
                 'def fit_ols_matrix(X, y):\n'
                 '    # Agregar columna de unos para el intercepto si no está presente\n'
                 '    X_design = np.hstack([np.ones((X.shape[0], 1)), X])\n'
                 '    # Ecuación normal: beta = inv(X^T * X) * X^T * y\n'
                 '    beta = np.linalg.inv(X_design.T.dot(X_design)).dot(X_design.T).dot(y)\n'
                 '    return beta</code></pre>'
                 '<p>Sube tu notebook estructurado con la ecuación del modelo y las estimaciones inmobiliarias calculadas paso a paso.</p>'),
                
                # AVANZADO
                ('Regresión Logística', 'explicacion',
                 '<h3>Regresión Logística: Clasificación Lineal Binaria mediante la Función Sigmoide</h3>'
                 '<p>Cuando la variable dependiente de interés Y no es continua, sino categórica binaria (como Spam/No Spam, Éxito/Fallo, Transacción Fraudulenta/Lícita), el modelo de regresión lineal clásica deja de ser adecuado, ya que la recta OLS puede predecir valores fuera del intervalo $[0, 1]$. Para resolver esto, recurrimos a la <strong>Regresión Logística</strong>.</p>'
                 '<h4>La Función de Enlace Logit</h4>'
                 '<p>En lugar de predecir la salida discreta directamente, la regresión logística modela la **probabilidad** de que el evento ocurra, denotada por $p = P(Y=1|X)$. Para acotar las salidas al intervalo $[0, 1]$, pasamos la combinación lineal de entradas a través de la **función logística estándar (sigmoide)**:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$p = \sigma(z) = \\frac{1}{1 + e^{-(\beta_0 + \beta_1 X)}}$$</p>'
                 '<p>Al despejar la combinación lineal, obtenemos la función de enlace **Logit** o el logaritmo de los momios (log-odds), el cual demuestra que el modelo es lineal en el espacio de los log-odds:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$\ln\left( \\frac{p}{1 - p} \right) = \beta_0 + \beta_1 X$$</p>'),
                
                ('Matriz Confusión', 'explicacion',
                 '<h3>Evaluación de Clasificadores: La Matriz de Confusión y Métricas de Diagnóstico</h3>'
                 '<p>A diferencia de los modelos continuos evaluados con MSE o R2, los modelos de clasificación binaria como la regresión logística se evalúan contrastando las predicciones discretas frente a las clases reales observadas. La herramienta fundamental de diagnóstico para este fin es la **Matriz de Confusión**.</p>'
                 '<h4>Estructura de la Matriz</h4>'
                 '<p>La matriz tabula los cuatro resultados lógicos posibles de una clasificación:</p>'
                 '<ul>'
                 '  <li><strong>Verdaderos Positivos (TP):</strong> Casos reales positivos clasificados correctamente como positivos.</li>'
                 '  <li><strong>Verdaderos Negativos (TN):</strong> Casos reales negativos clasificados correctamente como negativos.</li>'
                 '  <li><strong>Falsos Positivos (FP) - Error Tipo I:</strong> Casos reales negativos clasificados erróneamente como positivos.</li>'
                 '  <li><strong>Falsos Negativos (FN) - Error Tipo II:</strong> Casos reales positivos clasificados erróneamente como negativos.</li>'
                 '</ul>'
                 '<h4>Derivación de Métricas Críticas</h4>'
                 '<p>A partir de estos cuatro cuadrantes, derivamos métricas fundamentales:</p>'
                 '<p style="color:var(--neon-purple);">$$\\text{Precisión (Accuracy)} = \\frac{TP + TN}{TP + TN + FP + FN}$$</p>'
                 '<p style="color:var(--neon-purple);">$$\\text{Exactitud (Precision)} = \\frac{TP}{TP + FP} \\quad (\\text{De lo predicho positivo, cuánto es real})$$</p>'
                 '<p style="color:var(--neon-purple);">$$\\text{Sensibilidad (Recall)} = \\frac{TP}{TP + FN} \\quad (\\text{De lo real positivo, cuánto se detectó})$$</p>'
                 '<p style="color:var(--neon-purple);">$$F1\\text{-Score} = 2 \\cdot \\frac{\\text{Precision} \\cdot \\text{Recall}}{\\text{Precision} + \\text{Recall}} \\quad (\\text{Media armónica})$$</p>'),
                
                ('Taller Logístico', 'demo',
                 '<h3>Taller Práctico: Implementación y Evaluación de un Clasificador de SPAM</h3>'
                 '<p>En este laboratorio técnico, implementarás un clasificador binario de correos electrónicos no deseados (SPAM) utilizando regresión logística y evaluarás su desempeño construyendo manualmente la matriz de confusión y calculando todas las métricas de diagnóstico (Accuracy, Precision, Recall y F1-Score).</p>'
                 '<h4>Procedimiento del Taller</h4>'
                 '<ol>'
                 '  <li>Carga el dataset de correos electrónicos con variables extraídas de frecuencia de palabras y etiquetas binarias (1 para SPAM, 0 para lícito).</li>'
                 '  <li>Entrena un modelo de regresión logística básica en Python.</li>'
                 '  <li>Aplica un umbral de decisión estándar de $0.5$ para convertir las probabilidades continuas en predicciones discretas.</li>'
                 '  <li>Construye la matriz de confusión de $2\times2$ tabulando las predicciones y calcula los parámetros TP, TN, FP y FN.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de cálculo de matriz de confusión\n'
                 'def evaluate_classification(y_true, y_pred_probs, threshold=0.5):\n'
                 '    y_pred = [1 if p >= threshold else 0 for p in y_pred_probs]\n'
                 '    tp = sum([1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1])\n'
                 '    tn = sum([1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0])\n'
                 '    fp = sum([1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1])\n'
                 '    fn = sum([1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0])\n'
                 '    return tp, tn, fp, fn</code></pre>'
                 '<p>Sube tu notebook documentando la matriz de confusión detallada y una reflexión sobre qué tipo de error (Tipo I o Tipo II) es más crítico al procesar SPAM.</p>'),
                
                ('Multicolinealidad', 'explicacion',
                 '<h3>El Desafío de la Multicolinealidad: Diagnóstico mediante el Factor de Inflación de la Varianza (VIF)</h3>'
                 '<p>En los modelos de regresión lineal múltiple, uno de los problemas teóricos y prácticos más destructivos es la <strong>Multicolinealidad</strong>. Ocurre cuando dos o más variables independientes o explicativas en el modelo están altamente correlacionadas linealmente entre sí, lo que dificulta aislar el efecto individual de cada variable sobre la predicción global y destruye la estabilidad numérica de la estimación de OLS.</p>'
                 '<h4>Consecuencias Analíticas de la Multicolinealidad</h4>'
                 '<p>Cuando hay multicolinealidad alta, los errores estándar de los coeficientes estimados ($\hat{\beta}_j$) se inflan exponencialmente. Esto provoca que las pruebas de hipótesis estadística t de Student dejen de ser fiables, clasificando variables importantes como no significativas debido a la enorme incertidumbre de su estimador.</p>'
                 '<h4>El Factor de Inflación de la Varianza (VIF)</h4>'
                 '<p>Para diagnosticar la presencia y gravedad del problema, calculamos el **VIF** para cada variable independiente $X_j$ construyendo una regresión auxiliar de $X_j$ en función de todas las demás variables independientes del modelo, obteniendo su correspondiente coeficiente $R_j^2$:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-purple);">$$VIF_j = \\frac{1}{1 - R_j^2}$$</p>'
                 '<p>Se consideran reglas de oro diagnósticas:</p>'
                 '<ul>'
                 '  <li><strong>$VIF < 5$:</strong> Multicolinealidad leve o tolerable.</li>'
                 '  <li><strong>$VIF \ge 10$:</strong> Multicolinealidad severa y destructiva. Se debe remover una de las variables correlacionadas o aplicar técnicas de reducción de dimensionalidad (como PCA) o regularización.</li>'
                 '</ul>'),
                
                ('Regularización', 'explicacion',
                 '<h3>Regularización Lasso (L1) y Ridge (L2): Mitigando el Sobreajuste en Alta Dimensionalidad</h3>'
                 '<p>Cuando entrenamos modelos de regresión con una gran cantidad de variables independientes explicativas, corremos el riesgo severo de caer en el <strong>Sobreajuste (Overfitting)</strong>: el modelo aprende el ruido aleatorio del dataset de entrenamiento pero pierde su capacidad de generalizar sobre datos nuevos no vistos. Para prevenir esto, incorporamos técnicas de **Regularización**, penalizando los coeficientes del modelo para que tiendan a cero.</p>'
                 '<h4>Modelado Matemático de Penalizaciones</h4>'
                 '<ul>'
                 '  <li><strong>Regresión Ridge (Regularización L2):</strong> Añade una penalización cuadrática equivalente al cuadrado de la norma L2 de los pesos. Reduce todos los coeficientes suavemente, estabilizándolos ante multicolinealidad, pero sin forzar a ninguno a ser exactamente cero.'
                 '      <p style="color:var(--neon-purple);">$$Ploss = MSE + \lambda \\sum_{j=1}^k \beta_j^2$$</p>'
                 '  </li>'
                 '  <li><strong>Regresión Lasso (Regularización L1):</strong> Añade una penalización absoluta basada en la norma L1. Tiene la propiedad matemática única de encoger algunos coeficientes a exactamente cero, actuando como un método automático de **Selección de Variables**.'
                 '      <p style="color:var(--neon-purple);">$$Ploss = MSE + \lambda \\sum_{j=1}^k |\beta_j|$$</p>'
                 '  </li>'
                 '</ul>'
                 '<p>Estudiaremos cómo el parámetro de fuerza de regularización $\lambda$ controla el balance entre el sesgo y la varianza en el modelo.</p>'),
                
                ('Proyecto Avanzado', 'demo',
                 '<h3>Proyecto Final de Regresión: Regresión Regularizada en Datasets Complejos de Alta Dimensionalidad</h3>'
                 '<p>El proyecto final de esta academia de Regresión Lineal Predictiva consiste en la construcción e implementación completa de un modelo predictivo robusto de regresión lineal regularizada para estimar el precio final de vehículos usados a partir de un dataset complejo de alta dimensionalidad con más de 40 variables continuas y nominales altamente correlacionadas.</p>'
                 '<h4>Requerimientos del Proyecto</h4>'
                 '<ul>'
                 '  <li>Realiza un preprocesamiento completo del dataset: normalización de variables continuas, codificación One-Hot para variables categóricas, y división de datos.</li>'
                 '  <li>Calcula el Factor de Inflación de la Varianza (VIF) inicial para diagnosticar la multicolinealidad.</li>'
                 '  <li>Implementa y entrena un modelo clásico de Regresión OLS, un modelo Ridge (L2) y un modelo Lasso (L1).</li>'
                 '  <li>Realiza una búsqueda del parámetro óptimo de regularización $\lambda$ (hyperparameter tuning) utilizando validación cruzada (Cross-Validation).</li>'
                 '  <li>Compara el rendimiento de los tres modelos calculando el MSE, RMSE y $R^2$ final sobre el conjunto de prueba, justificando analíticamente cuál modelo provee la mejor generalización.</li>'
                 '</ul>'
                 '<p>Sube tu informe final detallado y tu script de Python para ser evaluado por el comité matemático de la academia.</p>'),
            ]
        },
        {
            'id': 6,
            'title': 'Algoritmos Genéticos',
            'lessons': [
                # BASICO
                ('Darwinismo Digital', 'explicacion',
                 '<h3>Darwinismo Digital: Fundamentos de la Computación Evolutiva y el Espacio de Búsqueda</h3>'
                 '<p>La computación evolutiva es una rama de la Inteligencia Artificial inspirada directamente en las teorías biológicas de la selección natural y la evolución darwiniana de las especies formulada por Charles Darwin. Introducida formalmente por <strong>John Holland</strong> en la década de 1970 con la creación de los <strong>Algoritmos Genéticos (AGs)</strong>, esta metodología de optimización heurística busca "evolucionar" soluciones óptimas a problemas computacionales complejos.</p>'
                 '<h4>El Concepto de la Evolución Digital</h4>'
                 '<p>Los AGs no requieren información analítica de derivadas matemáticas de la función de coste. Operan simulando una población de soluciones candidatas que compiten por reproducirse. Las soluciones más aptas se seleccionan para transmitir sus características a las siguientes generaciones mediante cruce y mutación, permitiendo que la población converja progresivamente hacia la región óptima del espacio de búsqueda.</p>'
                 '<p>Analizaremos las ventajas existenciales de los AGs al resolver problemas sumamente difíciles caracterizados por espacios de búsqueda no lineales, discretos o repletos de óptimos locales, donde los métodos tradicionales de optimización analítica (como el descenso de gradiente) fallan inevitablemente.</p>'),
                
                ('Cromosomas y Genes', 'explicacion',
                 '<h3>Estructura de Datos Genética: Codificación del Genoma Digital</h3>'
                 '<p>El primer paso fundamental al diseñar un Algoritmo Genético consiste en estructurar la representación de los datos, mapeando las variables de decisión del problema real en una estructura de datos evolutiva. Aquí aplicamos analogías directas con la genética biológica:</p>'
                 '<ul>'
                 '  <li><strong>Gen:</strong> La unidad de información más pequeña que representa una variable de decisión específica (por ejemplo, un parámetro de configuración).</li>'
                 '  <li><strong>Cromosoma (Individuo):</strong> Una cadena ordenada de genes que codifica una solución candidata completa al problema.</li>'
                 '  <li><strong>Genotipo:</strong> La representación interna cifrada del cromosoma (por ejemplo, una cadena de bits binarios).</li>'
                 '  <li><strong>Fenotipo:</strong> La manifestación física o decodificación del cromosoma al dominio del problema real para su evaluación.</li>'
                 '</ul>'
                 '<h4>Técnicas de Codificación Estándar</h4>'
                 '<ol>'
                 '  <li><strong>Codificación Binaria:</strong> El genoma se representa mediante una cadena de bits (0s y 1s). Es el modelo clásico de Holland, fácil de analizar mediante el Teorema de los Esquemas.</li>'
                 '  <li><strong>Codificación de Valor Real / Flotante:</strong> Los genes son números continuos directos. Es ideal para optimización de funciones continuas complejas de ingeniería.</li>'
                 '  <li><strong>Codificación Permutacional:</strong> El cromosoma es una secuencia ordenada de índices únicos (ej. lista de ciudades para el TSP), donde no se permiten duplicados.</li>'
                 '</ol>'),
                
                ('Población Inicial', 'demo',
                 '<h3>Laboratorio Práctico: Generación Estructurada de Poblaciones Iniciales y Diversidad Genética</h3>'
                 '<p>El rendimiento y la velocidad de convergencia de un Algoritmo Genético dependen en gran medida del diseño de su **Población Inicial**. Si la población inicial carece de diversidad (si los individuos son muy similares desde el inicio), el algoritmo sufrirá una convergencia prematura en un óptimo local pobre, perdiendo capacidad de exploración.</p>'
                 '<h4>Procedimiento de Programación del Laboratorio</h4>'
                 '<ol>'
                 '  <li>Define el tamaño de la población (típicamente entre 50 y 200 individuos) y la longitud del cromosoma binario.</li>'
                 '  <li>Implementa una rutina de Python que genere individuos aleatorios distribuidos uniformemente utilizando generadores pseudoaleatorios.</li>'
                 '  <li>Codifica la rutina de decodificación que transforma el genotipo binario a un fenotipo de valor real en un rango específico $[x_{min}, x_{max}]$.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de generación de población binaria\n'
                 'import random\n'
                 'def generate_initial_population(pop_size, chromosome_len):\n'
                 '    # Genera una lista de listas de bits aleatorios\n'
                 '    return [[random.randint(0, 1) for _ in range(chromosome_len)] for _ in range(pop_size)]\n'
                 '\n'
                 'def decode_binary(chromosome, x_min, x_max):\n'
                 '    # Convierte binario a entero y luego a rango flotante\n'
                 '    bit_str = "".join(map(str, chromosome))\n'
                 '    val_int = int(bit_str, 2)\n'
                 '    max_int = (2 ** len(chromosome)) - 1\n'
                 '    return x_min + (val_int / max_int) * (x_max - x_min)</code></pre>'
                 '<p>Sube tu notebook con las funciones ejecutadas mostrando la dispersión y la diversidad de tu población inicial en un rango de $[-5.0, 5.0]$.</p>'),
                
                ('Función Fitness', 'explicacion',
                 '<h3>La Función de Aptitud (Fitness Function): La Métrica Rectora del Éxito Evolutivo</h3>'
                 '<p>En los Algoritmos Genéticos, el criterio que decide qué soluciones son "buenas" o "malas" se formaliza mediante la <strong>Función de Aptitud (Fitness Function)</strong>. Constituye el único enlace de comunicación entre el dominio del problema real y el motor abstracto de evolución artificial, evaluando qué tan bien adaptado está un individuo al entorno o problema específico.</p>'
                 '<h4>Diseño Matemático del Fitness</h4>'
                 '<p>La función de fitness debe asignar un único valor numérico real a cada individuo de la población. A mayor aptitud, mayor probabilidad tendrá el individuo de sobrevivir y reproducirse:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$Fitness(Cromosoma) = f(Fenotipo)$$</p>'
                 '<p>Analizaremos las diferencias críticas al formular el fitness en problemas de maximización (donde la aptitud es directamente proporcional a la función objetivo) y problemas de minimización (donde debemos mapear la función de coste $C(x)$ a una escala positiva inversa de aptitud, por ejemplo: $F(x) = \\frac{1}{C(x) + \\epsilon}$).</p>'),
                
                ('Paisaje Fitness', 'explicacion',
                 '<h3>El Paisaje de Aptitud (Fitness Landscape): Geometría del Espacio Muestral Evolutivo</h3>'
                 '<p>El concepto de **Paisaje de Aptitud (Fitness Landscape)**, propuesto originalmente por el genetista Sewall Wright en 1932, es una metáfora geométrica sumamente potente para visualizar el comportamiento dinámico de los Algoritmos Genéticos.</p>'
                 '<h4>Estructura del Paisaje Geométrico</h4>'
                 '<p>En este espacio n-dimensional, las coordenadas horizontales representan las combinaciones posibles de genes (genotipos) y la coordenada vertical representa el valor de aptitud (fitness). Esto forma una "topografía evolutiva" caracterizada por:</p>'
                 '<ul>'
                 '  <li>**Picos de Aptitud:** Regiones de alta adaptación correspondientes a soluciones óptimas locales o globales.</li>'
                 '  <li>**Valles:** Zonas de baja aptitud que representan soluciones no viables o ineficientes.</li>'
                 '  <li>**Rugosidad del Paisaje:** Si la topografía es suave y regular, es fácil de escalar mediante gradientes simples. Si el paisaje es altamente rugoso, caótico y discontinuo, los AGs destacan sobre los algoritmos tradicionales al usar operadores poblacionales de cruce para "saltar" entre picos de aptitud y evitar quedar atrapados en óptimos locales pobres.</li>'
                 '</ul>'),
                
                ('Taller Fitness', 'demo',
                 '<h3>Taller Práctico: Diseño y Evaluación de Funciones Fitness Complejas</h3>'
                 '<p>En esta sesión práctica, diseñarás e implementarás una función de fitness robusta para resolver un problema de optimización combinatorio clásico en ingeniería de software: el <strong>Problema de la Mochila (Knapsack Problem)</strong>.</p>'
                 '<h4>Procedimiento del Taller</h4>'
                 '<ol>'
                 '  <li>Carga la lista de 10 elementos disponibles con sus correspondientes pesos y utilidades comerciales.</li>'
                 '  <li>Define la variable de capacidad máxima de carga de la mochila (ej. 15 kg).</li>'
                 '  <li>Codifica la función fitness para un cromosoma binario de 10 bits. Si la combinación supera la capacidad máxima de la mochila, la función debe aplicar una **penalización drástica** (pérdida severa de aptitud) para evitar soluciones inviables.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de función fitness para la mochila con penalización\n'
                 'def evaluate_knapsack_fitness(chromosome, weights, values, max_capacity):\n'
                 '    total_weight = sum([w * b for w, b in zip(weights, chromosome)])\n'
                 '    total_value = sum([v * b for v, b in zip(values, chromosome)])\n'
                 '    if total_weight > max_capacity:\n'
                 '        # Penalización severa por inviabilidad\n'
                 '        return 0\n'
                 '    return total_value</code></pre>'
                 '<p>Entrega tu notebook con la función de fitness implementada y evalúa al menos 5 cromosomas aleatorios demostrando el efecto protector de la penalización.</p>'),
                
                # INTERMEDIO
                ('Operador de Selección', 'explicacion',
                 '<h3>Operadores de Selección: La Presión Selectiva y los Métodos de Selección de Progenitores</h3>'
                 '<p>El **Operador de Selección** es el encargado de dirigir la búsqueda del Algoritmo Genético hacia regiones prometedoras del espacio de búsqueda, imitando el principio biológico de la supervivencia de los más aptos. Su objetivo es elegir a los individuos de la generación actual que actuarán como "padres" para transmitir sus características a la siguiente generación.</p>'
                 '<h4>Metodologías de Selección Estándar</h4>'
                 '<ul>'
                 '  <li>**Selección por Ruleta (Roulette Wheel Selection):** La probabilidad $p_i$ de seleccionar a un individuo es proporcional a su aptitud absoluta. Se visualiza como una ruleta de casino donde los individuos más aptos poseen sectores geométricos más grandes:'
                 '      <p style="color:var(--neon-purple);">$$p_i = \\frac{Fitness_i}{\\sum_{j=1}^M Fitness_j}$$</p>'
                 '  </li>'
                 '  <li>**Selección por Torneo (Tournament Selection):** Se eligen al azar $k$ individuos de la población y el que tenga mayor aptitud gana el torneo y es seleccionado. Permite controlar fácilmente la **presión selectiva** variando el tamaño del torneo $k$.</li>'
                 '  <li>**Selección por Ranking:** Ordena la población según su aptitud y asigna una probabilidad basada puramente en su rango ordinal, estabilizando la deriva genética.</li>'
                 '</ul>'),
                
                ('Cruce (Crossover)', 'explicacion',
                 '<h3>El Operador de Cruce (Crossover): Recombinación Genética y Transferencia de Características</h3>'
                 '<p>El **Cruce (Crossover)** es el operador evolutivo nuclear de los Algoritmos Genéticos. Es el encargado de la **Explotación** del espacio de búsqueda: toma características de dos soluciones padres con alta aptitud y las recombina para engendrar individuos hijos que idealmente hereden las mejores virtudes de ambos progenitores.</p>'
                 '<h4>Tipos Fundamentales de Cruce Binario</h4>'
                 '<ol>'
                 '  <li>**Cruce de Un Punto:** Se selecciona al azar un punto de corte a lo largo del cromosoma. Los genes anteriores al corte se heredan del Padre 1 y los posteriores se heredan del Padre 2.'
                 '      <p>Padre 1: <code>1111|1111</code>, Padre 2: <code>0000|0000</code> $\\rightarrow$ Hijo: <code>1111|0000</code></p>'
                 '  </li>'
                 '  <li>**Cruce de Dos Puntos:** Se seleccionan dos puntos de corte, intercambiando el segmento central entre ambos cromosomas padres.</li>'
                 '  <li>**Cruce Uniforme:** Cada gen del hijo se decide individualmente lanzando una moneda al aire (probabilidad típica: 50% de heredar del Padre 1 y 50% del Padre 2).</li>'
                 '</ol>'
                 '<p>Estudiaremos cómo el parámetro de la **Tasa de Cruce ($p_c$)**, que oscila típicamente en el intervalo $[0.6, 0.95]$, controla la frecuencia con la que se aplica la recombinación genética sobre la población.</p>'),
                
                ('Taller Cruce', 'demo',
                 '<h3>Taller de Programación Evolutiva: Implementación de Operadores de Recombinación de un Punto</h3>'
                 '<p>En este laboratorio técnico, codificarás en Python el operador de cruce clásico de un punto y evaluarás la variabilidad cromosómica resultante a partir de dos padres seleccionados.</p>'
                 '<h4>Procedimiento del Taller</h4>'
                 '<ol>'
                 '  <li>Define dos cromosomas binarios correspondientes a dos soluciones viables conocidas del problema de la mochila.</li>'
                 '  <li>Codifica la función de cruce de un punto utilizando cortes de arreglos nativos de Python.</li>'
                 '  <li>Implementa la lógica del parámetro de probabilidad de cruce ($p_c$). Si un número aleatorio es mayor a $p_c$, el operador no se ejecuta y los hijos son copias exactas de los padres.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de cruce de un punto en Python\n'
                 'def crossover_one_point(parent_1, parent_2, p_c=0.8):\n'
                 '    if random.random() > p_c:\n'
                 '        return parent_1.copy(), parent_2.copy()\n'
                 '    # Seleccionar punto de corte aleatorio\n'
                 '    cut_point = random.randint(1, len(parent_1) - 1)\n'
                 '    child_1 = parent_1[:cut_point] + parent_2[cut_point:]\n'
                 '    child_2 = parent_2[:cut_point] + parent_1[cut_point:]\n'
                 '    return child_1, child_2</code></pre>'
                 '<p>Sube tu notebook conteniendo la función de cruce y realiza una prueba con 50 iteraciones registrando la similitud genética promedio de los descendientes.</p>'),
                
                ('Mutación', 'explicacion',
                 '<h3>El Operador de Mutación: Exploración Genética e Inmunidad a los Óptimos Locales</h3>'
                 '<p>Mientras que el cruce se encarga de explotar las regiones conocidas recombinando soluciones buenas, el **Operador de Mutación** tiene la responsabilidad existencial de la **Exploración**: introduce pequeñas variaciones aleatorias aleatorias en los cromosomas hijos para inyectar diversidad inédita a la población.</p>'
                 '<h4>Mecanismo del Operador de Mutación</h4>'
                 '<p>La mutación previene que la población se homogenice por completo e introduce nuevos genes en el pool genético, garantizando que el algoritmo pueda escapar de los **Óptimos Locales** del paisaje de aptitud.</p>'
                 '<ul>'
                 '  <li>**Mutación Binaria (Bit Flip Crossover):** Consiste en recorrer gen por gen el cromosoma y, con una probabilidad pequeña dada por la **Tasa de Mutación ($p_m$)**, invertir el bit (de 0 a 1, o de 1 a 0).'
                 '      <p>Cromosoma Hijo: <code>110101</code> $\\rightarrow$ Mutación del Bit 3 $\\rightarrow$ <code>111101</code></p>'
                 '  </li>'
                 '  <li>**Tasa de Mutación ($p_m$):** Es un parámetro críticamente sensible que suele fijarse en valores muy bajos, típicamente del orden de $\\frac{1}{L}$ (donde $L$ es la longitud del cromosoma, lo que equivale a mutar en promedio un bit por individuo). Si $p_m$ es demasiado alto, el algoritmo degenera en una búsqueda puramente aleatoria ineficiente.</li>'
                 '</ul>'),
                
                ('Elitismo', 'explicacion',
                 '<h3>Elitismo: Garantía Matemática de la Preservación Genética de la Excelencia</h3>'
                 '<p>En el ciclo estándar de un Algoritmo Genético, los operadores de cruce y mutación son probabilísticos y destructivos. Existe el riesgo latente de que, al recombinar o mutar a los mejores individuos de la generación actual, se destruyan sus valiosas combinaciones genéticas, perdiendo al mejor espécimen encontrado hasta el momento.</p>'
                 '<h4>El Protocolo de Elitismo</h4>'
                 '<p>Para proteger el progreso evolutivo, se implementa la técnica de **Elitismo**. Consiste en clonar intactos a los mejores individuos de la generación actual (por ejemplo, el top 1% o 2% de la población) y transmitirlos directamente directamente a la población de la generación siguiente, antes de aplicar los operadores destructivos de cruce y mutación sobre el resto de la población.</p>'
                 '<p>Analizaremos cómo el elitismo acelera drásticamente la convergencia del algoritmo al garantizar que la aptitud del mejor individuo de la población sea una **función estrictamente no decreciente** a lo largo de las generaciones:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$BestFitness(Gen_{t+1}) \\ge BestFitness(Gen_t)$$</p>'),
                
                ('Taller Ciclo Completo', 'demo',
                 '<h3>Taller Práctico: Integración Completa de un Ciclo de Algoritmo Genético</h3>'
                 '<p>En este taller integrador, unirás todas las piezas construidas hasta el momento (población inicial, función de fitness, selección por torneo, cruce de un punto, mutación binaria y elitismo) para ensamblar el ciclo evolutivo completo de un Algoritmo Genético capaz de resolver el Problema de la Mochila de forma autónoma.</p>'
                 '<h4>Estructura del Ciclo Evolutivo Requerido</h4>'
                 '<ol>'
                 '  <li>Inicializar población aleatoria.</li>'
                 '  <li>Evaluar la aptitud (fitness) de toda la población.</li>'
                 '  <li>Reservar a los mejores 2 individuos (Elitismo).</li>'
                 '  <li>Bucle de selección de padres, cruce y mutación para completar la población restante.</li>'
                 '  <li>Reemplazar la vieja población y registrar al mejor individuo histórico.</li>'
                 '  <li>Repetir durante 100 generaciones o hasta alcanzar convergencia estable.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto del bucle evolutivo integrado\n'
                 'def run_evolutionary_loop(generations, pop_size, chrom_len, max_cap):\n'
                 '    pop = generate_initial_population(pop_size, chrom_len)\n'
                 '    best_history = []\n'
                 '    for gen in range(generations):\n'
                 '        fits = [evaluate_knapsack_fitness(ind, w, v, max_cap) for ind in pop]\n'
                 '        best_history.append(max(fits))\n'
                 '        # Elitismo, selección, reproducción...\n'
                 '    return best_history</code></pre>'
                 '<p>Sube tu notebook completo con el gráfico que muestre la evolución y el incremento paulatino del mejor fitness histórico a lo largo de las generaciones.</p>'),
                
                # AVANZADO
                ('Problema del Viajero', 'explicacion',
                 '<h3>El Problema del Viajante de Comercio (TSP): Optimización de Permutaciones en Redes de Transporte</h3>'
                 '<p>El <strong>Problema del Viajante de Comercio (TSP - Traveling Salesperson Problem)</strong> es un problema clásico de optimización combinatoria clasificado como NP-duro. Consiste en encontrar la ruta más corta posible que permita a un vendedor visitar un conjunto de N ciudades exactamente una vez y regresar al punto de partida.</p>'
                 '<h4>El Desafío de la Codificación</h4>'
                 '<p>Si intentamos resolver el TSP utilizando la codificación binaria clásica de Holland, los operadores de cruce y mutación tradicionales generarán invariablemente rutas no viables con ciudades repetidas (por ejemplo, visitar la ciudad 3 dos veces) y ciudades omitidas por completo. Por ende, es estrictamente obligatorio migrar a una **Codificación Permutacional**:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$Cromosoma = [C_3, C_1, C_5, C_2, C_4]$$</p>'
                 '<p>Donde cada número representa el índice de una ciudad única y el cromosoma completo representa la secuencia exacta del viaje. Analizaremos cómo se calcula la aptitud en el TSP, definiéndose de forma inversa a la distancia euclidiana total del trayecto de viaje.</p>'),
                
                ('Cruce de Orden (OX)', 'explicacion',
                 '<h3>Cruce de Orden (Order Crossover - OX): Recombinación de Genomas Permutacionales</h3>'
                 '<p>Dado que no podemos utilizar el cruce convencional en cromosomas permutacionales para resolver el problema del viajero (TSP), debemos diseñar operadores especializados en preservar el orden relativo y la posición de los genes sin introducir duplicados. El operador estándar industrial es el **Cruce de Orden (OX - Order Crossover)**.</p>'
                 '<h4>Algoritmo de Recombinación OX</h4>'
                 '<ol>'
                 '  <li>Se seleccionan al azar dos puntos de corte idénticos en ambos padres.</li>'
                 '  <li>Se copia el segmento central delimitado por los cortes directamente del Padre 1 al correspondiente segmento central del Hijo 1.</li>'
                 '  <li>Partiendo del segundo punto de corte, se recorre el Padre 2 gen por gen de forma circular. Si un gen no está presente en el segmento central ya heredado del Padre 1, se inserta en la primera posición disponible del Hijo 1 de forma circular.</li>'
                 '</ol>'
                 '<p>Este ingenioso algoritmo preserva las secuencias locales y el orden relativo de los tramos de ruta de forma impecable, garantizando que el descendiente siempre sea una permutación legal y válida sin ciudades duplicadas.</p>'),
                
                ('Taller Rutas', 'demo',
                 '<h3>Taller Avanzado: Optimización del Viajero mediante Algoritmos Genéticos Permutacionales</h3>'
                 '<p>En este laboratorio avanzado, implementarás y codificarás en Python el cruce de orden (OX) y un operador de mutación por intercambio (Swap Mutation) para resolver el problema del viajero (TSP) para una red de 10 ciudades en un plano bidimensional.</p>'
                 '<h4>Pipeline del Taller</h4>'
                 '<ol>'
                 '  <li>Define la matriz de distancias euclidianas entre las 10 ciudades a partir de sus coordenadas en 2D.</li>'
                 '  <li>Codifica el operador de cruce de orden (OX).</li>'
                 '  <li>Implementa la mutación por intercambio (Swap Mutation), que simplemente intercambia aleatoriamente la posición de dos ciudades en la secuencia del viaje.</li>'
                 '  <li>Corre la evolución y encuentra la ruta más corta y económica para completar el viaje.</li>'
                 '</ol>'
                 '<pre><code># Esqueleto de mutación por intercambio permutacional\n'
                 'def mutate_swap(chromosome, p_m=0.1):\n'
                 '    if random.random() > p_m:\n'
                 '        return chromosome\n'
                 '    idx1, idx2 = random.sample(range(len(chromosome)), 2)\n'
                 '    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]\n'
                 '    return chromosome</code></pre>'
                 '<p>Sube tu notebook con la función OX implementada y una gráfica que ilustre la mejor ruta de viaje final optimizada.</p>'),
                
                ('Inteligencia de Enjambre', 'explicacion',
                 '<h3>Inteligencia de Enjambre: Modelado Colectivo e Algoritmos Bio-Inspirados</h3>'
                 '<p>Más allá de la genética evolutiva clásica que imita la reproducción cromosómica, existe otra vertiente monumental en la IA bio-inspirada: la **Inteligencia de Enjambre (Swarm Intelligence)**. Consiste en modelar el comportamiento colectivo y coordinado de sistemas descentralizados y auto-organizados de agentes simples que interactúan localmente entre sí y con su entorno.</p>'
                 '<h4>Inspiración Biológica del Enjambre</h4>'
                 '<p>Esta metodología se inspira en patrones de la naturaleza como:</p>'
                 '<ul>'
                 '  <li>El vuelo coordinado de bandadas de pájaros o cardúmenes de peces.</li>'
                 '  <li>El comportamiento social de colonias de hormigas buscando comida (Ant Colony Optimization).</li>'
                 '  <li>El vuelo de búsqueda de enjambres de abejas.</li>'
                 '</ul>'
                 '<p>En estas sociedades animales, no existe ningún líder central que dicte órdenes de movimiento. El comportamiento global inteligente de búsqueda de recursos emerge de forma sorprendente gracias a reglas locales extremadamente sencillas de proximidad y comunicación indirecta, superando las capacidades individuales de los agentes.</p>'),
                
                ('PSO en Acción', 'explicacion',
                 '<h3>Optimización por Enjambre de Partículas (PSO): Vectores de Fuerza Físicos y Socialización</h3>'
                 '<p>El algoritmo de **Optimización por Enjambre de Partículas (PSO - Particle Swarm Optimization)**, desarrollado por James Kennedy y Russell Eberhart en 1995, es la técnica clásica de inteligencia de enjambre para optimizar funciones matemáticas continuas multidimensionales.</p>'
                 '<h4>Ecuaciones Físicas de Movimiento</h4>'
                 '<p>En el PSO, cada solución candidata se visualiza como una "partícula" sin masa que vuela a través del espacio de búsqueda hiperdimensional. Cada partícula $i$ posee un vector de posición actual $\mathbf{x}_i$ y un vector de velocidad $\mathbf{v}_i$, los cuales se actualizan iterativamente sumando fuerzas de inercia, atracción cognitiva (hacia su mejor posición individual histórica $\mathbf{p}_i$) y atracción social (hacia la mejor posición histórica global descubierta por todo el enjambre $\mathbf{g}$):</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\mathbf{v}_i^{(t+1)} = w \mathbf{v}_i^{(t)} + c_1 r_1 (\mathbf{p}_i - \mathbf{x}_i^{(t)}) + c_2 r_2 (\mathbf{g} - \mathbf{x}_i^{(t)})$$</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$\mathbf{x}_i^{(t+1)} = \mathbf{x}_i^{(t)} + \mathbf{v}_i^{(t+1)}$$</p>'
                 '<p>Donde $w$ es el peso de inercia, $c_1$ es el coeficiente de aprendizaje cognitivo, $c_2$ el coeficiente de aprendizaje social, y $r_1, r_2$ son números aleatorios uniformes independientes en el rango $[0, 1]$.</p>'),
                
                ('Proyecto Bio-IA', 'demo',
                 '<h3>Proyecto de Fin de Grado: Optimización Bio-Inspirada de la Función de Rastrigin</h3>'
                 '<p>El proyecto final de esta academia de Algoritmos Genéticos consiste en el diseño, implementación y evaluación comparativa completa del algoritmo de Optimización por Enjambre de Partículas (PSO) para encontrar el mínimo global absoluto de la **Función de Rastrigin** de 5 dimensiones.</p>'
                 '<h4>La Función Multimodal de Rastrigin</h4>'
                 '<p>La función de Rastrigin es una función matemática no lineal altamente multimodal caracterizada por contener una enorme cantidad de óptimos locales rugosos, sirviendo como un excelente benchmark de estrés para evaluar algoritmos metaheurísticos:</p>'
                 '<p style="text-align:center; font-size:1.1rem; color:var(--neon-blue);">$$f(\mathbf{x}) = 10d + \\sum_{i=1}^d \left( x_i^2 - 10 \cos(2\pi x_i) \\right)$$</p>'
                 '<h4>Requerimientos del Entregable</h4>'
                 '<ul>'
                 '  <li>Implementar el enjambre de partículas PSO en Python configurando un tamaño mínimo de 30 partículas.</li>'
                 '  <li>Evaluar la convergencia variando el coeficiente cognitivo $c_1$ y social $c_2$ para analizar cómo influyen en el equilibrio entre exploración y explotación.</li>'
                 '  <li>Presentar un informe de fin de grado que demuestre la velocidad de convergencia y la capacidad del enjambre para eludir los miles de valles locales y localizar el mínimo global absoluto en la coordenada origen $\mathbf{0}$ con una precisión mínima de 4 decimales.</li>'
                 '</ul>'
                 '<p>Sube tu notebook de entrega final e informe técnico detallado para ser calificado por el tribunal académico.</p>'),
            ]
        }
    ]

    for c_info in courses_info:
        try:
            course = Course.objects.get(id=c_info['id'])
            # Update title and level/details to be premium
            course.title = c_info['title']
            course.save()

            print(f"\nInyectando contenido premium para el Curso {course.id}: {course.title}...")

            order = 1
            for title, s_type, html_content in c_info['lessons']:
                # Detect Level
                if order <= 6:
                    level_tag = 'BASICO'
                elif order <= 12:
                    level_tag = 'INTERMEDIO'
                else:
                    level_tag = 'AVANZADO'

                full_title = f'[{level_tag}] {title}'
                
                # Check if it should be explicacion or demo in the database
                # In final_content_setup.py, they had specific types
                # Let's map it cleanly
                db_section_type = 'explicacion' if s_type == 'explicacion' else 'demo'

                CourseContent.objects.create(
                    course=course,
                    title=full_title,
                    content=html_content,
                    section_type=db_section_type,
                    order=order
                )
                print(f"  -> Creada lección {order}: {full_title} ({db_section_type})")
                order += 1

            print(f"Curso {course.title} actualizado exitosamente con {order-1} lecciones.")
        except Course.DoesNotExist:
            print(f"ERROR: No se encontró el curso con ID {c_info['id']} en la base de datos.")

if __name__ == "__main__":
    run()
