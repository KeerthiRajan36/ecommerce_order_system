from pydantic import BaseModel, Field



class ProductCreate(BaseModel):

    name:str = Field(
        min_length=2,
        max_length=150
    )


    description:str | None=None


    price:float = Field(
        gt=0
    )


    stock:int = Field(
        ge=0
    )


    category:str



class ProductUpdate(BaseModel):

    name:str | None=None

    description:str | None=None

    price:float | None=Field(
        default=None,
        gt=0
    )

    stock:int | None=Field(
        default=None,
        ge=0
    )

    category:str | None=None



class ProductResponse(BaseModel):

    id:int

    name:str

    description:str | None

    price:float

    stock:int

    category:str

    is_active:bool


    class Config:

        from_attributes=True
