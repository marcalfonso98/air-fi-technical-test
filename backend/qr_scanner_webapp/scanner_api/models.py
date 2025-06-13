from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()

class ScanLog(models.Model):
    # Set the DB fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scan_logs')
    qr_content = models.TextField()
    to_email = models.EmailField()
    timestamp = models.DateTimeField(default=timezone.now)
    

    # Set the output
    def __str__(self):
        return f"USER: {self.user.email} | qr_content={self.qr_content} | TO={self.to_email} | timestamp={self.timestamp}"
        