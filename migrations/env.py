import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context
from app.models.base import Base

# Add the app folder to the path so we can import models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the Base and models


# this is the Alembic Config object, which provides access to
# the configuration values and methods to run migrations
config = context.config

# Use the sqlalchemy.url from the alembic.ini config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# Interpret the config file for Python logging
fileConfig(config.config_file_name)

# Set the target metadata for Alembic to auto-generate migrations
target_metadata = Base.metadata


def run_migrations_online():
    """Run migrations in 'online' mode (connected to the database)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        # Execute the migration script
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if __name__ == "__main__":
    run_migrations_online()
