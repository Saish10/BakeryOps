"""Base model for all models"""

from datetime import datetime

import ulid
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.types import CHAR, TypeDecorator

from app.dependencies.db import Base


class ULIDType(TypeDecorator):
    """
    A custom SQLAlchemy type decorator for handling ULID (Universally Unique
    Lexicographically Sortable Identifier) fields in a database.
    """

    impl = CHAR(26)  # ULID is a 26-character string
    cache_ok = True

    def process_bind_param(self, value, dialect):
        """
        Converts the ULID value to a string for database storage.
        """
        if value is not None:
            return str(value)

    def process_result_value(self, value, dialect):
        """
        Processes ULID values retrieved from the database,
        ensuring they are in the correct string format.
        """
        if value is not None:
            return value

    @staticmethod
    def generate_ulid():
        """Generates a new ULID."""
        return ulid.new()


class BaseModel:
    """Base class for all models"""

    __abstract__ = True  # Make it an abstract base class

    # Default columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    internal_id = Column(
        ULIDType, unique=True, index=True, default=ULIDType.generate_ulid
    )
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
