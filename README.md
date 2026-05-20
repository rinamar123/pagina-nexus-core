# 🤖 Plataforma Educativa de Inteligencia Artificial y Machine Learning - IA ACADEMY - Nexo Core

Este es el repositorio oficial de la **Plataforma Educativa de IA y Machine Learning - IA ACADEMY**, una moderna aplicación web desarrollada en **Django** con un diseño estético de alta fidelidad estilo **Cyberpunk / Dark Mode** y una arquitectura robusta para la gestión académica, interactividad de estudiantes y automatización de servicios de seguridad y notificaciones.

El workspace contiene el directorio principal de desarrollo **`Laboratorio_RinaMarriaga`**, el cual aloja la versión avanzada, completa e hiper-personalizada de la plataforma. Esta versión cuenta con el sistema de seguridad obligatorio con fuerza de contraseña, flujo interactivo de progreso de clases, entregas de talleres, carga de archivos de proyecto final (CSV), estadísticas de rendimiento y promedio académico de 0.0 a 5.0, emulador de terminal interactivo de Python, semillas de datos completos de producción y el lienzo de partículas interactivas estilo Antigravity.

---

## 👤 Usuarios de Prueba

### Administradores

| Usuario | Contraseña | Notas |
|---------|------------|-------|
| `admin` | `admin123` | Acceso total al panel `/panel/login/` |
| `profesor` | `Profesor2026*` | Acceso total al panel `/panel/login/` |

### Estudiantes

| Usuario | Contraseña | Nombre | Estado |
|---------|------------|--------|--------|
| `andres01032001` | `Iacademy2026*` | Andres | Aceptado |
| `ana.garcia` | `Ana2026*` | Ana García | Aceptado |
| `maria.rodriguez` | `Maria2026*` | María Rodríguez | Aceptado |
| `carlos.lopez` | `Carlos2026*` | Carlos López | Pendiente |

> Para crear o restablecer estos usuarios en cualquier entorno (local o producción):  
> `python manage.py seed_test_users`

---

## 🚀 Características Implementadas y Mejoras Agregadas

Hemos evolucionado el proyecto original añadiendo una capa de interactividad premium, optimizando la experiencia de usuario y garantizando la robustez del sistema:

### 1. 🔒 Capa de Seguridad Obligatoria (Force Password Update)
* **Control de Primer Acceso:** Implementación de un decorador personalizado `@check_password_change` que intercepta todas las vistas del portal del estudiante. Si el estudiante aún posee su contraseña generada aleatoriamente por el sistema (`generated_password`), es redirigido obligatoriamente a actualizarla.
* **Políticas de Seguridad Estrictas:** Validación en tiempo real (frontend y backend) de contraseñas de alta seguridad que exige:
  * Mínimo de **10 caracteres** de longitud.
  * Al menos **una letra mayúscula** `[A-Z]`.
  * Al menos **una letra minúscula** `[a-z]`.
  * Al menos **un número** `\d`.
  * Al menos **un carácter especial** `[\W_]` (como `@`, `#`, `$`, `%`, `*`).
* **Visualización Dinámica:** Interfaz interactiva de cambio de clave con indicadores visuales de cumplimiento de reglas de seguridad.

### 2. 🔑 Flujo Integral de Recuperación de Contraseña
* Integración nativa y segura de las vistas de autenticación de Django (`PasswordResetView`, `PasswordResetDoneView`, `PasswordResetConfirmView`, `PasswordResetCompleteView`).
* **Diseño Premium:** Plantillas personalizadas con temática cyberpunk para todo el flujo de recuperación (solicitud, correo enviado, confirmación segura con token de un solo uso y pantalla de completado).
* **Alertas de Seguridad:** Envío automatizado de correos de confirmación en caso de que la contraseña sea cambiada, incluyendo enlaces directos para recuperar la cuenta si no fue autorizada.

