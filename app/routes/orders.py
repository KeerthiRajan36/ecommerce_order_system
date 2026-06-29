from fastapi import (
    APIRouter,
    Depends,
    Query
)

from sqlalchemy.orm import Session


from app.database import get_db


from app.schemas.order import (
    OrderResponse
)


from app.services.order_service import (
    create_order,
    deliver_order,
    get_orders,
    get_order_by_id,
    confirm_order,
    cancel_order
)


from app.utils.dependencies import (
    get_current_user,
    admin_required
)


from app.models.user import User



router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)



@router.post(
    "",
    response_model=OrderResponse
)
def place_order(

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return create_order(

        db,

        current_user.id

    )



@router.get("")
def list_orders(

    status:str=None,

    page:int=Query(
        1,
        ge=1
    ),

    limit:int=Query(
        10,
        ge=1
    ),

    db:Session=Depends(get_db),

    admin:User=Depends(admin_required)

):


    return get_orders(

        db,

        status,

        page,

        limit

    )





@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def order_details(

    order_id:int,

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return get_order_by_id(

        db,

        order_id

    )





@router.put(
    "/{order_id}/confirm"
)
def confirm(

    order_id:int,

    db:Session=Depends(get_db),

    admin:User=Depends(admin_required)

):


    return confirm_order(

        db,

        order_id

    )





@router.put(
    "/{order_id}/cancel"
)
def cancel(

    order_id:int,

    db:Session=Depends(get_db),

    admin:User=Depends(admin_required)

):


    return cancel_order(

        db,

        order_id

    )

@router.put(
    "/{order_id}/deliver"
)
def deliver(

    order_id:int,

    db:Session=Depends(get_db),

    admin:User=Depends(admin_required)

):


    return deliver_order(

        db,

        order_id

    )