from sqlalchemy import Column, BigInteger, TEXT, DATE

from todo_list.db.session_local import Base


class Authenticate(Base):
    __tablename__ = "authenticate"

    _id = Column(BigInteger, unique=True, primary_key=True)
    api_key = Column(TEXT)
