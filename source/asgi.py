import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "source.settings." + os.environ.get('APP_ENVIRONMENT'))

application = get_asgi_application()
