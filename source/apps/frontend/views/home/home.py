from django.shortcuts import render
from django.views import View

from source.apps.core.maps import arcgis_manager
from source.apps.core.models.reports.cssegis import ReportCsseGisModel


class HomeView(View):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        maps = arcgis_manager.get_all().order_by('name')
        reports = ReportCsseGisModel.objects.all()

        return render(request, self.template_name, {
            'maps': maps,
            'reports': reports
        })
