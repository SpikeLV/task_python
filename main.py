from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

from src.database import delete_db, create_db
from src.router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_db()
    print("DB deleted")
    await create_db()
    print("DB created")
    yield
    print("reload APP")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)