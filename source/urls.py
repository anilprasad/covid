from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    re_path(r'^jet/', include('jet.urls', 'jet')),
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    re_path(r'^%s/' % settings.APP_ADMIN_PATH, admin.site.urls),
    re_path(r'^api/v1/', include('source.apps.api.urls')),
    re_path('summernote/', include('django_summernote.urls')),
]

urlpatterns += i18n_patterns(
    re_path(
        r'^jsi18n/$',
        JavaScriptCatalog.as_view(domain='djangojs'),
        name='javascript-catalog'
    ),
    re_path(r'^', include('source.apps.frontend.urls.home')),
    re_path(r'^reports/', include('source.apps.frontend.urls.reports')),
    re_path(r'^maps/', include('source.apps.frontend.urls.maps')),
    re_path(r'^account/', include('source.apps.frontend.urls.account')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'source.apps.core.views.handler400'
handler404 = 'source.apps.core.views.handler404'
handler403 = 'source.apps.core.views.handler403'
handler500 = 'source.apps.core.views.handler500'
