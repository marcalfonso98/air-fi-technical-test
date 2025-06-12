from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

# Create your models here.
class ScanLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scan_logs')
    qr_content = models.TextField()
    email = models.EmailField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"user={self.user.username} | qr_content={self.qr_content} | email={self.email} | timestamp={self.timestamp}"
        