from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
    String,
    Enum
)

from sqlalchemy.orm import relationship

from app.database import Base

import enum



class PaymentStatus(str, enum.Enum):

    PENDING="pending"

    SUCCESS="success"

    FAILED="failed"




class Payment(Base):

    __tablename__="payments"



    id = Column(
        Integer,
        primary_key=True
    )


    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        unique=True
    )


    amount = Column(
        Float,
        nullable=False
    )


    payment_method = Column(
        String(50)
    )


    payment_status = Column(
        Enum(PaymentStatus),
        default=PaymentStatus.PENDING
    )



    order = relationship(
        "Order",
        back_populates="payment"
    )
