from django.conf import settings
from django.core.exceptions import DisallowedHost
from django.db import connection
from django.http import Http404, HttpResponseNotFound
from django.urls import set_urlconf
from django.utils.deprecation import MiddlewareMixin
from django_tenants.utils import (
    remove_www,
    get_public_schema_name,
    get_tenant_types,
    has_multi_type_tenants,
    get_tenant_domain_model,
    get_public_schema_urlconf,
)


class TenantMainMiddleware(MiddlewareMixin):
    TENANT_NOT_FOUND_EXCEPTION = Http404
    """
    This middleware should be placed at the very top of the middleware stack.
    Selects the proper database schema using the request host. Can fail in
    various ways which is better than corrupting or revealing data.
    """

    @staticmethod
    def hostname_from_request(request):
        """Extracts hostname from request. Used for custom requests filtering.
        By default removes the request's port and common prefixes.
        """
        print("request.get_host()", request.get_host())
        return remove_www(request.get_host().split(":")[0])

    def get_tenant(self, domain_model, hostname):
        if hostname.endswith("localhost"):
            subdomain = (
                "public" if hostname == "localhost" else hostname.split(".")[0]
            )
            domain = domain_model.objects.select_related("tenant").get(
                tenant__schema_name=subdomain
            )
        else:
            domain = domain_model.objects.select_related("tenant").get(
                domain=hostname
            )
        return domain

    def process_request(self, request):
        """Processes a request and selects the tenant and domain."""
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.

        connection.set_schema_to_public()
        try:
            hostname = self.hostname_from_request(request)
        except DisallowedHost:
            return HttpResponseNotFound()

        domain_model = get_tenant_domain_model()
        try:
            domain = self.get_tenant(domain_model, hostname)
        except domain_model.DoesNotExist:
            self.no_tenant_found(request, hostname)
            return

        domain.tenant.domain_url = hostname
        request.tenant = domain.tenant
        # request.entity = domain
        connection.set_tenant(request.tenant)
        self.setup_url_routing(request)

    def no_tenant_found(self, request, hostname):
        """What should happen if no tenant is found.
        This makes it easier if you want to override the default behavior"""
        if (
            hasattr(settings, "SHOW_PUBLIC_IF_NO_TENANT_FOUND")
            and settings.SHOW_PUBLIC_IF_NO_TENANT_FOUND
        ):
            self.setup_url_routing(request=request, force_public=True)
        else:
            raise self.TENANT_NOT_FOUND_EXCEPTION(
                f"No tenant for hostname {hostname}"
            )

    @staticmethod
    def setup_url_routing(request, force_public=False):
        """
        Sets the correct url conf based on the tenant
        :param request:
        :param force_public
        """
        public_schema_name = get_public_schema_name()
        if has_multi_type_tenants():
            tenant_types = get_tenant_types()
            if not hasattr(request, "tenant") or (
                (
                    force_public
                    or request.tenant.schema_name == get_public_schema_name()
                )
                and "URLCONF" in tenant_types[public_schema_name]
            ):
                request.urlconf = get_public_schema_urlconf()
            else:
                tenant_type = request.tenant.get_tenant_type()
                request.urlconf = tenant_types[tenant_type]["URLCONF"]
            set_urlconf(request.urlconf)

        else:
            # Do we have a public-specific urlconf?
            if hasattr(settings, "PUBLIC_SCHEMA_URLCONF") and (
                force_public
                or request.tenant.schema_name == get_public_schema_name()
            ):
                request.urlconf = settings.PUBLIC_SCHEMA_URLCONF


