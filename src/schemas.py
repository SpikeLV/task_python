from pydantic import BaseModel
from typing import Optional

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class STask(STaskAdd):
    id: int

class STaskId(BaseModel):
    ok: bool
    task_id: int