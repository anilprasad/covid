from django.shortcuts import render
from django.views import View

from source.apps.core.models import MapsArcgisModel


class SelfMapView(View):
    """
    This view renders map for self checked case: home isolated,
    confirmed (covid confirmed case)
    """
    template_name = 'maps/self.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, context={
            'map': ''
        })
