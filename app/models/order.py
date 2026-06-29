from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    Enum
)

from sqlalchemy.orm import relationship

from app.database import Base

import enum



class OrderStatus(str, enum.Enum):

    PENDING="pending"

    CONFIRMED="confirmed"

    CANCELLED="cancelled"

    DELIVERED="delivered"




class Order(Base):

    __tablename__="orders"


    id = Column(
        Integer,
        primary_key=True
    )


    customer_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    total_amount = Column(
        Float,
        nullable=False
    )


    order_status = Column(
        Enum(OrderStatus),
        default=OrderStatus.PENDING
    )



    customer = relationship(
        "User",
        back_populates="orders"
    )


    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete"
    )


    payment = relationship(
        "Payment",
        back_populates="order",
        uselist=False
    )



class OrderItem(Base):

    __tablename__="order_items"



    id = Column(
        Integer,
        primary_key=True
    )


    order_id = Column(
        Integer,
        ForeignKey("orders.id")
    )


    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )


    quantity = Column(
        Integer,
        nullable=False
    )


    price = Column(
        Float,
        nullable=False
    )



    order = relationship(
        "Order",
        back_populates="items"
    )


    product = relationship(
        "Product",
        back_populates="order_items"
    )
