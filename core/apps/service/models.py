import time

from apps.user.forms import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.mixins.models import Sortable, Timestampable


class ServiceStepValue(Timestampable):
    """
    Service Step Value model for Cartable.
    """
    title = models.CharField(_("title"), max_length=255)
    image = models.ImageField(_("image"), upload_to="services/step_values", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = _("Service Step Value")
        verbose_name_plural = _("Service Step Values")


class ServiceStep(Timestampable, Sortable):
    """
    Service Step model for Cartable.
    """
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), null=True,blank=True)
    values = models.ManyToManyField(ServiceStepValue, verbose_name=_("values"), related_name="steps", blank=True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.title}"

    class Meta:
        ordering = ["order"]
        verbose_name = _("Service Step")
        verbose_name_plural = _("Service Steps")

    @property
    def get_values(self) -> list[str]:
        return [str(value) for value in self.values.all()]


class Service(Timestampable, Sortable):
    """
    Service model for Cartable.
    """
    title = models.CharField(_("title"), max_length=255)
    excerpt = models.CharField(_("excerpt"), max_length=255, null=True, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)
    image = models.ImageField(_("image"), upload_to="services/", null=True, blank=True)
    steps = models.ManyToManyField(ServiceStep, verbose_name=_("steps"), related_name="services", blank=True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.title}"

    class Meta:
        ordering = ["order"]
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    @property
    def get_steps(self) -> list[str]:
        return [str(step) for step in self.steps.all()]


class ServiceStatus(Timestampable):
    """
    Servie Status model for Cartable.
    """
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), null=True, blank=True)
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service_statuses",
        verbose_name=_("service")
    )

    def __str__(self) -> str:
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = _("Request Status")
        verbose_name_plural = _("Request Statuses")


class Request(Timestampable):
    """
    Request model for Cartable.
    """
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="requests",
        verbose_name=_("service")
    )
    status = models.ForeignKey(
        ServiceStatus,
        on_delete=models.CASCADE,
        related_name="requests",
        verbose_name=_("status")
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_requests",
        verbose_name=_("creator"),
        null=True,
        blank=True
    ),
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="requests",
        verbose_name=_("user")
    )
    tracking_code = models.CharField(_("reacking code"), max_length=255, null=True, blank=True)
    data = models.JSONField(_("data"), null=True, blank=True)
    viewed_by_admin = models.BooleanField(_("viewed by admin"), default=False)

    def __str__(self) -> str:
        return f"Request: {self.tracking_code} - {self.service} - {self.user}"

    def save(self, *args, **kwargs):
        if not self.tracking_code:
            self.tracking_code = self.generate_tracking_code()
        super().save(*args, **kwargs)

    def change_status_alert(self, status):
        pass

    def generate_tracking_code(self):
        timestamp = int(time.time())
        tracking_code = f"{timestamp}-{self.id}"
        return tracking_code

    class Meta:
        verbose_name = _("Request")
        verbose_name_plural = _("Requests")
