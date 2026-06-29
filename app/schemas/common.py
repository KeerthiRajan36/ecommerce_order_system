from pydantic import BaseModel

from typing import Generic,TypeVar,List



T=TypeVar("T")



class PaginationResponse(
    BaseModel,
    Generic[T]
):

    total_records:int

    current_page:int

    limit:int

    data:List[T]
