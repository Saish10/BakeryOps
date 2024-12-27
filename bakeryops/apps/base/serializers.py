"""
Serializers for the base app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from rest_framework import serializers
from .models import Country, State


class CountrySerializer(serializers.ModelSerializer):
    """Serializer for Country model"""

    class Meta:
        """Class Meta"""

        model = Country
        fields = [
            "id",
            "internal_id",
            "name",
            "numeric_code",
            "alpha2_code",
            "alpha3_code",
            "isd_code",
            "currency",
        ]


class StateSerializer(serializers.ModelSerializer):
    """Serializer for State model"""

    class Meta:
        """Class Meta"""

        model = State
        fields = [
            "id",
            "name",
            "code",
        ]
