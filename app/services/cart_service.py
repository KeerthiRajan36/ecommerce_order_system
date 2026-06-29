from sqlalchemy.orm import Session

from app.models.cart import Cart
from app.models.product import Product

from app.schemas.cart import CartAddRequest

from app.exceptions.custom import (
    ProductNotFoundException,
    InsufficientStockException
)



def add_to_cart(
    db:Session,
    customer_id:int,
    cart_data:CartAddRequest
):

    product=db.query(Product).filter(
        Product.id==cart_data.product_id
    ).first()



    if not product:
        raise ProductNotFoundException()



    if not product.is_active:

        raise Exception(
            "Product inactive"
        )



    if cart_data.quantity > product.stock:

        raise InsufficientStockException()



    existing=db.query(Cart).filter(

        Cart.customer_id==customer_id,

        Cart.product_id==cart_data.product_id

    ).first()



    if existing:


        total_quantity = (
            existing.quantity
            +
            cart_data.quantity
        )


        if total_quantity > product.stock:

            raise InsufficientStockException()



        existing.quantity=total_quantity

        db.commit()

        db.refresh(existing)

        return existing



    item=Cart(

        customer_id=customer_id,

        product_id=cart_data.product_id,

        quantity=cart_data.quantity

    )


    db.add(item)

    db.commit()

    db.refresh(item)


    return item





def get_cart(

    db:Session,

    customer_id:int

):


    return db.query(Cart).filter(

        Cart.customer_id==customer_id

    ).all()





def remove_from_cart(

    db:Session,

    customer_id:int,

    product_id:int

):


    item=db.query(Cart).filter(

        Cart.customer_id==customer_id,

        Cart.product_id==product_id

    ).first()



    if not item:

        raise Exception(
            "Cart item not found"
        )



    db.delete(item)

    db.commit()



    return {

        "message":
        "Removed successfully"

    }
