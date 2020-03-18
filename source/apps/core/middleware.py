import pytz

from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from source.apps.core.helper import get_user_geo_info_by_ip


class IpMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        get_user_geo_info_by_ip(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
