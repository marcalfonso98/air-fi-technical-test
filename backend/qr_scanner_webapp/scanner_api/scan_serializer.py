from rest_framework import serializers

class ScanSerializer(serializers.Serializer):
    qr_content = serializers.CharField(max_length=200)
    user_email = serializers.EmailField(max_length=50)