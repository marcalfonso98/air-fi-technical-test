from django.urls import path, include
from .views import ScanQR

urlpatterns = [
    path('scan/', ScanQR.as_view(), name='scan-qr')  ,  
]
