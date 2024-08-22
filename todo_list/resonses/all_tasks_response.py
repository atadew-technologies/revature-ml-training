from pydantic import BaseModel

class Tasks(BaseModel):
    id: str
    name: str


class AllTasksResponse(BaseModel):
    tasks: list = [Tasks]