### 3. 👤 Perfil de Estudiante Editable y Dinámico
* Sección dedicada dentro del dashboard del estudiante que permite la edición de sus datos personales esenciales:
  * Nombre completo.
  * Número de teléfono.
  * Dirección de residencia.
  * **Foto de Perfil:** Carga y actualización de foto de perfil almacenada en la base de datos y renderizada de manera dinámica en la barra lateral y cabeceras.

### 4. 📈 Sistema de Seguimiento de Progreso (Lesson Progress)
* **Base de Datos Dinámica:** Creación del modelo `LessonProgress` para rastrear las lecciones completadas por cada estudiante en cada curso.
* **Interactividad Directa:** Botones de "Completar Tema" y "Siguiente" que marcan la lección como completada y redirigen automáticamente al siguiente módulo del curso.
* **Barras de Progreso en Tiempo Real:** Renderizado visual de porcentajes de completado en el panel principal y las páginas de curso.
* **Bloqueo/Desbloqueo de Evaluaciones:** Liberación del proyecto final o parcial cuando el estudiante completa el 100% de los temas interactivos del curso.

### 5. 📂 Sistema de Entregas de Talleres (Assignment Submissions)
* **Carga de Archivos:** Los estudiantes pueden subir y sincronizar sus entregas y talleres directamente dentro de cada tema de aprendizaje en la base de datos (`AssignmentSubmission`).
* **Evaluación del Administrador:** Soporte en base de datos para calificaciones de talleres.
* **Entrega de Proyecto Final (CSV):** Un cargador de archivos especializado diseñado para entregar proyectos prácticos (archivos CSV de sets de datos) una vez que todas las lecciones del curso están completadas.

### 6. 📊 Dashboard Estadístico Académico e Historial de Calificaciones
* Interfaz analítica (`estadisticas.html`) que recopila métricas clave del estudiante:
  * Porcentaje exacto de progreso por cada curso.
  * Promedio de notas convertido matemáticamente a la escala académica de **0.0 a 5.0**.
  * Estado de aprobación dinámico ("APROBADO" si promedio es $\ge 3.0$, "EN PROCESO" si está cursando, y "SIN NOTAS" si no hay calificaciones registradas).
  * Promedio Académico Acumulado (GPA) total en el sistema.

### 7. 🎨 Interfaz Cyberpunk de Alta Fidelidad
* Estilo visual vanguardista en modo oscuro con acentos de color curados (azul neón, magenta, morado).
* **Partículas Interactivas en Canvas (Efecto Antigravity):** Fondo dinámico con un lienzo `<canvas>` que dibuja una red de nodos flotantes y genera una estela de puntitos luminosos (neon cyan y magenta) que siguen el movimiento del cursor, conectándose entre sí con líneas láser tenues y atrayéndose magnéticamente al ratón.
* **Cifras de Red Expandidas:** Un panel de métricas en el encabezado con efectos de cristal hover 3D que indica en tiempo real el estado del sistema y del curso: Uptime, Latencia, Nodos Activos, Estudiantes Sincronizados e Interactividad.
* Efectos de **Glassmorphism** (paneles translúcidos con desenfoque de fondo).
* Animaciones fluidas, efectos hover interactivos en tarjetas de cursos, tipografía premium (`Space Grotesk` y `Outfit` vía Google Fonts) y un diseño totalmente responsivo adaptado para computadores y dispositivos móviles.

### 8. 🌾 Semillas de Datos Avanzadas
* Creación de scripts especializados para poblar la base de datos con contenido pedagógico real de alta calidad en áreas de Programación Python, Django y Machine Learning (ej. `populate_premium_full.py`, `setup_exam_questions.py`, `final_content_setup.py`), listos para producción.

### 9. 🌟 Últimas Innovaciones y Mejoras de Interfaz (Portal del Estudiante)
* **Perfil Flotante Superior Interactivo (Dropdown Menu):**
  * Refactorización del indicador de usuario sincronizado de la barra de navegación en un gatillo interactivo (`.profile-nav-container`) con efectos de hover neón y una flecha indicadora `▼`.
  * Integración de un menú desplegable flotante de alta fidelidad (`.profile-dropdown-menu`) estilo glassmorphism que se activa al hacer clic, mostrando la ficha técnica completa del estudiante (avatar redondo enmarcado en neón, nombre, correo, teléfono, nivel y dirección de red) sin sobrecargar la pantalla principal.
  * Incorporación de un botón interactivo neón violeta "**⚙️ EDITAR PERFIL**" en la parte inferior del panel flotante para guiar de manera clara y rápida al formulario de edición de perfil.
  * Programación de controladores de exclusión mutua de dropdowns y dismiss automático con clics externos.
