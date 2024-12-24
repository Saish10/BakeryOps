"""
Models package
"""
import os
import glob
from sqlalchemy.ext.declarative import declarative_base

# This will be used as the base class for all models
Base = declarative_base()

# Automatically import all Python files in the current directory
# This ensures that models get registered with SQLAlchemy
model_files = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
for model_file in model_files:
    if not model_file.endswith('__init__.py'):
        # Dynamically import models to ensure are registered with SQLAlchemy
        __import__(f"src.models.{os.path.basename(model_file)[:-3]}")
