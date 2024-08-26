from enum import Enum
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.security.api_key import APIKeyHeader


from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from todo_list.CustomMiddleware import CustomMiddleware

env_path = Path("./") / ".env"
load_dotenv(env_path)

from todo_list.routers import default_router


app = FastAPI(title="FastAPI Training")

apiKeyHeader = APIKeyHeader(name="x-api-key")


#app.add_middleware(CustomMiddleware)

app.include_router(default_router.api_router)




