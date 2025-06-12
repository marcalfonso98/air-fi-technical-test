from rest_framework import permissions, status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .user_serializer import UserSerializer

class UserRegistrationView(APIView):
    # Token not required here
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {'message': 'Usuario creado con éxito'},
            status=status.HTTP_200_OK
        )



# Create your views here.
