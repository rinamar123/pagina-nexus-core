import uuid
from django.db import models
from django.contrib.auth.models import User

class AdminRequest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_request')
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Solicitud de {self.user.username}"
