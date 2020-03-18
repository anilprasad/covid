from django.conf import settings

from source.version import VERSION


def global_settings(request):
    return {
        'APP_NAME': settings.APP_NAME,
        'APP_DEBUG': settings.DEBUG,
        'APP_FRONTEND_URL': settings.APP_FRONTEND_URL,
        'public_url': settings.APP_FRONTEND_URL,
        'ASSETS_VERSION': VERSION,
    }
