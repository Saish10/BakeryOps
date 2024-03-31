from functools import wraps
import logging
from typing import Tuple

from flask import jsonify
from sqlalchemy.types import TypeDecorator, CHAR
from ulid import new as generate_ulid
from app import db
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from logger import log


class ULIDType(TypeDecorator):
    impl = CHAR(26)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            return str(value)

    def process_result_value(self, value, dialect):
        if value is not None:
            return value


class UpdateMixin:

    def update(self, attributes):
        """
        Update multiple attributes with their new values.
        :param attribute_dict: A dictionary where keys are attribute names and
            values are new values.
        :return: True if the update is successful, False otherwise.
        """
        for attribute_name, new_value in attributes.items():
            if hasattr(self, attribute_name):
                setattr(self, attribute_name, new_value)
            else:
                return False
        db.session.flush()
        return True


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    internal_id = db.Column(
        ULIDType, unique=True, index=True, default=lambda: str(generate_ulid())
    )
    is_active = db.Column(db.Boolean(), server_default="true", index=True)
    created_date = db.Column(db.DateTime(), server_default=datetime.now())
    updated_date = db.Column(db.DateTime(), onupdate=datetime.now())
    created_by_id = db.Column(db.String(500), nullable=True, index=True)
    updated_by_id = db.Column(db.String(500), nullable=True, index=True)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"


class Currency(BaseModel):
    __tablename__ = 'currency'

    name = db.Column(db.String(200), nullable=True)
    alpha_3 = db.Column(db.String(200), nullable=True)
    symbol = db.Column(db.String(200), nullable=True)

    country = db.relationship(
        'Country', backref='Currency', foreign_keys='Country.currency'
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.alpha_3}"

    @classmethod
    def get_currency(cls, **criteria):
        return cls.query.filter_by(**criteria, is_active=True)


class Country(BaseModel):
    __tablename__ = 'country'

    name = db.Column(db.String(100), nullable=True)
    isd_code = db.Column(db.String(100), nullable=True)
    alpha2_code = db.Column(db.String(50), nullable=True)
    alpha3_code = db.Column(db.String(50), nullable=True)
    numeric_code = db.Column(db.String(50), nullable=True)
    currency = db.Column(db.Integer, db.ForeignKey('currency.id'))

    states = db.relationship(
        "State", backref="country", foreign_keys="State.state"
    )
    phone_numbers = db.relationship(
        "PhoneNumber", backref="country", foreign_keys="PhoneNumber.country"
    )


    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    @classmethod
    def get_country(cls, **criteria):
        return cls.query.filter_by(**criteria, is_active=True)


class State(BaseModel):
    __tablename__ = 'state'

    name = db.Column(db.String(200), nullable=True)
    iso_code = db.Column(db.String(200), nullable=True)
    country = db.Column(db.Integer, db.ForeignKey('country.id'))

    state_addresses =db.relationship(
        'Address', backref='state', foreign_keys='Address.state'
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    @classmethod
    def get_state(cls, **criteria):
        return cls.query.filter_by(**criteria, is_active=True)


class PhoneNumber(BaseModel):
    __tablename__ = 'phone_number'

    number = db.Column(db.String(200), nullable=True)
    alternate_number = db.Column(db.String(200), nullable=True)
    country = db.Column(db.Integer, db.ForeignKey('country.id'))

    user_phone_numbers = db.relationship(
        "User", backref="phone_number", foreign_keys=('User.phone_number')
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.number}"

    @classmethod
    def get_number(cls, **criteria):
        return cls.query.filter_by(**criteria, is_active=True)

    @classmethod
    def create(cls, data):
        try:
            country = Country.get_country(name=data.get('country')).first()
            number = cls(
                number=data.get('number'),
                alternate_number=data.get('alternate_number'),
                country=country.id
            )
            db.session.add(number)
            db.session.flush()
            return number
        except Exception as e:
            log.error(f'Error in PhoneNumber - create : {e}',exc_info=True)
            db.session.rollback()
            return None


class Address(BaseModel):
    __tablename__ = 'address'

    address_1 = db.Column(db.String(500), nullable=True)
    address_2 = db.Column(db.String(500), nullable=True)
    city = db.Column(db.String(500), nullable=True)
    zipcode = db.Column(db.String(500), nullable=True)
    state = db.Column(db.Integer, db.ForeignKey('state.id'))

    user_address = db.relationship(
        "User", backref="address", foreign_keys=('User.address')
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"

    @classmethod
    def get_address(cls, **criteria):
        return cls.query.filter_by(**criteria, is_active=True)

    @classmethod
    def create(cls, data):
        try:
            state = State.get_state(name=data.get('state')).first()
            address = cls(
                address_1 = data.get('address_1'),
                address_2 = data.get('address_2'),
                city = data.get('city'),
                zipcode = data.get('zipcode'),
                state = state.id
            )
            db.session.add(address)
            db.session.flush()
            return address
        except Exception as e:
            log.error(f'Error in Address - create : {e}', exc_info=True)
            db.session.rollback()
            return None


class Utils:

    def __init__(self):
        super().__init__()

    def get_api_response(self, status, status_code, header, msg, data=None):
        response = {
            "status": status,
            "status_code": status_code,
            "message_header": header,
            "message": msg,
        }
        if data is not None:
            response["data"] = data

        return jsonify(response)
