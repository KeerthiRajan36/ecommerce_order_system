from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


from app.exceptions.custom import AppException



async def app_exception_handler(

    request:Request,

    exc:AppException

):


    return JSONResponse(

        status_code=exc.status_code,

        content={

            "success":False,

            "message":exc.message,

            "path":request.url.path

        }

    )





async def validation_exception_handler(

    request:Request,

    exc:RequestValidationError

):


    return JSONResponse(

        status_code=422,

        content={

            "success":False,

            "message":"Validation Error",

            "errors":exc.errors()

        }

    )
