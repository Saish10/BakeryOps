"""
This module defines the admin interface for the accounts app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.contrib import admin
from .models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    """
    Admin interface for the UserAccount model.
    """

    list_display = ("email", "first_name", "last_name")
    search_fields = ("email", "first_name", "last_name")
