"""Tenant model"""

from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.orm import relationship
from .base import BaseModel, Base


class TenantModel(Base, BaseModel):
    """Tenant model"""

    __tablename__ = "tenants"

    name = Column(String, index=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # Relationship with Branding (one-to-one)
    branding = relationship("Branding", back_populates="tenant", uselist=False)
