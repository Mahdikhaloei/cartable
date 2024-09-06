from apps.service.models import Request, Service, ServiceStep, ServiceStepValue
from apps.user.v1.serializers import UserSerializer
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


class ServiceSerializer(serializers.ModelSerializer):
    steps = ServiceStepSerializer(many=True)

    class Meta:
        model = Service
        fields = ["id", "title", "excerpt", "description", "image", "order", "steps"]


class RequestSerializer(serializers.ModelSerializer):
    status = ServiceStepSerializer()
    service = ServiceSerializer()
    creator = UserSerializer()
    user = UserSerializer()

    class Meta:
        model = Request
        fields = [
            "id",
            "status",
            "service",
            "creator",
            "user",
            "tracking_code",
            "data",
            "viewed_by_admin",
            "created_at",
            "updated_at"
        ]
