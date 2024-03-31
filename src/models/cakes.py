from app import db
from .base import BaseModel


class Cake(BaseModel):
    __tablename__ = 'cake'

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(255))

    order_items = db.relationship(
        "OrderItem", backref="cake", foreign_keys='OrderItem.cake_id'
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"