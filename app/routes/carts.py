from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from app.database import get_db


from app.schemas.cart import (
    CartAddRequest,
    CartResponse
)


from app.services.cart_service import (
    add_to_cart,
    get_cart,
    remove_from_cart
)


from app.utils.dependencies import (
    get_current_user
)


from app.models.user import User



router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)



@router.post(
    "/add",
    response_model=CartResponse
)
def add_cart_item(

    data:CartAddRequest,

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return add_to_cart(

        db,

        current_user.id,

        data

    )





@router.get("")
def view_cart(

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return get_cart(

        db,

        current_user.id

    )





@router.delete(
    "/remove/{product_id}"
)
def delete_cart_item(

    product_id:int,

    db:Session=Depends(get_db),

    current_user:User=Depends(get_current_user)

):


    return remove_from_cart(

        db,

        current_user.id,

        product_id

    )
