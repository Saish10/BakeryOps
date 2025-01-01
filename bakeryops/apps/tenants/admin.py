"""Admin interface for the Tenant and Domain models."""

from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Branding, Tenant, Domain


@admin.register(Tenant)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    """Admin interface for the Customer model."""

    list_display = ("name", "schema_name", "email")
    search_fields = ("name", "email")
    readonly_fields = ("schema_name",)


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """Admin interface for the Domain model."""

    list_display = ("domain", "tenant", "is_primary")
    search_fields = ("domain", "tenant__name")

@admin.register(Branding)
class BrandingAdmin(admin.ModelAdmin):
    """Admin interface for the Branding model."""

    list_display = ("tenant", "tagline", "primary_color", "secondary_color")
