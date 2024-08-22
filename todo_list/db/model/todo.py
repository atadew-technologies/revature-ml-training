from sqlalchemy import Column, BigInteger, TEXT, DATE

from todo_list.db.session_local import Base


class Todo(Base):
    __tablename__ = "todo"

    _id = Column(BigInteger, unique=True, primary_key=True)
    uuid = Column(TEXT)
    name = Column(TEXT)
    createdDate = Column(DATE)
    updatedDate = Column(DATE)