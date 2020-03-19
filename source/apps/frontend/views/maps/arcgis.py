from django.shortcuts import render
from django.views import View

from source.apps.core.models import MapsArcgisModel


class ArcgisMapView(View):
    template_name = 'maps/arcgis.html'

    def get(self, request, *args, **kwargs):

        instance = MapsArcgisModel.objects.get(slug=kwargs.get('country'))

        return render(request, self.template_name, context={
            'map': instance
        })
