"""
URLs for the base app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.urls import path
from .views import CountryListView, StateListView

urlpatterns = [
    path("countries/", CountryListView.as_view(), name="country-list"),
    path("states/", StateListView.as_view(), name="state-list"),
]
