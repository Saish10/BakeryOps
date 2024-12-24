"""
Configuration for Alembic migrations
"""
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Import the Base from models/__init__.py
from src.models import Base
from src.config.database import engine

# Import all models automatically by loading them from models/__init__.py
import src.models  # will load all models defined in the models folder

config = context.config

# Load environment variables from .env
load_dotenv()

# Set up the database URL for Alembic
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Add your model's metadata here (Base.metadata)
target_metadata = Base.metadata

def run_migrations_online():
    """Run migrations"""
    connectable = engine.connect()

    with connectable:
        context.configure(
            connection=connectable,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()
