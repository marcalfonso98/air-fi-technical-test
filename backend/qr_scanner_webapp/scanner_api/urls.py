from django.urls import path
from .views import ScanQRView, ScanHistoryView

urlpatterns = [
    path('scan/', ScanQRView.as_view(), name='scan-qr'),
    path('scan-history/', ScanHistoryView.as_view(), name='scan-history'),
]
