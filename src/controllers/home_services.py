from fastapi import status
from fastapi.responses import JSONResponse


def home_api():
    return JSONResponse(
        content={"message": "This is task home route"}, status_code=status.HTTP_200_OK
    )
