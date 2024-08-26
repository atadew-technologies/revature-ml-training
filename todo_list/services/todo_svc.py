from fastapi import Depends, HTTPException
from sqlalchemy.orm import sessionmaker
from starlette import status

from todo_list.db.authenticate_db import AuthenticateDB
from todo_list.db.session_local import get_session
from todo_list.db.todo_db import TodoDB


class TodoSVC:

    def __init__(self, session: sessionmaker = Depends(get_session)):
        self.session = session

    def getTodoList(self):
        todo = TodoDB(self.session)
        response =  todo.getTodoList()
        print(response)
        return response

    def authenticate(self, api_key_header):
        auth = AuthenticateDB(self.session)
        key = auth.getAPIKey(api_key_header)
        if key == None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API Key",
            )
        if api_key_header == key.api_key:
            return True
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or missing API Key",
            )

