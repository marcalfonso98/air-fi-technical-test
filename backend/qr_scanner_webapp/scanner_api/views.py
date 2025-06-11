from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .scan_serializer import ScanSerializer

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
        
        # Get the validated user
        user = request.user
        
        return Response({"message": "Scan API Works"})