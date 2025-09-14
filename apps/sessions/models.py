from django.db import models
from django.utils import timezone
from datetime import timedelta
import uuid

def default_expires_at():
    return timezone.now() + timezone.timedelta(days=14)

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='sessions')
    session_key = models.CharField(max_length=40, unique=True)
    expires_at = models.DateTimeField(default=default_expires_at)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return self.expires_at < timezone.now()

    def __str__(self):
        return f"Session for {self.user.nom} (Expires: {self.expires_at.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        app_label = 'custom_sessions'
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        ordering = ['-expires_at']
