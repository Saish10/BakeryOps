"""
This module defines the admin interface for the products app.
"""
from django.contrib import admin
from .models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for the Product model.
    """
    list_display = (
        "name",
        "description",
        "price",
    )

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for the ProductCategory model.
    """
    list_display = (
        "name",
        "description",
    )