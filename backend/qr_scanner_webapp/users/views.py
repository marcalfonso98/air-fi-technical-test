from rest_framework import permissions, status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .user_serializer import UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from .custom_token_serializer import CustomTokenObtainPairSerializer

class UserRegistrationView(APIView):
    # Token not required here
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        # Validate all the data
        serializer.is_valid(raise_exception=True)
        
        # Create the user in the DB
        serializer.save() 
        
        return Response(
            {'message': 'Usuario creado exitosamente!'},
            status=status.HTTP_200_OK
        )
        

# Set the view
class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
