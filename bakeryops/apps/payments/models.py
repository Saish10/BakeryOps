"""
Payments app models
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import BaseModel


class PaymentStatus(models.TextChoices):
    """
    Payment status choices for a cake order website.
    """
    PAID = "paid", _("Paid")
    PARTIALLY_PAID = "partially_paid", _("Partially Paid")
    FAILED = "failed", _("Failed")
    REFUNDED = "refunded", _("Refunded")
    PENDING = "pending", _("Pending")
    CANCELLED = "cancelled", _("Cancelled")


class Payment(BaseModel):
    """
    Payment model
    """

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="payments",
    )
    payment_method = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        choices=[
            ("CASH", _("Cash")),
            ("CARD", _("Card")),
            ("UPI", _("UPI")),
        ],
        verbose_name=_("Payment Method"),
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name=_("Amount"),
    )
    status = models.CharField(
        max_length=255,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
        null=False,
        blank=False,
        verbose_name=_("Payment Status"),
    )
    payment_date = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("Payment Date"),
    )

    class Meta:
        """
        Meta class
        """
        db_table = "payments"
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        """
        Returns a string representation of the payment.
        """
        return str(self.id)
