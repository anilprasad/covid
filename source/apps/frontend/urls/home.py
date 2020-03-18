from django.urls import re_path

from source.apps.frontend.views.home import home


urlpatterns = [
    re_path(r'^$', home.HomeView.as_view(), name='home'),
]
