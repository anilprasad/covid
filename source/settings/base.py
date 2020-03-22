import os
import sys
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, '../fixtures/')
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# APP SPECIFIC SETTINGS
APP_NAME = os.environ.get('APP_NAME')
APP_FRONTEND_URL = os.environ.get("APP_FRONTEND_URL", None)
APP_ADMIN_PATH = os.environ.get("APP_ADMIN_PATH", "admin")

# SECURITY SETTINGS
X_FRAME_OPTIONS = 'SAMEORIGIN'
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = None
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECRET_KEY = os.environ.get('APP_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# User and authentication
AUTH_USER_MODEL = 'core.User'
AUTHENTICATION_BACKENDS = [
    'source.apps.core.backends.user.backends.AuthBackend',
    'django.contrib.auth.backends.ModelBackend',
]
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
PASSWORD_RESET_TIMEOUT_DAYS = 3
LOGIN_URL = 'login'
ADMIN_EMAILS = (
    'rada.calin@gmail.com',
)

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Application definition

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'collectfast',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.forms',
    'django_celery_beat',
    'debug_toolbar',
    'sorl.thumbnail',
    'compressor',
    # 'captcha',
    'django_summernote',

    'django_filters',
    'vinaigrette',
    'corsheaders',
    'leaflet',
    'widget_tweaks',

    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',

    'source.apps.hreflang',
    'source.apps.inlinecss',
    'source.apps.core',
    'source.apps.api',
    'source.apps.frontend',
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'source.apps.core.middleware.IpMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
]

ROOT_URLCONF = 'source.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'source.apps.frontend.context_processors.global_settings',
            ],
        },
    },
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

WSGI_APPLICATION = 'source.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('ro', _('Romanian')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '{0}/{1}.log'.format(os.path.join(BASE_DIR, 'logs'), datetime.today().strftime("%Y-%m-%d")),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# CACHE SETTINGS
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('APP_REDIS', 'redis://redis:6379/0'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": os.environ.get("APP_NAME")
    }
}

# CACHE TTL
CACHE_TTL = 60 * 15

# SESSION
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_NAME = str(APP_NAME).lower()
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

DEFAULT_FILE_STORAGE = 'source.s3utils.MediaStorage'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_URL = '/static/'
STATICFILES_LOCATION = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static-dev'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

# Media files (UGC)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
MEDIAFILES_LOCATION = 'media/'

# AWS S3 Settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_HOST = os.environ.get('AWS_S3_HOST', 's3-eu-central-1.amazonaws.com')
AWS_S3_STATICFILES_LOCATION = 'static'
AWS_S3_MEDIAFILES_LOCATION = 'media'
AWS_DEFAULT_ACL = None
APP_USE_S3_STORAGE = os.environ.get('APP_USE_S3_STORAGE')

if APP_USE_S3_STORAGE == '1':
    # Static file config to be used with AWS S3
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    COMPRESS_STORAGE = 'source.s3utils.CachedS3BotoStorage'
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"

    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_S3_STATICFILES_LOCATION)
    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_S3_MEDIAFILES_LOCATION)
    COMPRESS_URL = STATIC_URL

    DEFAULT_FILE_STORAGE = 'source.s3utils.MediaStorage'

    MEDIAFILES_LOCATION = AWS_S3_MEDIAFILES_LOCATION
    STATICFILES_LOCATION = AWS_S3_STATICFILES_LOCATION

    CLOUDFRONT_DOMAIN = os.environ.get('AWS_CLOUDFRONT_DOMAIN')
    CLOUDFRONT_ID = os.environ.get('AWS_CLOUDFRONT_ID')
    AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN
    AWS_DEFAULT_ACL = None

    os.environ['S3_USE_SIGV4'] = 'True'

# Collectfast
AWS_PRELOAD_METADATA = True
COLLECTFAST_THREADS = 50

# django-htmlmin settings
HTML_MINIFY = not DEBUG
KEEP_COMMENTS_ON_MINIFYING = False


ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# CORS
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:3000',
)

from .partial.rest_framework import *
from .partial.email import *
from .partial.celery import *
from .partial.jet_dashboard import *
from .partial.sorl_thumbnail import *
from .partial.summernote import *
from .partial.google import *
from .partial.leaflet import *
from .partial.geoip import *
