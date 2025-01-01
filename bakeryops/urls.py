"""
URL configuration for law_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SchemaView = get_schema_view(
    openapi.Info(
        title="Bakery Ops",
        default_version="v1",
        description="Bakery Ops",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "",
        include(("base.urls", "base"), namespace="base"),
    ),
    path(
        "account/",
        include(("accounts.urls", "accounts"), namespace="accounts"),
    ),
    path(
        "product/",
        include(("products.urls", "products"), namespace="products"),
    ),
    path(
        "order/",
        include(("orders.urls", "orders"), namespace="orders"),
    ),
    path(
        "payment/",
        include(("payments.urls", "payments"), namespace="payments"),
    ),
    path(
        "notification/",
        include(
            ("notifications.urls", "notifications"), namespace="notifications"
        ),
    ),
    path(
        "dashboard/",
        include(("dashboard.urls", "dashboard"), namespace="dashboard"),
    ),
    path(
        "report/",
        include(("reports.urls", "reports"), namespace="reports"),
    ),
]
