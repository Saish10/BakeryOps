"""
This module defines the BaseConfig class for the base app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.apps import AppConfig


class BaseConfig(AppConfig):
    """
    Configuration for the base app.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "base"
