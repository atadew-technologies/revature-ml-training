from enum import Enum
from pathlib import Path

from fastapi import FastAPI



from dotenv import load_dotenv
env_path = Path("./") / ".env"
load_dotenv(env_path)

from todo_list.routers import default_router


app = FastAPI(title="FastAPI Training")




app.include_router(default_router.api_router)




