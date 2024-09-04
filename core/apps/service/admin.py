from apps.service.models import ServiceStep, ServiceStepValue
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


@admin.register(ServiceStepValue)
class ServiceStepValueAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "image", )}),
        (_("Timestamp"), {"fields": ("created_at", "updated_at")}),
    )
    list_display = ("title", "created_at")
    list_filter = ("title",)
    search_fields = ("title",)
    ordering = ("pk",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(ServiceStep)
class ServiceStepAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("title", "description", "order")}),
        (_("Relations"), {"fields": ("values", )}),
        (_("Timestamp"), {"fields": ("created_at", "updated_at")}),
    )
    list_display = ("title", "created_at", "get_values")
    list_filter = ("title", "values")
    search_fields = ("title", "description")
    filter_horizontal = ("values",)
    ordering = ("order",)
    readonly_fields = ("created_at", "updated_at")

    @admin.display(description="Values")
    def get_values(self, obj):
        return obj.get_values
