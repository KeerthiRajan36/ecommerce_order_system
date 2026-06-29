from fastapi import (
    APIRouter,
    Depends,
    Query
)


from sqlalchemy.orm import Session


from app.database import get_db


from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)


from app.services.product_service import (
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product
)


from app.utils.dependencies import (
    admin_required
)



router = APIRouter(
    prefix="/products",
    tags=["Products"]
)



@router.post(
    "",
    response_model=ProductResponse
)
def add_product(

    product:ProductCreate,

    db:Session=Depends(get_db),

    admin=Depends(admin_required)

):


    return create_product(

        db,

        product

    )



@router.get("")
def list_products(

    category:str=None,

    page:int=Query(
        1,
        ge=1
    ),

    limit:int=Query(
        10,
        ge=1,
        le=100
    ),

    db:Session=Depends(get_db)

):


    return get_products(

        db,

        category,

        page,

        limit

    )





@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def product_details(

    product_id:int,

    db:Session=Depends(get_db)

):


    return get_product(

        db,

        product_id

    )





@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def edit_product(

    product_id:int,

    data:ProductUpdate,

    db:Session=Depends(get_db),

    admin=Depends(admin_required)

):


    return update_product(

        db,

        product_id,

        data

    )





@router.delete(
    "/{product_id}"
)
def remove_product(

    product_id:int,

    db:Session=Depends(get_db),

    admin=Depends(admin_required)

):


    return delete_product(

        db,

        product_id

    )
