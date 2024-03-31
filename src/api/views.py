from flask import request
from flask.views import MethodView
from app import swagger, app
from flask_restx import Resource
from marshmallow import ValidationError

from decorators import api_response, db_transaction
from .serializers import RegisterSchema
from models.users import User


class Register(Resource, MethodView):

    @swagger.doc(security='Bearer')
    @swagger.expect(RegisterSchema)
    @db_transaction
    @api_response
    def post(self):
        """
        Handles the POST request to register a new user.
        """
        try:
            data = RegisterSchema().load(request.get_json())
        except ValidationError as e:
            return 'error', e.messages, 400, {}

        success, message = User.signup(data)
        if not success:
            return 'error', message, 400, {}
        return 'success', message, 200, {}

