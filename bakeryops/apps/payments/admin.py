"""
This module defines the admin interface for the payments app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Admin interface for the Payment model."""

    list_display = ("order", "payment_method", "amount", "status")
