from pydantic import BaseModel, EmailStr
from typing import Optional

from app.models.user import UserRole


class UserBase(BaseModel):

    name:str

    email:EmailStr

    role:Optional[UserRole] = None


class UserCreate(UserBase):

    password:str



class UserResponse(UserBase):

    id:int

    role:UserRole

    is_active:bool


    class Config:

        from_attributes=True
