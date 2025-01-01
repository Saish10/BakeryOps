"""
Tenants models
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_tenants.models import TenantMixin, DomainMixin

from base.models import BaseModel


class Tenant(TenantMixin):
    """
    Tenant Model
    """

    name = models.CharField(
        max_length=255,
        help_text=_("Enter a Tenant name"),
        verbose_name=_("Tenant Name"),
    )
    email = models.EmailField(
        unique=True,
        db_index=True,
        verbose_name=_("Email Address"),
        help_text=_("Enter a valid email address (e.g., example@domain.com)."),
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Meta class
        """

        db_table = "tenant"
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"


class Domain(DomainMixin):
    """
    Tenant domain model for the Customer app.
    """

    class Meta:
        """
        Meta class for the Tenant domain model.
        """

        db_table = "domain"
        verbose_name = "Tenant Domain"
        verbose_name_plural = "Tenant Domains"


class Branding(BaseModel):
    """
    Tenant branding model
    """

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="branding"
    )
    tagline = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Tagline")
    )
    logo = models.ImageField(
        upload_to="branding/logo",
        null=True,
        blank=True,
        verbose_name=_("Logo")
    )
    favicon = models.ImageField(
        upload_to="branding/favicon",
        null=True,
        blank=True,
        verbose_name=_("Favicon")
    )
    primary_color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Primary Color")
    )
    secondary_color = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Secondary Color"),
    )
    font_family = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Font Family")
    )

    class Meta:
        """
        Meta class for the Tenant branding model.
        """

        db_table = "branding"
        verbose_name = "Branding"
        verbose_name_plural = "Brandings"

    def __str__(self):
        return f"Branding : {self.tenant.name}"
