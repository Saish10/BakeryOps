"""
Notification models
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from base.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(BaseModel):
    """
    Notification model
    """

    user = models.ForeignKey(
        "accounts.UserAccount",
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    message = models.TextField(
        verbose_name=_("Message"),
    )
    read_at = models.DateTimeField(null=True, blank=True)
    notification_type = models.CharField(
        max_length=20,
        choices=[
            ("order_update", "Order Update"),
            ("promotion", "Promotion"),
            ("reminder", "Reminder"),
            ("system", "System"),
            ("announcement", "Announcement"),
        ],
        default="order_update",
    )

    def __str__(self):
        return f"Notification #{self.id}"

    class Meta:
        """
        Meta class for Notification model
        """

        db_table = "notifications"
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
