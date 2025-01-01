"""
Products app models
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel


class OrderStatus(models.TextChoices):
    """
    Order status choices for a cake order website.
    """

    PENDING = "pending", _("Pending")
    CONFIRMED = "confirmed", _("Confirmed")
    BAKING = "baking", _("Baking")
    READY = "ready", _("Ready for Pickup/Delivery")
    OUT_FOR_DELIVERY = "out_for_delivery", _("Out for Delivery")
    DELIVERED = "delivered", _("Delivered")
    CANCELLED = "cancelled", _("Cancelled")
    REFUNDED = "refunded", _("Refunded")


class Order(BaseModel):
    """
    Order model
    """
    order_by = models.ForeignKey(
        "accounts.UserAccount",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    status = models.CharField(
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
        max_length=20,
        verbose_name=_("Order Status"),
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Total Price"),
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Order Date"),
    )
    delivery_date = models.DateTimeField(
        null=True,
        verbose_name=_("Delivery Date"),
    )
    other_instructions = models.TextField(
        null=True,
        verbose_name=_("Other Instructions"),
    )

    class Meta:
        """
        Meta class
        """
        db_table = "orders"
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(BaseModel):
    """
    Order item model
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="order_items",
    )
    quantity = models.IntegerField(
        verbose_name=_("Quantity"),
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Unit Price")
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Total Price")
    )

    class Meta:
        """
        Meta class
        """
        db_table = "order_items"
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"Order Item #{self.id}"
