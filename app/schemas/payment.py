from pydantic import BaseModel, Field

from app.models.payment import PaymentStatus




class PaymentCreate(BaseModel):

    amount:float = Field(
        gt=0
    )


    payment_method:str



class PaymentResponse(BaseModel):

    id:int

    order_id:int

    amount:float

    payment_method:str

    payment_status:PaymentStatus


    class Config:

        from_attributes=True
