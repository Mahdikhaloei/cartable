from apps.service.models import Service
from apps.service.v1.serializers import ServiceSerializer
from core.utils.mixins.viewsets import MultipleFieldLookupMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class ServiceViewSet(MultipleFieldLookupMixin, ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ["get",]
    permission_classes = [AllowAny,]
