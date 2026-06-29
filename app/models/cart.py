from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base



class Cart(Base):

    __tablename__="cart"


    id = Column(
        Integer,
        primary_key=True
    )


    customer_id = Column(
        Integer,
        ForeignKey("users.id")
    )


    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )


    quantity = Column(
        Integer,
        default=1
    )


    customer = relationship(
        "User",
        back_populates="cart_items"
    )


    product = relationship(
        "Product",
        back_populates="cart_items"
    )
