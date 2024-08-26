from datetime import timedelta

from fastapi import HTTPException
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware


class CustomMiddleware(BaseHTTPMiddleware):


    def __init__(self, app):
        super().__init__(app)


    async def dispatch(self, request, call_next):
        if request.headers.get('x-api-key') == "09e347bbfe4e69c9f606a3fa3391175a6ac522a8eff1da6e9f017b03ba56041":
            response = await call_next(request)
            return response
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API Key",
            )