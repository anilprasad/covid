from rest_framework import routers

from source.apps.api.common.views import CommonViewSet

router = routers.SimpleRouter()
router.register(r'common', CommonViewSet, basename='common')
