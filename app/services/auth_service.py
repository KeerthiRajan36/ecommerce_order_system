from sqlalchemy.orm import Session

from app.models.user import User,UserRole

from app.schemas.user import UserCreate

from app.schemas.auth import LoginRequest

from app.utils.security import (
    hash_password,
    verify_password
)

from app.utils.jwt import create_access_token

from app.exceptions.custom import (
    UserAlreadyExistsException,
    UserNotFoundException
)



def register_user(
    db:Session,
    user_data:UserCreate
):


    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()



    if existing_user:

        raise UserAlreadyExistsException()



    new_user = User(

        name=user_data.name,

        email=user_data.email,

        password=hash_password(
            user_data.password
        ),

        role=user_data.role if user_data.role else UserRole.CUSTOMER

    )


    db.add(new_user)

    db.commit()

    db.refresh(new_user)



    return new_user





def login_user(
    db:Session,
    login_data:LoginRequest
):


    user = db.query(User).filter(
        User.email == login_data.email
    ).first()



    if not user:

        raise UserNotFoundException()



    valid_password = verify_password(
        login_data.password,
        user.password
    )



    if not valid_password:

        raise Exception(
            "Invalid credentials"
        )



    token=create_access_token(

        {
            "sub":user.email,

            "role":user.role.value

        }

    )



    return token
