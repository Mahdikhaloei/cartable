from apps.service.models import ServiceStepValue
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
