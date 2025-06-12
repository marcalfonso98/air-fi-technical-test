from rest_framework import serializers
from django.contrib.auth.models import User # Importa el modelo User de Django
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        
        # Fields for the register
        fields = ['username', 'email', 'password']
        
        
        def validate_email(self, email):
            if User.objects.filter(email__iexact=email).exists():
                raise serializers.ValidationError(f"El correo '{email}' ya existe, prueba con otro.")
        
        def create(self, data):
            # **data -> to obtain each key-value
            user = User.objects.create_user(**data)
            return user