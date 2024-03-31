from app import db
from .base import BaseModel, Address, PhoneNumber
from logger import log
from constants import ERROR_MSG

class User(BaseModel):
    __tablename__ = 'user'

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.Integer, db.ForeignKey('phone_number.id'))
    address = db.Column(db.Integer, db.ForeignKey('address.id'))
    is_baker = db.Column(db.Boolean(), server_default="false", index=True)
    is_customer = db.Column(db.Boolean(), server_default="false", index=True)

    orders = db.relationship(
        "Order", backref="user", foreign_keys=('Order.customer')
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.email}"

    @classmethod
    def signup(cls, data: dict) -> tuple[bool, str]:
        """
        Create a new user object with the provided data.

        Args:
            data (dict): A dictionary containing the user's details.

        Returns:
            tuple[bool, str]: A tuple indicating if the user creation process
            was successful and a message.
        """
        try:
            address = Address.create(data.get('address_details'))
            number = PhoneNumber.create(data.get('phone_details'))
            user = cls(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                password=data.get('password'),
                email=data.get('email'),
                address=address.id,
                phone_number=number.id,
                is_baker=data.get('is_baker'),
                is_customer=data.get('is_customer')
            )
            db.session.add(user)
            db.session.flush()
            return True, 'User created successfully.'
        except Exception as e:
            log.error(f'Error in User - signup: {e}', exc_info=True)
            return False, ERROR_MSG
