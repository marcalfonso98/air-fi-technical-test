import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr_scanner_webapp.settings')

application = get_asgi_application()
