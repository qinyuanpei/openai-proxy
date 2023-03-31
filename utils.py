from fastapi import status
from fastapi.responses import JSONResponse, Response  
from typing import Union

def resp_200(*, data: Union[list, dict, str]) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=data
    ) 