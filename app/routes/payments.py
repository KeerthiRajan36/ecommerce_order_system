from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from app.database import get_db


from app.schemas.payment import (
    PaymentCreate,
    PaymentResponse
)


from app.services.payment_service import (
    create_payment,
    get_payment
)


from app.utils.dependencies import (
    get_current_user
)


from app.models.user import User



router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)



@router.post(
    "/{order_id}",
    response_model=PaymentResponse
)
def make_payment(

    order_id:int,

    data:PaymentCreate,

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return create_payment(

        db,

        order_id,

        data

    )





@router.get(
    "/{payment_id}",
    response_model=PaymentResponse
)
def payment_details(

    payment_id:int,

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return get_payment(

        db,

        payment_id

    )
