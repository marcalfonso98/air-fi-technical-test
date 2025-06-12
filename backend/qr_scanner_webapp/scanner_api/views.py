from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.mail import send_mail

from .scan_serializer import ScanSerializer
from .scan_history_serializer import ScanHistorySerializer
from .models import ScanLog

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
        
        scan_log = ScanLog.objects.create(
            user=user,
            qr_content=qr_data,
            email=user_email
        )
        
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
        
        print(scan_log)

        
        return Response({"message": "Escaneo ralizado correctamente!"}, status=status.HTTP_200_OK)
    
class ScanHistory(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        query_set = ScanLog.objects.filter(user=user)#.order_by('-timestamp')
        
        # Many -> multiple items will be serialized
        serializer = ScanHistorySerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        