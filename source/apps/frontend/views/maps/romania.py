from django.shortcuts import render
from django.views import View


class RomaniaMapView(View):
    template_name = 'maps/romania.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