* **Libros de Texto Ultra-Enriquecidos (3,000 palabras por clase):**
  * Carga masiva en las 54 lecciones de la base de datos de un temario científico exhaustivo de grado académico (equivalente a 5 hojas de Word de alta densidad por tema) estructurado en español técnico con antecedentes epistemológicos, fórmulas matemáticas en notación LaTeX, simulaciones en pseudocódigo formal y discusiones críticas de optimización.
* **Diagramas Académicos Cyberpunk Generados por Software:**
  * Diseño de un script generador programático (`generate_diagrams_pil.py`) que dibuja matemáticamente 3 diagramas académicos en formato PNG (Perceptrón/Control Difuso, Línea de Regresión OLS con errores residuales y flujo reproductivo genético/PSO) en colores cyberpunk sobre fondo oscuro.
  * Integración e inserción directa de estas imágenes científicas en las lecciones de sus respectivos cursos (`/media/diagrams/`) como figuras de referencia técnica.
* **Diagnóstico Neuronal Dinámico por AJAX:**
  * Re-diseño del widget de autoevaluación estático a un motor dinámico que recorre y renderiza en tiempo real los 54 retos diagnósticos únicos guardados en base de datos.
  * Sincronización inmediata con el endpoint `/submit_challenge/` mediante peticiones asíncronas POST AJAX que evalúan las respuestas al instante, proyectando retroalimentación de postgrado y coloración verde neón (correcto) o carmesí (incorrecto).
* **Animaciones de Física Realista y Efecto Bezier:**
  * Animación oscilatoria basada en física real (`@keyframes bellRing`) que balancea dinámicamente la campana de notificaciones al pasar el cursor.
  * Botón de cierre de sesión (**LOGOUT**) con efectos de transición cubic-bezier, desplazamiento vertical sutil y resplandor neón carmesí de alta gama.
* **Flujo Pedagógico Unificado:**
  * Remoción de todas las integraciones estáticas de YouTube y nodos de refuerzo redundantes en `curso.html` para centrar la atención del alumno en los libros de texto avanzados de alta densidad y sus retos diagnósticos.

---

## 📂 Estructura del Proyecto (`Laboratorio_RinaMarriaga`)

```text
Laboratorio_RinaMarriaga/
├── ai_project/               # Configuración del proyecto principal Django
│   ├── settings.py           # Variables de configuración, SMTP, Gmail API y bases de datos
│   ├── urls.py               # Enrutamiento de URLs de todo el ecosistema
│   └── ...
├── enrollment/               # App de Inscripción y Landing Page principal
│   ├── models.py             # Modelos de Course, Student, CourseContent, Exam, ExamAttempt
│   ├── views.py              # Vistas de catálogo y procesamiento de solicitudes de ingreso
│   └── templates/            # Landing page index y vistas de cursos
├── panel/                    # App del Panel de Administración (Gestión Interna)
│   ├── views.py              # Gestión de estudiantes, cursos, carga de recursos y exportaciones CSV
│   └── templates/            # Dashboard administrativo y formularios de edición
├── student_portal/           # App del Portal del Estudiante (Dashboard Académico)
│   ├── models.py             # Modelos de LessonProgress y AssignmentSubmission
│   ├── views.py              # Lógica de progreso, estadísticas, edición de perfil y force password
│   └── templates/            # Vistas cyberpunk de dashboard, estadísticas, cambio de contraseña, etc.
├── terminal/                 # App del Emulador de Consola Interactiva
│   ├── views.py              # Control de acceso y renderizado del sandbox de Python
│   └── templates/            # Interfaz interactiva de la terminal virtual de código
├── notificaciones/           # App del Sistema de Log de Notificaciones Internas
│   └── models.py             # Modelo Notification (almacena logs de alertas en base de datos)
├── email_service/            # App del Sistema de Comunicaciones Automatizadas
│   ├── services.py           # Envío de correos de credenciales, avisos de seguridad y aceptaciones
│   └── gmail_api.py          # Adaptador de envío seguro a través de la Gmail API REST
├── db.sqlite3                # Base de datos pre-migrada y pre-cargada con contenido premium
├── requirements.txt          # Dependencias y librerías del proyecto
└── manage.py                 # Gestor de comandos de Django
```

