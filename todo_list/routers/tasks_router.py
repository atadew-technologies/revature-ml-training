from fastapi import APIRouter, Depends

from todo_list.requests.todo import Todo
from todo_list.resonses.all_tasks_response import AllTasksResponse
from todo_list.resonses.create_task_response import CreateTaskResponse
from todo_list.resonses.all_tasks_response import Tasks
from todo_list.services.todo_svc import TodoSVC

api_router = APIRouter()

@api_router.get("/")
async def routerRoot():
    return {"message": "Welcome To ToDo Project"}


@api_router.post("/task", response_model=CreateTaskResponse)
async def createNewTask(todo: Todo):
    return CreateTaskResponse


@api_router.get("/task/all", response_model=AllTasksResponse)
async def readAllTasks(svc: TodoSVC = Depends(TodoSVC)):
    return svc.getTodoList()

@api_router.get("/task/{taskId}", response_model=Tasks)
async def readAllTasks(taskId: int):
    return {}

@api_router.delete("/task/{taskId}")
async def readAllTasks(taskId: int):
    return {}


@api_router.put("/task/{taskId}")
async def updateTask(taskId: int, todo: Todo):
    return {}