from functools import wraps
from models.base import Utils
from logger import log
from app import db



def api_response(api_function):

    @wraps(api_function)
    def wrapper(request, *args, **kwargs):
        msg_header = request.header
        method_type = api_function.__name__.upper()
        try:
            status, status_code, message, extra = api_function(
                request, *args, **kwargs
            )
            return Utils().get_api_response(
                status, status_code, msg_header, message, extra
            )
        except Exception as e:
            log.error(f"{method_type} API | Error: {e}", exc_info=True)
            return Utils().get_api_response(
                "error", 500, str(e), msg_header, None
            )

    return wrapper


def db_transaction(func):
    """
    Decorator to manage database transactions for API endpoints.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            success, result, status_code = func(*args, **kwargs)
            if success:
                db.session.commit()
                log.info("DB transaction committed successfully.")
            else:
                db.session.rollback()
                log.error("DB transaction rolled back.")
            return result, status_code

        except Exception as e:
            db.session.rollback()
            log.error(f"Error in commit: {e}", exc_info=True)
            return "error", "Transaction failed.", 500

    return wrapper
