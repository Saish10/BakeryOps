import os
import base64
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


def decode(data):
    try:
        decoded_data = base64.b64decode(data).decode("utf-8")
        if decoded_data.lower() in ["no", "false"]:
            return False
        return decoded_data
    except Exception:
        return data


PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.pardir)
)

LOG_DIR = os.path.join(PROJECT_ROOT, 'logs')
LOG_FILE_NAME = (os.environ.get('DATABASE_NAME'))
LOG_BACKUP_COUNT = (os.environ.get('LOG_BACKUP_COUNT'))
LOG_SIZE = (os.environ.get('LOG_SIZE'))


CSRF_ENABLED = bool((os.environ.get('LOG_FILE_NAME')))
DEBUG = bool((os.environ.get('DEBUG')))
ENV = (os.environ.get('ENV'))
HTTP_HOST = (os.environ.get('HTTP_HOST'))

# DATABASE = {
#     'NAME': (os.environ.get('DB_NAME')),
#     'USER': (os.environ.get('DB_USER')),
#     'PASSWORD': (os.environ.get('DB_PASSWORD')),
#     'HOST': (os.environ.get('DB_HOST')),
#     'PORT': (os.environ.get('DB_PORT'))
# }
DATABASE = {
    'NAME': os.environ.get('DB_NAME'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    'HOST': os.environ.get('DB_HOST'),
    'PORT': os.environ.get('DB_PORT')
}
SQLALCHEMY_DATABASE_URI = (
    'postgresql://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s/%(NAME)s' % DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = bool(
    (os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS'))
)

# JWT_HEADER_TYPE = (os.environ.get('JWT_HEADER_TYPE'))
# JWT_ALGORITHM = (os.environ.get('JWT_ALGORITHM'))
# JWT_PRIVATE_KEY = (os.environ.get('JWT_PRIVATE_KEY'))
# JWT_PUBLIC_KEY = (os.environ.get('JWT_PUBLIC_KEY'))
# JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(
#     (os.environ.get('JWT_ACCESS_TOKEN_EXPIRES'))))
# JWT_REFRESH_TOKEN_EXPIRES = timedelta(minutes=int(
#     (os.environ.get('JWT_REFRESH_TOKEN_EXPIRES'))))

FLASK_ADMIN_SWATCH = (os.environ.get('FLASK_ADMIN_SWATCH'))
SECRET_KEY = (os.environ.get('SECRET_KEY'))



