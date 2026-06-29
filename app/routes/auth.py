from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session


from app.database import get_db


from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)


from app.services.auth_service import (
    register_user,
    login_user
)
from app.utils.dependencies import get_current_user



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post(
    "/register",
    response_model=UserResponse
)
def register(

    user:UserCreate,

    db:Session=Depends(get_db)

):


    return register_user(

        db,

        user

    )





@router.post(
    "/login",
    response_model=TokenResponse
)
def login(

    data:LoginRequest,

    db:Session=Depends(get_db)

):


    token=login_user(

        db,

        data

    )


    return {

        "access_token":token,

        "token_type":"bearer"

    }


@router.get("/users")
def get_profile(
    db:Session=Depends(get_db)
):
    users = db.query(User).all()

    return users