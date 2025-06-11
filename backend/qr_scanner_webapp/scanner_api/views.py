from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .scan_serializer import ScanSerializer
from django.core.mail import send_mail

# Create your views here.
class ScanQR(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request, format=None):
        # Verify the data
        serializer = ScanSerializer(data=request.data)
        
        # Raise exception in case of error
        serializer.is_valid(raise_exception=True)        
        
        # Extract the data
        qr_data = serializer.validated_data['qr_content']
        user_email = serializer.validated_data['user_email']
        
        # Get the username of the authenticated user
        user = request.user
        
        mail = send_mail(
            "Resumen Escaneo QR",
            f'''
                Hola {user},\n\n
                Te informamos que has realizado un escáner con éxito y 
                a continuación tienes la información asociada:\n
                Contenido del QR: {qr_data}
                Nombre de usuario: {user}\n
                Gracias,
                Equipo de Escáneres Air-Fi
            ''',
            "noreply_scanner@gmail.com", # From
            ["malfonso621@gmail.com"], # To
            fail_silently=False
        )
        

        
        return Response({"message": "Scan API Works"})