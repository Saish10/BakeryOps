"""
This module defines the AccountsConfig class for the accounts app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    Configuration for the accounts app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
