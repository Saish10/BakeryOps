from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import tenant as crud
from app.schemas import tenant as schemas
from app.dependencies.db import SessionLocal

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new tenant
@router.post("/", response_model=schemas.Tenant)
def create_tenant(tenant: schemas.TenantCreate, db: Session = Depends(get_db)):
    return crud.create_tenant(db=db, tenant=tenant)

# Endpoint to get a tenant by ID
@router.get("/{tenant_id}", response_model=schemas.Tenant)
def read_tenant(tenant_id: int, db: Session = Depends(get_db)):
    return crud.get_tenant(db=db, tenant_id=tenant_id)

# Endpoint to get all tenants
@router.get("/", response_model=list[schemas.Tenant])
def read_tenants(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_tenants(db=db, skip=skip, limit=limit)
