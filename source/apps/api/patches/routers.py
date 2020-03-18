from rest_framework import routers

from django.conf import settings
from django.utils.safestring import mark_safe


class AppAPIRootView(routers.APIRootView):
    """
    Controls appearance of the API root view
    """

    def get_view_name(self) -> str:
        return f'{getattr(settings, "APP_NAME")} API'

    def get_view_description(self, html=False) -> str:
        text = f'{getattr(settings, "APP_NAME")} API'
        if html:
            return mark_safe(f"<p>{text}</p>")
        else:
            return text


class DefaultRouter(routers.DefaultRouter):

    APIRootView = AppAPIRootView

    """
    Extends `DefaultRouter` class to add a method for extending url routes from another router.
    """
    def extend(self, router):
        self.registry.extend(router.registry)
