from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enrollment.urls')),
    path('panel/', include('panel.urls')),
    path('estudiante/', include('student_portal.urls')),
    path('estudiantes/', include('student_portal.urls')),
    path('terminal/', include('terminal.urls')),
    path('notificaciones/', include('notificaciones.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
