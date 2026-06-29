from fastapi import Depends,HTTPException,status

from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials

from sqlalchemy.orm import Session


from app.database import get_db

from app.utils.jwt import decode_access_token

from app.models.user import User ,UserRole



security = HTTPBearer()



def get_current_user(

    credential:HTTPAuthorizationCredentials=Depends(security),

    db:Session=Depends(get_db)

):
    token = credential.credentials

    payload=decode_access_token(token)



    if not payload:

        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid Token"

        )


    email=payload.get("sub")



    user=db.query(User).filter(
        User.email==email
    ).first()



    if not user:

        raise HTTPException(

            status_code=404,

            detail="User not found"

        )


    return user


def admin_required(

    current_user:User=Depends(get_current_user)

):


    if current_user.role != UserRole.ADMIN:


        raise HTTPException(

            status_code=403,

            detail="Admin access required"

        )


    return current_user
