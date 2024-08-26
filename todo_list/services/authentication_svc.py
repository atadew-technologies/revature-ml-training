from fastapi import Security, HTTPException, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import sessionmaker
from starlette import status

from todo_list.db.authenticate_db import AuthenticateDB
from todo_list.db.session_local import get_session

apiKeyHeader = APIKeyHeader(name="x-api-key")


class AuthenticationSVC:

    def __init__(self):
        self.session: sessionmaker = get_session()



    def authenticate(self, api_key_header: str = Security(apiKeyHeader)) -> str:

        if api_key_header != None:
            return api_key_header
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API Key",
            )
