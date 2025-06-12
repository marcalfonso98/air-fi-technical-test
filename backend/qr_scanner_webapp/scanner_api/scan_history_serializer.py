from rest_framework import serializers
from .models import ScanLog

class ScanHistorySerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = ScanLog
        fields = ['id', 'user_username', 'qr_content', 'email', 'timestamp']
        read_only_fields = ['id', 'user_username', 'qr_content', 'recipient_email', 'timestamp']