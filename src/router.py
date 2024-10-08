from fastapi import APIRouter, Depends
from typing import Annotated

from src.repository import TaskRepository
from src.schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_all()
    return {tasks }

@router.post("/")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}