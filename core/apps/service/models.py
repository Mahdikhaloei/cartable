from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.mixins.models import Sortable, Timestampable


class ServiceStepValue(Timestampable):
    title = models.CharField(_("title"), max_length=255)
    image = models.ImageField(_("image"), upload_to="service/step_value", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.pk}: {self.value}"

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
        verbose_name = _("Service Step")
        verbose_name_plural = _("Service Steps")
