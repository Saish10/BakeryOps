"""
Command to load all fixtures.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

import os

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to load all fixtures."""

    help = "Load all fixtures"

    def handle(self, *args, **options):
        """Command to load all fixtures."""
        # Define the fixture files to load
        fixtures = [
            "bakeryops/fixtures/currencies.json",
            "bakeryops/fixtures/countries.json",
            "bakeryops/fixtures/states.json",
        ]

        for fixture in fixtures:
            if os.path.exists(fixture):
                self.stdout.write(
                    self.style.SUCCESS(f"Loading fixture {fixture}")
                )
                call_command("loaddata", fixture)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Fixture file {fixture} does not exist")
                )
