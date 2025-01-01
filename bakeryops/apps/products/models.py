"""
Products app models
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel


class ProductCategory(BaseModel):
    """
    Product category model
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )

    class Meta:
        """
        Meta class
        """
        db_table = "product_categories"
        verbose_name = _("Product Category")
        verbose_name_plural = _("Product Categories")

class Product(BaseModel):
    """
    Product model
    """
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price"),
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("Category"),
    )

    class Meta:
        """
        Meta class
        """
        db_table = "products"
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
