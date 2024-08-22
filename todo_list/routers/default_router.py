from fastapi import APIRouter

from todo_list.routers import tasks_router

api_router = APIRouter()

api_router.include_router(tasks_router.api_router, tags=["Task Management"])
