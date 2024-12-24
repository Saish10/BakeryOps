from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Create a new database engine instance
SQLALCHEMY_DATABASE_URL = settings.DB_URL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)  # For SQLite (adjust for PostgreSQL, etc.)

# Create sessionmaker instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models to inherit from
Base = declarative_base()
