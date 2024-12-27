"""
Admin Reorder Configuration
"""
__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

ADMIN_REORDER = (
    # ACCOUNTS
    {
        "app": "accounts",
        "label": "User & Auth Management",
        "models": (
            "accounts.UserAccount",
        ),
    },
    # BASE
    {
        "app": "base",
        "models": (
            "base.Country",
            "base.State",
        ),
    },
    {
        "app": "tenants",
        "models": (
            "tenants.Customer",
            "tenants.Domain",
        ),
    },
)
