from django.urls import re_path

from source.apps.frontend.views.reports.country import ReportsCountryView


urlpatterns = [
    re_path(r'^(?P<country>[\w-]+)$', ReportsCountryView.as_view(), name='reports_country'),
]