---

## 🛠️ Guía de Instalación y Recreación Desde Cero

Sigue estos pasos detallados para montar, configurar e iniciar el proyecto en tu entorno local:

### 1. Preparación del Entorno

#### 1.1 Crear el directorio e iniciar el Entorno Virtual
```bash
# Entrar a la carpeta del laboratorio
cd Laboratorio_RinaMarriaga

# Crear entorno virtual venv
python -m venv venv

# Activar entorno virtual
# En Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# En Windows (CMD):
.\venv\Scripts\activate.bat
# En macOS/Linux:
source venv/bin/activate
```

#### 1.2 Instalar las dependencias
Asegúrate de que las dependencias estén actualizadas en el entorno virtual.
```bash
pip install -r requirements.txt
```
*Las librerías principales requeridas son:*
* `Django>=5.0.0`
* `google-api-python-client>=2.10.0` (Para integración de Gmail API)
* `google-auth-oauthlib>=0.5.0`
* `google-auth-httplib2>=0.1.0`
* `Pillow>=10.0.0` (Para manejo de imágenes y fotos de perfil)

---

### 2. Configuración Principal

#### 2.1 Editar `ai_project/settings.py`
El archivo de configuración ya contiene los parámetros ideales de desarrollo y servicios de correo pre-configurados:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Aplicaciones del Core
    'enrollment',
    'panel',
    'student_portal',
    'terminal',
    'notificaciones',
    'email_service',
]

# Rutas de inicio de sesión y multimedia
LOGIN_URL = '/panel/login/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de correo convencional SMTP (ejemplo con Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo_gmail@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contrasena_de_aplicacion'
DEFAULT_FROM_EMAIL = 'Academia IA <tu_correo_gmail@gmail.com>'
EMAIL_TIMEOUT = 30

