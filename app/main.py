from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi.exceptions import RequestValidationError

import logging


from app.database import Base, engine

from app.config import settings


from app.exceptions.custom import AppException

from app.exceptions.handlers import (
    app_exception_handler,
    validation_exception_handler
)


from app.routes.auth import router as auth_router
from app.routes.products import router as product_router
from app.routes.carts import router as cart_router
from app.routes.orders import router as order_router
from app.routes.payments import router as payment_router





Base.metadata.create_all(
    bind=engine
)



app = FastAPI(

    title=settings.PROJECT_NAME,
)


app.add_exception_handler(
    AppException,
    app_exception_handler
)


app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)





app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


logging.basicConfig(

    filename="app/logs/app.log",

    level=logging.INFO,

    format=
    "%(asctime)s %(levelname)s %(message)s"

)




app.include_router(

    auth_router,

    prefix="/api/v1"

)


app.include_router(

    product_router,

    prefix="/api/v1"

)


app.include_router(

    cart_router,

    prefix="/api/v1"

)


app.include_router(

    order_router,

    prefix="/api/v1"

)


app.include_router(

    payment_router,

    prefix="/api/v1"

)



@app.get("/")
def home():

    return {

        "message":
        "E-Commerce API Running",

        "version":
        "1.0.0"

    }
