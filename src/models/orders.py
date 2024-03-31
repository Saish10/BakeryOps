from .base import BaseModel
from app import db


class Order(BaseModel):
    __tablename__ = 'order'

    ORDER_STATUS = [
        ('pending', "Pending"),
        ('processing', "Processing"),
        ('ready_for_pickup', "Ready for Pickup"),
        ('out_for_delivery', "Out for Delivery"),
        ('delivered', "Delivered"),
        ('cancelled', "Cancelled"),
        ('on_hold', "On Hold"),
    ]

    customer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    delivery_date = db.Column(db.DateTime)
    status = db.Column(db.ChoiceType(ORDER_STATUS), nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)

    order_items = db.relationship(
        "OrderItem", backref="order", foreign_keys = 'OrderItem.order'
    )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"

    @classmethod
    def get_order(cls, **criteria):
        return cls.query.filter_by(**criteria)

    @classmethod
    def create_order(cls, **data):
        order = cls(**data)
        db.session.add(order)
        db.session.flush()
        return order


class OrderItem(BaseModel):
    __tablename__ = 'order_item'

    order = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    cake_id = db.Column(db.Integer, db.ForeignKey('cake.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal_price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}"

    @classmethod
    def get_order_item(cls, **criteria):
        return cls.query.filter_by(**criteria)

    @classmethod
    def create_order_item(cls, **data):
        order_item = cls(**data)
        db.session.add(order_item)
        db.session.flush()
        return order_item