# Configuración de Gmail API REST (Opcional - Prioridad si está habilitado)
GMAIL_API_ENABLED = False  # Cambiar a True para usar la API REST de Google
GMAIL_API_CREDENTIALS_FILE = BASE_DIR / 'client_secret.json'
GMAIL_API_TOKEN_FILE = BASE_DIR / 'token.json'
GMAIL_API_SCOPES = ['https://www.googleapis.com/auth/gmail.send']
```

#### 2.2 Rutas Globales (`ai_project/urls.py`)
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enrollment.urls')),
    path('panel/', include('panel.urls')),
    path('estudiantes/', include('student_portal.urls')),  # Rutas del Portal de Estudiante
    path('terminal/', include('terminal.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### 3. Aplicaciones e Implementación

#### 3.1 App `enrollment` (Registro e Inscripciones)
* **Modelos Principales:** 
  * `Course`: Título, descripción, nivel, duración, instructor e íconos.
  * `Student`: Uno a uno con el usuario de Django, almacena campos adicionales como `phone`, `address`, `profile_picture`, `status` y la contraseña autogenerada `generated_password`.
  * `CourseContent`: Secciones de explicación, ejemplos y demos asociadas al curso.
* **Flujo:** La página principal captura el registro de los estudiantes, los deja con estado `pending` y registra una alerta interna de notificación.

#### 3.2 App `panel` (Administración Central)
* Permite al personal administrativo ver un consolidado de estadísticas de estudiantes.
* Al presionar "Aceptar" en una solicitud de inscripción:
  1. Se cambia el estado del estudiante a `accepted`.
  2. Se crea un usuario de Django (`django.contrib.auth.models.User`) de forma automática.
  3. Se genera una contraseña temporal y se almacena en `student.generated_password`.
  4. Se envía un correo electrónico de bienvenida automatizado con las credenciales y enlace del portal.
* Exportación directa de toda la base de datos de estudiantes en formato CSV.

#### 3.3 App `student_portal` (El Nexus Académico de los Estudiantes)
* **Control de Acceso Seguro (Decorador):**
  ```python
  def check_password_change(view_func):
      @wraps(view_func)
      def _wrapped_view(request, *args, **kwargs):
          if hasattr(request.user, 'student') and request.user.student.generated_password:
              messages.warning(request, "PROTOCOLO DE SEGURIDAD: Debes actualizar tu contraseña inicial antes de continuar.")
              return redirect('student_change_password')
          return view_func(request, *args, **kwargs)
      return _wrapped_view
  ```
* **Manejo del Progreso (`LessonProgress`):**
  Marca el estado `completed=True` para un tema específico de un curso. Desbloquea dinámicamente el proyecto final cuando todas las lecciones del curso han sido estudiadas.
* **Lógica de Calificación:**
  El promedio del estudiante es procesado en el servidor para convertirlo a la escala estándar colombiana de `0.0` a `5.0`:
  $$\text{Nota Promedio} = \text{round}\left(\frac{\text{Promedio en Base 100}}{100} \times 5, 1\right)$$
* **Centro de Calificaciones de Talleres y Feedback:**
  * **Consola Administrativa Avanzada (Estudiante -> Curso -> Lección):** Localizada en `/panel/talleres/`, esta consola diseñada desde cero soluciona la incompatibilidad de Django Admin con Python 3.14.0. Se organiza en un flujo inteligente de 3 paneles: **Estudiante ➔ Sus Cursos Inscritos ➔ Sus Entregas por Lección**. Esto asegura que las evaluaciones se realicen de forma totalmente aislada por cada estudiante y curso (en caso de estar inscrito en más de uno), permitiendo asignar notas decimales (escala `0.0 - 5.0`) que se mapean automáticamente a base `100` en la base de datos, y dejar comentarios de retroalimentación detallados.
  * **Gestión de Estudiantes (Edición y Eliminación Segura):** Incorpora herramientas en el Dashboard administrativo para modificar la información del perfil del estudiante y matricularlo o desmatricularlo de múltiples cursos de forma interactiva mediante checkboxes. A su vez, implementa la eliminación segura en cascada (POST) para borrar simultáneamente la cuenta de acceso (`User` de Django) y la ficha del estudiante, evitando registros huérfanos en la base de datos de SQLite.
  * **Notificaciones Dinámicas (Campana Estudiantil):** Al calificar un taller, se crea un registro de notificación que activa una campana interactiva en el Dashboard del estudiante con un badge numérico en tiempo real, dropdown animado y opción de archivar.
  * **Visibilidad de Retroalimentación:** Dentro de la lección del curso (`curso.html`), el estudiante ve su calificación final y una caja de cristal esmerilado con la retroalimentación textual provista por el docente.

#### 3.4 App `email_service` (Transmisor Automatizado)
* Posee la capacidad de enrutar los envíos tanto por SMTP convencional como por la robusta API REST de Gmail utilizando credenciales de OAuth2 en formato JSON.
* Envía correos electrónicos para:
  1. Credenciales de bienvenida tras la aceptación.
  2. Notificación en caso de rechazo del registro.
  3. Alerta de seguridad inmediata tras una actualización de contraseña en el portal.

---

### 4. Migraciones y Base de Datos

Si deseas recrear o aplicar migraciones a la base de datos de SQLite, ejecuta los siguientes comandos en tu terminal con el entorno virtual activo:

```bash
# Crear archivos de migración
python manage.py makemigrations enrollment
python manage.py makemigrations student_portal
python manage.py makemigrations notificaciones
python manage.py makemigrations email_service
python manage.py makemigrations terminal

