from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship

from app.database import Base

import enum



class UserRole(str, enum.Enum):

    ADMIN = "admin"

    CUSTOMER = "customer"



class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String(100),
        nullable=False
    )


    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )


    password = Column(
        String(255),
        nullable=False
    )


    role = Column(
        Enum(UserRole),
        default=UserRole.CUSTOMER
    )


    is_active = Column(
        Boolean,
        default=True
    )





    cart_items = relationship(
        "Cart",
        back_populates="customer",
        cascade="all, delete"
    )


    orders = relationship(
        "Order",
        back_populates="customer"
    )
