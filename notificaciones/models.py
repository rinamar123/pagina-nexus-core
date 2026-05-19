from django.db import models

class Notification(models.Model):
    NOTIF_TYPES = [
        ('info',    'Información'),
        ('success', 'Éxito'),
        ('warning', 'Advertencia'),
        ('error',   'Error'),
    ]
    student    = models.ForeignKey('enrollment.Student', on_delete=models.CASCADE, related_name='notifications')
    title      = models.CharField(max_length=200, default='Notificación')
    message    = models.TextField(blank=True, default='')
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES, default='info')
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.student.name}"

    class Meta:
        ordering = ['-created_at']
        db_table = 'enrollment_notification'

class AdminNotification(models.Model):
    NOTIF_TYPES = [
        ('info',    'Información'),
        ('success', 'Éxito'),
        ('warning', 'Advertencia'),
        ('error',   'Error'),
        ('diploma', 'Solicitud de Diploma'),
    ]
    title      = models.CharField(max_length=200, default='Notificación Administrativa')
    message    = models.TextField(blank=True, default='')
    notif_type = models.CharField(max_length=20, choices=NOTIF_TYPES, default='info')
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link       = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"ADMIN: {self.title}"

    class Meta:
        ordering = ['-created_at']
