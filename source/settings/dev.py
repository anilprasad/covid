import os

from .base import *

DEBUG = True
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = None
SESSION_COOKIE_SECURE = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ALLOWED_HOSTS

# EMAIL SETTINGS

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# MailCatcher: comment the kines below if you don't have it installed
# and use console.EmailBackend
EMAIL_HOST = os.environ.get('APP_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('APP_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('APP_EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.environ.get('APP_EMAIL_PORT', 1025)
EMAIL_USE_TLS = False

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


# STATIC FILE CONFIG
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static-dev'),
]

# django-htmlmin settings
HTML_MINIFY = False
KEEP_COMMENTS_ON_MINIFYING = False

# django-compressor
COMPRESS_ENABLED = False

# SOLR.THUMBNAIL
THUMBNAIL_DEBUG = True

# DEBUG TOOLBAR HACK FOR DOCKER
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda _request: DEBUG
}
