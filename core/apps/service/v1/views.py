from apps.service.models import Service
from apps.service.v1.serializers import ServiceSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from utils.mixins.viewsets import MultipleFieldLookupMixin


class ServiceViewSet(MultipleFieldLookupMixin, ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ["get",]
    permission_classes = [AllowAny,]
