from fastapi import FastAPI
from app.api import tenant

app = FastAPI()

# Include the Tenant API routes
app.include_router(tenant.router, prefix="/tenants", tags=["tenants"])
