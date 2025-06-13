from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

# Custom token to use the EMAIL as the USERNAME 
# Due to TokenObtainPair that by default uses "username, password"
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.username_field] = serializers.CharField(write_only=True)
        self.fields.pop('username', None)

    def validate(self, attrs):
        email = attrs.get(self.username_field)
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("No puede haber ningún campo vacío.", code='no_credentials')
        
        # Authenticate the user
        user = authenticate(request=self.context.get('request'), username=email, password=password)
        
        if not user:
            raise serializers.ValidationError(f"No existe ningún usuario con las credenciales indicadas.", code='invalid_credentials')

        if not user.is_active:
            raise serializers.ValidationError(f"La cuenta de {user} está inactiva", code='inactive_account')

        data = super().validate(attrs)

        return data