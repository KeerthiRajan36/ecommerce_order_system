class AppException(Exception):

    def __init__(
        self,
        message:str,
        status_code:int=400
    ):

        self.message = message

        self.status_code = status_code



class UserAlreadyExistsException(AppException):

    def __init__(self):

        super().__init__(
            message="Email already registered",
            status_code=400
        )



class UserNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            message="User not found",
            status_code=404
        )



class ProductNotFoundException(AppException):

    def __init__(self):

        super().__init__(
            message="Product not found",
            status_code=404
        )



class ProductAlreadyExistsException(AppException):

    def __init__(self):

        super().__init__(
            message="Product already exists",
            status_code=400
        )



class InsufficientStockException(AppException):

    def __init__(self):

        super().__init__(
            message="Insufficient product stock",
            status_code=400
        )



class InvalidPaymentException(AppException):

    def __init__(self):

        super().__init__(
            message="Payment validation failed",
            status_code=400
        )



class DuplicatePaymentException(AppException):

    def __init__(self):

        super().__init__(
            message="Payment already exists",
            status_code=400
        )
