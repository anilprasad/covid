from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'foo': 'bar'})
