"""
Base views
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from base.utility.response import APIResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from .serializers import CountrySerializer, StateSerializer
from .utils import CountryManager, StateManager


class CountryListView(APIView):
    """
    List countries with Django filter functionality
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["BASE"],
        operation_id="country_list",
        operation_description="Retrieve a list of countries.",
        operation_summary="Retrieve a list of countries.",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search for countries by name.",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get(self, request):
        """
        List all countries
        """
        queryset = CountryManager(request).get_countries()
        serializer = CountrySerializer(queryset, many=True)
        response = APIResponse.success(
            "Country list retrieved successfully", serializer.data
        )
        return Response(response, status=HTTP_200_OK)


class StateListView(APIView):
    """
    List states with Django filter functionality
    """

    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=["BASE"],
        operation_id="state_list",
        operation_description="Retrieve a list of states.",
        operation_summary="Retrieve a list of states.",
        manual_parameters=[
            openapi.Parameter(
                "country_id",
                openapi.IN_QUERY,
                description="Filter states by country ID.",
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_UUID,
                required=True,
            ),
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search for states by name.",
                type=openapi.TYPE_STRING,
            ),
        ],
    )
    def get(self, request):
        """
        List all states
        """
        queryset = StateManager(request).get_states()
        serializer = StateSerializer(queryset, many=True)
        response = APIResponse.success(
            "State list retrieved successfully", serializer.data
        )
        return Response(response, status=HTTP_200_OK)
