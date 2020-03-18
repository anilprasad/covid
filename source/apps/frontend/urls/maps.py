from django.urls import re_path

from source.apps.frontend.views.maps.world import WorldMapView


urlpatterns = [
    re_path(r'^world$', WorldMapView.as_view(), name='map_world'),
]
