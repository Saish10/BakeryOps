"""
This module defines the BaseModel model for the all apps.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Base Model
    """

    internal_id = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_("Internal ID"),
        verbose_name=_("Internal ID"),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_("Indicates whether the object is active or not"),
        verbose_name=_("Active"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time when the object was created"),
        verbose_name=_("Created At"),
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("The date and time when the object was last updated"),
        verbose_name=_("Updated At"),
        null=True,
        blank=True,
    )

    class Meta:
        """
        Meta class
        """

        abstract = True


class Country(BaseModel):
    """
    Country Model
    """

    name = models.CharField(
        max_length=255,
        help_text=_("Country name"),
        verbose_name=_("Country Name"),
    )
    numeric_code = models.CharField(
        max_length=10,
        help_text=_("Country numeric code"),
        verbose_name=_("Country Numeric Code"),
    )

    alpha2_code = models.CharField(
        max_length=2,
        help_text=_("country alpha2 code"),
        verbose_name=_("Country Alpha2 Code"),
    )

    alpha3_code = models.CharField(
        max_length=3,
        help_text=_("Country alpha3 code"),
        verbose_name=_("Country Alpha3 Code"),
    )

    isd_code = models.CharField(
        max_length=4,
        help_text=_("Country alpha3 code"),
        verbose_name=_("Country ISD Code"),
    )
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.CASCADE,
        related_name="countries",
        verbose_name=_("Currency"),
        help_text=_("Currency used in the country"),
    )

    class Meta:
        """
        Meta class for the Country model
        """

        db_table = "countries"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        """
        Returns a string representation of the country, using the name.
        """
        return str(self.name)


class State(BaseModel):
    """
    State Model
    """

    name = models.CharField(
        max_length=255,
        help_text=_("State name"),
        verbose_name=_("State Name"),
    )
    code = models.CharField(
        max_length=5,
        help_text=_("State code"),
        verbose_name=_("State Code"),
    )
    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        related_name="states",
        verbose_name=_("Country"),
        help_text=_("Country"),
    )

    class Meta:
        """
        Meta class for the State model
        """

        db_table = "states"
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        """
        Returns a string representation of the state, using the name.
        """
        return str(self.name)


class Currency(BaseModel):
    """
    Currency Model
    """

    name = models.CharField(
        max_length=255,
        help_text=_("Currency name"),
        verbose_name=_("Currency Name"),
    )
    code = models.CharField(
        max_length=3,
        help_text=_("Currency code (ISO 4217)"),
        verbose_name=_("Currency Code"),
    )
    symbol = models.CharField(
        max_length=5,
        help_text=_("Currency symbol"),
        verbose_name=_("Currency Symbol"),
    )

    class Meta:
        """
        Meta class for the Currency model
        """

        db_table = "currencies"
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")

    def __str__(self):
        """
        Returns a string representation of the currency, using the name and symbol.
        """
        return f"{self.name} ({self.symbol})"