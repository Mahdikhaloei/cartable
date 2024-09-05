from apps.user.v1.views import UserViewSet
from core.apps.service.v1.views import ServiceViewSet
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register("users", UserViewSet)
router.register("services", ServiceViewSet)

app_name = "api"

urlpatterns = router.urls
