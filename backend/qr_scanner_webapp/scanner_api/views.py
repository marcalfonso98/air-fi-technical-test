from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.mail import send_mail

from .scan_serializer import ScanSerializer
from .scan_history_serializer import ScanHistorySerializer
from .models import ScanLog

class ScanQRView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        # Verify the data
        serializer = ScanSerializer(data=request.data)
        
        # Raise exception in case of error
        serializer.is_valid(raise_exception=True)        
        
        # Extract the data
        qr_data = serializer.validated_data['qr_content']
        to_email = serializer.validated_data['to_email']
        
        # Get the username of the authenticated user
        user = request.user
        
        ScanLog.objects.create(
            user=user,
            qr_content=qr_data,
            to_email=to_email
        )
        
        # Fake mail using console.EmailBackend
        send_mail(
            f"Escáner QR de {user}",
            f'''
                Hola,\n
                Te informamos que alguien ha escaneado un código QR y quiere que lo veas.
                A continuación puedes ver la información asociada:\n
                - Contenido del QR: {qr_data}
                - Nombre de usuario: {user}\n
                Gracias,
                Equipo de Escáneres Air-Fi
            ''',
            "noreply_scanner@gmail.com", # From
            [to_email], # To
            fail_silently=False
        )
        
        return Response({"message": "Escaneo realizado correctamente!"}, status=status.HTTP_200_OK)
    
class ScanHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        query_set = ScanLog.objects.filter(user=user)#.order_by('-timestamp')
        
        # Many -> multiple items will be serialized
        serializer = ScanHistorySerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        