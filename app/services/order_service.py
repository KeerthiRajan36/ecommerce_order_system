from sqlalchemy.orm import Session


from app.models.cart import Cart
from app.models.product import Product
from app.models.order import (
    Order,
    OrderItem,
    OrderStatus
)


from app.exceptions.custom import (
    InsufficientStockException,
    ProductNotFoundException
)


def create_order(

    db:Session,

    customer_id:int

):


    cart_items = db.query(Cart).filter(

        Cart.customer_id == customer_id

    ).all()



    if not cart_items:

        raise Exception(
            "Cart is empty"
        )



    total_amount = 0



    order = Order(

        customer_id=customer_id,

        total_amount=0,

        order_status=OrderStatus.PENDING

    )



    db.add(order)

    db.commit()

    db.refresh(order)



    for item in cart_items:


        product=db.query(Product).filter(

            Product.id==item.product_id

        ).first()



        if not product:

            raise ProductNotFoundException()



        # Stock validation

        if item.quantity > product.stock:

            raise InsufficientStockException()



        item_total = (

            product.price
            *
            item.quantity

        )


        total_amount += item_total



        order_item = OrderItem(

            order_id=order.id,

            product_id=product.id,

            quantity=item.quantity,

            price=product.price

        )


        db.add(order_item)



        # Reduce stock

        product.stock -= item.quantity



        # Remove cart item

        db.delete(item)



    order.total_amount = total_amount



    db.commit()

    db.refresh(order)



    return order


def get_orders(

    db:Session,

    status=None,

    page:int=1,

    limit:int=10

):


    query=db.query(Order)



    if status:

        query=query.filter(

            Order.order_status==status

        )



    total=query.count()



    orders=query.offset(

        (page-1)*limit

    ).limit(limit).all()



    return {

        "total_records":total,

        "current_page":page,

        "limit":limit,

        "data":orders

    }


def get_order_by_id(

    db:Session,

    order_id:int

):


    order=db.query(Order).filter(

        Order.id==order_id

    ).first()



    if not order:

        raise Exception(
            "Order not found"
        )


    return order


def confirm_order(

    db:Session,

    order_id:int

):


    order=get_order_by_id(

        db,

        order_id

    )


    order.order_status = (

        OrderStatus.CONFIRMED

    )


    db.commit()

    db.refresh(order)



    return order


def cancel_order(

    db:Session,

    order_id:int

):


    order=get_order_by_id(

        db,

        order_id

    )



    for item in order.items:


        product=db.query(Product).filter(

            Product.id==item.product_id

        ).first()



        product.stock += item.quantity



    order.order_status = (

        OrderStatus.CANCELLED

    )



    db.commit()

    db.refresh(order)



    return order

def deliver_order(

    db:Session,

    order_id:int

):


    order=get_order_by_id(

        db,

        order_id

    )



    for item in order.items:


        product=db.query(Product).filter(

            Product.id==item.product_id

        ).first()



        product.stock += item.quantity



    order.order_status = (

        OrderStatus.DELIVERED

    )



    db.commit()

    db.refresh(order)



    return order
