from apps.service.models import ServiceStep, ServiceStepValue
from rest_framework import serializers


class ServiceStepValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStepValue
        fields = ["id", "title", "image"]


class ServiceStepSerializer(serializers.ModelSerializer):
    values = ServiceStepValueSerializer(many=True)

    class Meta:
        model = ServiceStep
        fields = ["id", "title", "description", "order", "values"]