# Aplicar las migraciones a la base de datos sqlite
python manage.py migrate
```

#### Crear Superusuario (Administrador del Sistema)
```bash
python manage.py createsuperuser
```
*Sigue las instrucciones en la consola para registrar tu usuario administrativo.*

---

### 5. Semillas de Datos (Poblar la Plataforma)

Para facilitarte un entorno listo para interactuar sin necesidad de escribir cursos y exámenes a mano, hemos creado scripts automatizados de semillas dentro del proyecto. Ejecútalos en el siguiente orden para cargar contenido pedagógico y simulaciones de exámenes:

```bash
# 1. Poblar contenido temático interactivo estructurado (Python, Django, ML)
python populate_premium_full.py

# 2. Configurar el banco de preguntas estructuradas de los exámenes del curso
python setup_exam_questions.py

# 3. Estructurar temas de clases prácticos y habilitadores
python final_content_setup.py
```
Estos scripts cargarán de forma inmediata cursos completos, descripciones docentes, avatares, lecciones teóricas y prácticas, exámenes y preguntas interactivas en tu base de datos SQLite.

---

### 6. Ejecución del Servidor Local

Una vez completados los pasos anteriores, ya estás listo para levantar el servidor web de desarrollo:

```bash
python manage.py runserver
```

El servidor estará disponible en la dirección: **`http://127.0.0.1:8000/`**

#### Direcciones del Ecosistema:
* **Landing Page principal e Inscripción:** `http://127.0.0.1:8000/`
* **Portal de Estudiantes (Dashboard & Login):** `http://127.0.0.1:8000/estudiantes/login/`
* **Panel Administrativo Interno:** `http://127.0.0.1:8000/panel/login/`
* **Django Admin Convencional:** `http://127.0.0.1:8000/admin/`

---

## ✉️ Configuración de Gmail API REST (Avanzado / Opcional)

Si deseas utilizar el canal de la API REST de Gmail en lugar de SMTP convencional:

1. Ve a la consola de desarrolladores de Google Cloud: **[Google Cloud Console](https://console.cloud.google.com/)**.
2. Crea un proyecto nuevo.
3. Habilita la **Gmail API** en la sección de bibliotecas de API.
4. Dirígete a la sección de **Pantalla de Consentimiento de OAuth** (OAuth Consent Screen), configura el tipo de usuario como Externo, agrega tu correo electrónico de prueba y añade los alcances (scopes) necesarios, específicamente:
   * `https://www.googleapis.com/auth/gmail.send`
5. Crea credenciales tipo **ID de cliente de OAuth** (OAuth Client ID) para una aplicación de escritorio.
6. Descarga las credenciales en formato JSON y guárdalas con el nombre de `client_secret.json` en la raíz de `Laboratorio_RinaMarriaga`.
7. En `ai_project/settings.py`, asegúrate de cambiar `GMAIL_API_ENABLED = True`.
8. La primera vez que el sistema intente enviar un correo (por ejemplo, al aceptar un estudiante), se abrirá una ventana automática en tu navegador para realizar la autenticación de OAuth. Al conceder los permisos, se generará de manera segura el archivo de token `token.json` en la raíz del proyecto para realizar los envíos de manera 100% automatizada en el futuro.

---

## 🔒 Notas Importantes y Buenas Prácticas
* **SQLite por defecto:** La base de datos es local (`db.sqlite3`). Si deseas moverte a producción (PostgreSQL/MySQL), modifica el bloque `DATABASES` en `settings.py`.
* **Carga de Archivos Multimedia:** Todos los entregables de estudiantes y fotos de perfil son gestionados bajo el directorio `/media/`.
* **Consola Interactiva:** El emulador de la terminal de Python está integrado con controles de sesión para evitar accesos de usuarios externos no autenticados o que no pertenezcan al curso correspondiente.
* **Diseño Responsivo:** Las plantillas CSS importan el Framework moderno de tipografía de Google, optimizando la legibilidad del material pedagógico y el código dentro de la plataforma.
