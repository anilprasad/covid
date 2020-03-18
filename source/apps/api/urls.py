from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import re_path, include
from django.conf import settings

# from source.apps.api.swagger_schema import SwaggerSchemaView
from source.apps.api.patches.routers import DefaultRouter
from source.apps.api.common.urls import router as common_router
from source.apps.api.auth.urls import router as auth_router


schema_view = get_schema_view(
    openapi.Info(
        title=getattr(settings, 'APP_NAME') + ' API',
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=getattr(settings, 'ADMIN_EMAILS', 'name@example.com')),
        license=openapi.License(name="Trade secret"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

router = DefaultRouter()
router.extend(auth_router)
router.extend(common_router)

urlpatterns = [
    re_path(r'', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # re_path(r'^docs/', SwaggerSchemaView.as_view()),
    # re_path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
