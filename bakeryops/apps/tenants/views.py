"""
Views for tenant app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
)
from base.utility.response import APIResponse
from drf_yasg.utils import swagger_auto_schema


class TenantBrandingView(APIView):
    """
    Tenant branding view
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id="tenant_branding",
        tags=["Tenant"],
    )
    def get(self, request):
        """
        Get tenant branding
        """

        response = APIResponse.success(
            message="Tenant branding retrieved successfully"
        )
        return Response(response, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_id="tenant_branding",
        tags=["Tenant"],
    )
    def post(self, request):
        """
        Update tenant branding
        """
        response = APIResponse.success(
            message="Tenant branding updated successfully"
        )
        return Response(response, status=HTTP_200_OK)
