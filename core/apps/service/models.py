from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.mixins.models import Sortable, Timestampable


class ServiceStepValue(Timestampable):
    title = models.CharField(_("title"), max_length=255)
    image = models.ImageField(_("image"), upload_to="services/step_values", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = _("Service Step Value")
        verbose_name_plural = _("Service Step Values")


class ServiceStep(Timestampable, Sortable):
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
