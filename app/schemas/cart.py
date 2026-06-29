from pydantic import BaseModel, Field



class CartAddRequest(BaseModel):

    product_id:int


    quantity:int = Field(
        gt=0
    )




class CartResponse(BaseModel):

    id:int

    product_id:int

    quantity:int


    class Config:

        from_attributes=True
