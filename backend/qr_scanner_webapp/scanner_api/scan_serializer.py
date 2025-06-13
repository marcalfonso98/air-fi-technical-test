from rest_framework import serializers

class ScanSerializer(serializers.Serializer):
    # Fields conditions
    qr_content = serializers.CharField(max_length=200)
    to_email = serializers.EmailField(max_length=50)