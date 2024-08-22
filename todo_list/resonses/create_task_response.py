from pydantic import BaseModel


class CreateTaskResponse(BaseModel):
    id: str