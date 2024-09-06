from apps.service.models import Request, Service
from apps.service.v1.serializers import RequestSerializer, ServiceSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from utils.mixins.viewsets import MultipleFieldLookupMixin


class ServiceViewSet(MultipleFieldLookupMixin, ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ["get",]
    permission_classes = [AllowAny,]


class RequestViewSet(MultipleFieldLookupMixin, ModelViewSet):
    queryset = Request.objects.all().order_by("-created_at")
    serializer_class = RequestSerializer
    permission_classes = [AllowAny,]

    def list(self, request, *args, **kwargs):
        current_user = request.user
        if current_user.is_superuser:
            queryset = self.queryset
        else:
            queryset = self.queryset.filter(user=current_user)
        # If you want to give access for departments you can add your scenarioes here
        return queryset
