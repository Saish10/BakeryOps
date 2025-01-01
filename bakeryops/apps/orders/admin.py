"""
This module defines the admin interface for the orders app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for the Order model.
    """

    list_display = ("id", "status", "created_at")
    list_filter = ("status",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin interface for the OrderItem model.
    """

    list_display = ("id", "quantity", "unit_price", "total_price")
