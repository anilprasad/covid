from django.urls import re_path

from source.apps.frontend.views.maps.arcgis import ArcgisMapView


urlpatterns = [
    re_path(r'^arcgis/(?P<country>[\w-]+)$', ArcgisMapView.as_view(), name='map_arcgis'),
]
