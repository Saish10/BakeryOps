"""Tenant schemas"""

from pydantic import BaseModel

class TenantBase(BaseModel):
    """Tenant schema"""
    name: str

class TenantCreate(TenantBase):
    """Tenant create schema"""


class Tenant(TenantBase):
    """Tenant class"""
    id: int

    class Config:
        """Config class"""
        orm_mode = True  # Enables ORM-to-Pydantic conversion
