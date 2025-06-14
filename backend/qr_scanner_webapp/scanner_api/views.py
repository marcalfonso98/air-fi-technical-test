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
        
        print(f"user is {request.user}")     
        
        # Extract the data
        if serializer.is_valid():
            qr_data = serializer.validated_data['qr_content']
            to_email = serializer.validated_data['to_email']
        
        try:
            # Get the username of the authenticated user
            ScanLog.objects.create(
                user=request.user,
                qr_content=qr_data,
                to_email=to_email
            )
        except Exception as e:
            print(f"Error creating ScanLog: {e}")
            return Response({"message": f"Database error creating scan log: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Fake mail using console.EmailBackend
        # if email_text --> send_email 'OK' otherwise 'KO'
        email_text = send_mail(
            f"Escáner QR de {request.user}",
            f'''
                Hola,\n
                Te informamos que alguien ha escaneado un código QR y quiere que lo veas.
                A continuación puedes ver la información asociada:\n
                - Contenido del QR: {qr_data}
                - Nombre de usuario: {request.user}\n
                Gracias,
                Equipo de Escáneres Air-Fi
            ''',
            "noreply_scanner@gmail.com", # From
            [to_email], # To Recipient
            fail_silently=False
        )
        
        return Response({"message": "Código QR enviado correctamente!", "email_sent": True if email_text else False}, status=status.HTTP_200_OK)
    
class ScanHistoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        query_set = ScanLog.objects.filter(user=user)#.order_by('-timestamp')
        
        # Many -> multiple items will be serialized
        serializer = ScanHistorySerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        