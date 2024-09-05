from apps.service.models import ServiceStepValue
from rest_framework import serializers


class ServiceStepValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStepValue
        fields = ["id", "title", "image"]
