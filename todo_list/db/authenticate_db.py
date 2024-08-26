from fastapi import Depends
from sqlalchemy.orm import sessionmaker

from todo_list.db.model.authenticate import Authenticate



class AuthenticateDB:

    def __init__(self, session: sessionmaker):
        self.session = session

    def getAPIKey(self, apiKey):

        with self.session.begin() as session:
            try:
                result = session.query(Authenticate).filter(Authenticate.api_key == apiKey).first()
                return result
            except Exception as e:
                session.rollback()
                raise e

