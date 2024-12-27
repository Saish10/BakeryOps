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


# class Branding(BaseModel):
#     """
#     Branding model for each tenant.
#     Stores branding-related information like logo, theme colors, etc.
#     """

#     tenant = models.OneToOneField(
#         Tenant,
#         on_delete=models.CASCADE,
#         related_name="branding",
#         verbose_name=_("Tenant"),
#         help_text=_("The tenant this branding belongs to."),
#     )
#     tagline = models.CharField(
#         max_length=255,
#         null=True,
#         blank=True,
#         help_text=_("Tagline for the tenant's branding"),
#         verbose_name=_("Tagline"),
#     )
#     logo = models.ImageField(
#         upload_to="branding/logos/",
#         null=True,
#         blank=True,
#         help_text=_("Logo image for the tenant's branding"),
#         verbose_name=_("Logo"),
#     )
#     primary_color = models.CharField(
#         max_length=7,
#         default="#000000",
#         help_text=_("Primary theme color for the tenant (e.g., #ff5733)"),
#         verbose_name=_("Primary Color"),
#     )
#     secondary_color = models.CharField(
#         max_length=7,
#         null=True,
#         blank=True,
#         help_text=_("Secondary theme color for the tenant (e.g., #33c1ff)"),
#         verbose_name=_("Secondary Color"),
#     )
#     background_color = models.CharField(
#         max_length=7,
#         null=True,
#         blank=True,
#         help_text=_(
#             "Background color for the tenant's branding (e.g., #ffffff)"
#         ),
#         verbose_name=_("Background Color"),
#     )
#     font_family = models.CharField(
#         max_length=255,
#         null=True,
#         blank=True,
#         help_text=_("Font family used in the tenant's branding"),
#         verbose_name=_("Font Family"),
#     )

#     class Meta:
#         """
#         Meta class for the Branding model.
#         """
#         db_table = "branding"
#         verbose_name = _("Branding")
#         verbose_name_plural = _("Brandings")

#     def __str__(self):
#         return f"Branding for {self.tenant.name}"
