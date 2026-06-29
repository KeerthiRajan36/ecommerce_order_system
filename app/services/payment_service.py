from sqlalchemy.orm import Session


from app.models.payment import (
    Payment,
    PaymentStatus
)

from app.models.order import Order


from app.schemas.payment import PaymentCreate


from app.exceptions.custom import (
    DuplicatePaymentException,
    InvalidPaymentException
)


def create_payment(

    db:Session,

    order_id:int,

    payment_data:PaymentCreate

):


    order=db.query(Order).filter(

        Order.id==order_id

    ).first()



    if not order:

        raise Exception(
            "Order not found"
        )



    existing=db.query(Payment).filter(

        Payment.order_id==order_id

    ).first()



    if existing:

        raise DuplicatePaymentException()



    if payment_data.amount != order.total_amount:

        raise InvalidPaymentException()



    payment=Payment(

        order_id=order_id,

        amount=payment_data.amount,

        payment_method=payment_data.payment_method,

        payment_status=PaymentStatus.SUCCESS

    )



    db.add(payment)


    db.commit()

    db.refresh(payment)



    return payment

def get_payment(

    db:Session,

    payment_id:int

):


    return db.query(Payment).filter(

        Payment.id==payment_id

    ).first()
