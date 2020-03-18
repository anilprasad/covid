from rest_framework import routers

from source.apps.api.auth.views import AuthViewSet

router = routers.SimpleRouter()
router.register(r'auth', AuthViewSet, basename='auth')
