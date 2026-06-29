from pydantic import BaseModel

from app.models.order import OrderStatus



class OrderCreate(BaseModel):

    pass



class OrderItemResponse(BaseModel):

    product_id:int

    quantity:int

    price:float


    class Config:

        from_attributes=True




class OrderResponse(BaseModel):

    id:int

    customer_id:int

    total_amount:float

    order_status:OrderStatus

    items:list[OrderItemResponse]


    class Config:

        from_attributes=True
