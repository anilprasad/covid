from django.urls import re_path

from source.apps.frontend.views.maps.arcgis import ArcgisMapView
from source.apps.frontend.views.maps.self import SelfMapView


urlpatterns = [
    re_path(r'^self/$', SelfMapView.as_view(), name='map_self'),
    re_path(r'^arcgis/(?P<country>[\w-]+)$', ArcgisMapView.as_view(), name='map_arcgis'),
]
