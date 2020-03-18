from .base import *

DEBUG = True
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None

ALLOWED_HOSTS = []

# CORS
CORS_ORIGIN_WHITELIST = ()

# EMAIL SETTINGS
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('APP_DB_NAME', 'app_dev'),
        'USER': os.environ.get('APP_DB_USER', 'root'),
        'PASSWORD': os.environ.get('APP_DB_PASSWORD', None),
        'HOST': os.environ.get('APP_DB_HOST', '192.168.33.11'),
        'PORT': os.environ.get('APP_DB_PORT', '3306'),
    }
}
