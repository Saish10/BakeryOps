"""
CRUD operations for tenants
"""

from sqlalchemy.orm import Session
from app.models.tenant import TenantModel
from app.schemas.tenant import TenantCreate


def create_tenant(db: Session, tenant: TenantCreate):
    """Create a new tenant"""
    db_tenant = TenantModel(name=tenant.name)
    db.add(db_tenant)
    db.commit()
    db.refresh(db_tenant)
    return db_tenant


def get_tenant(db: Session, tenant_id: int):
    """
    Get a tenant by ID
    """
    return db.query(TenantModel).filter(TenantModel.id == tenant_id).first()


def get_all_tenants(db: Session, skip: int = 0, limit: int = 10):
    """
    Get all tenants
    """
    return db.query(TenantModel).offset(skip).limit(limit).all()
