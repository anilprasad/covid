import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "source.settings." + os.environ.get('APP_ENVIRONMENT'))

application = get_wsgi_application()
