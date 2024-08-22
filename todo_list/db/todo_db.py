from fastapi import Depends
from sqlalchemy.orm import sessionmaker

from todo_list.db.model.todo import Todo
from todo_list.db.session_local import get_session


class TodoDB:

    def __init__(self, session: sessionmaker):
        self.session = session

    def getTodoList(self):

        with self.session.begin() as session:
            try:
                result = session.query(Todo).all()
                return result
            except Exception as e:
                session.rollback()
                raise e