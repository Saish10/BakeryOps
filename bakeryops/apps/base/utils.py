"""
Utilities for the base app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from .models import Country, State


class CountryManager:
    """
    Returns a queryset of all countries
    """

    def __init__(self, request):
        self.request = request
        self.search = self.request.query_params.get("search")

    def get_countries(self):
        """Returns a queryset of all countries."""
        countries = (
            Country.objects.filter(name__istartswith=self.search)
            if self.search
            else Country.objects.all()
        )
        return countries.order_by("name")


class StateManager:
    """
    Returns a queryset of all states
    """

    def __init__(self, request):
        self.request = request
        self.search = self.request.query_params.get("search")
        self.country = self.request.query_params.get("country_id")

    def get_states(self):
        """Returns a queryset of all states."""
        filters = {}
        if self.search:
            filters["name__istartswith"] = self.search
        if self.country:
            filters["country__internal_id"] = self.country
        return (
            State.objects.filter(**filters)
            .order_by("name")
            .select_related("country")
        )
