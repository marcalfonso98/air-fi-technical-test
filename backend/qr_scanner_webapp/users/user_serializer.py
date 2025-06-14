from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError # Mantener si se usa

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['email', 'password', 'username']
        
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Verify whether the email exists or not
    def validate_email(self, email):
        # Search for the email in the DB (exact coincidence)
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(f"El correo '{email}' ya existe, prueba con uno diferente.")
        return email

    def create(self, validated_data):
            # Extract the data before removing it
            # Important to hash the password not plain text
            password = validated_data.pop('password')
            email = validated_data.pop('email')
            username = validated_data.pop('username') 

            # Create the user
            user = User.objects.create_user(
                email=email,
                username=username, 
                password=password,
                **validated_data
            )
            return user