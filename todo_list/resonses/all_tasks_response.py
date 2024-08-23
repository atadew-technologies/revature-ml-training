from pydantic import BaseModel

class Tasks(BaseModel):
    id: str
    name: str


class AllTasksResponse(BaseModel):
    tasks: Tasks = [Tasks]