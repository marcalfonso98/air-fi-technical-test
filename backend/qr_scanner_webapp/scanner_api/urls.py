from django.urls import path, include
from .views import ScanQR, ScanHistory

urlpatterns = [
    path('scan/', ScanQR.as_view(), name='scan-qr'),
    path('scan-history/', ScanHistory.as_view(), name='scan-history'),
]
