from app import serializer
from marshmallow import fields


class AddressSchema(serializer.Schema):
    address_1 = fields.String()
    address_2 = fields.String()
    city = fields.String()
    zipcode = fields.String()
    state = fields.String()


class PhoneSchema(serializer.Schema):
    number = fields.String()
    alternate_number = fields.String()
    country = fields.String()


class RegisterSchema(serializer.Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    password = fields.String()
    address_details = AddressSchema()
    phone_details = PhoneSchema()
    is_baker = fields.Boolean()
    is_customer = fields.Boolean()
