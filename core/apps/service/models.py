from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.mixins.models import Timestampable


class Service(Timestampable):
    """
    Service model for Cartable project.
    """
    title = models.CharField(_("title"), max_length=255)
    excerpt = models.CharField(_("excerpt"), max_length=255, null=True, blank=True)
    description = models.TextField(_("description"), null=True, blank=True)
    image = models.ImageField(_("image"), upload_to="services/", null=True, blank=True)

    def __str__(self):
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
