import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_MAIL = os.environ.get('APP_SERVER_MAIL')
EMAIL_HOST = os.environ.get('APP_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('APP_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('APP_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('APP_DEFAULT_FROM_EMAIL')
EMAIL_PORT = os.environ.get('APP_EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
