"""
Main module
"""
from fastapi import FastAPI
from src.config.database import SessionLocal


app = FastAPI()

# Dependency to get the database session
def get_db():
    """
    Get the database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    """Read root"""
    return {"message": "Hello, BakeryOps World!"}
