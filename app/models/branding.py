"""
Branding model
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel, Base


class Branding(Base, BaseModel):
    """Branding model"""

    __tablename__ = "branding"

    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    logo_url = Column(String)
    theme_color = Column(String)
    font_style = Column(String)
    tagline = Column(String)
    header_image_url = Column(String)
    footer_text = Column(Text)
    custom_css = Column(Text)

    # Relationship with Tenant (one-to-one)
    tenant = relationship("Tenant", back_populates="branding")
