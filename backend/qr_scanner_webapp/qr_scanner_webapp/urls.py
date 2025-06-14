from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import CustomTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Token routes
    path('api/token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('scanner_api.urls')),
    path('api/', include('users.urls')),
]
