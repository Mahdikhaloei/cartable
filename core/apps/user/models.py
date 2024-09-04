from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.mixins.models import UUIDPrimaryKeyMixin


class UserRole(models.TextChoices):
    ADMIN = "admin", _("Admin")
    USER = "user", _("User")


class User(AbstractUser, UUIDPrimaryKeyMixin):
    """
    Default custom user model for Cartable.
    """
    # Due to this open issue of mypy, we ignore this error
    # https://github.com/typeddjango/django-stubs/issues/433
    username = None  # type: ignore
    email = models.EmailField(_("email address"), blank=True, unique=True)
    role = models.CharField(max_length=5, choices=UserRole.choices, default=UserRole.USER)
    auth0_access_token = models.CharField(max_length=2048, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.email
