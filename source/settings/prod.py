from .base import *

DEBUG = False
ALLOWED_HOSTS = ['covid.social']

# Compressor
COMPRESS_ENABLED = False

# django-htmlmin settings
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = False

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
