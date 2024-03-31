import os
import logging

from logging.handlers import RotatingFileHandler
from flask import request, g
from ulid import new as generate_ulid

# Import configuration constants
from config import LOG_DIR, LOG_FILE_NAME, LOG_SIZE, LOG_BACKUP_COUNT

# Ensure LOG_DIR exists
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except OSError as e:
        print(f"Error creating log directory: {e}")

log_file = os.path.join(LOG_DIR, LOG_FILE_NAME)


# Custom filter to add correlation ID to log records
class CorrelationIdFilter(logging.Filter):
    def filter(self, record):
        # Generate or retrieve the correlation ID from the API request
        if request and request.headers:
            correlation_id = getattr(g, 'correlation_id', None)
        else:
            correlation_id = str(generate_ulid())
        record.correlation_id = correlation_id
        return True


# Configure logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Handler for rotating log files
app_handler = RotatingFileHandler(
    log_file, maxBytes=LOG_SIZE, backupCount=LOG_BACKUP_COUNT
)
app_handler.setLevel(logging.DEBUG)

# Formatter for log messages
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s - %(correlation_id)s'
)
app_handler.setFormatter(formatter)

# Add handler and filter to the logger
log.addHandler(app_handler)
log.addFilter(CorrelationIdFilter())
