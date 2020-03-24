from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from source.apps.core.models.reports.cssegis import ReportCsseGisModel


class ReportsCountryView(View):
    template_name = 'reports/country.html'

    def get(self, request, *args, **kwargs):
        country = kwargs.get('country', 'us').replace('-',' ')
        page = request.GET.get('page', 1)
        reports = ReportCsseGisModel.objects.filter(Q(country__iexact=country)).order_by('-confirmed', 'state')
        paginator = Paginator(reports, 201)

        try:
            output = paginator.page(page)
        except PageNotAnInteger:
            output = paginator.page(1)
        except EmptyPage:
            output = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {
            'reports': output
        })
