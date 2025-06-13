import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qr_scanner_webapp.settings')

application = get_wsgi_application()
