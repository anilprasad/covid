from django.urls import re_path

from source.apps.frontend.views.maps.world import WorldMapView
from source.apps.frontend.views.maps.romania import RomaniaMapView


urlpatterns = [
    re_path(r'^world$', WorldMapView.as_view(), name='map_world'),
    re_path(r'^romania$', RomaniaMapView.as_view(), name='map_romania'),
]
