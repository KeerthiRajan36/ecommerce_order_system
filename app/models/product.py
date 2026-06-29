from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean
)

from sqlalchemy.orm import relationship

from app.database import Base



class Product(Base):

    __tablename__="products"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(150),
        unique=True,
        nullable=False
    )


    description = Column(
        String(500)
    )


    price = Column(
        Float,
        nullable=False
    )


    stock = Column(
        Integer,
        default=0
    )


    category = Column(
        String(100),
        nullable=False
    )


    is_active = Column(
        Boolean,
        default=True
    )



    cart_items = relationship(
        "Cart",
        back_populates="product"
    )


    order_items = relationship(
        "OrderItem",
        back_populates="product"
    )
