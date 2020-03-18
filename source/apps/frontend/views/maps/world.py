from django.shortcuts import render
from django.views import View


class WorldMapView(View):
    template_name = 'maps/world.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
