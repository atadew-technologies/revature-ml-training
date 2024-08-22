from fastapi import Depends
from sqlalchemy.orm import sessionmaker


from todo_list.db.session_local import get_session



class TodoSVC:

    def __init__(self, session: sessionmaker = Depends(get_session)):
        self.session = session

    def getTodoList(self):
        # todo = TodoDB(self.session)
        # todo.getTodoList()
        return {}


