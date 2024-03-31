from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_restx import Api, apidoc
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from config import DEBUG


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug = DEBUG
CORS(app)

jwt = JWTManager(app)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
serializer = Marshmallow(app)

url_prefix = '/bakery-ops'
swagger_desc = "API documentation for BakeryOps"

apidoc.apidoc.url_prefix = url_prefix
swagger = Api(
    app,
    version='v1.0',
    title='Bakeryops',
    description=swagger_desc,
    doc=f'{url_prefix}/swagger/',
    authorizations={
        'Bearer': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    prefix=url_prefix
)


