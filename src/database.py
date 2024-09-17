from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engyne = create_async_engine("sqlite+aiosqlite:///./tasks.db")
new_session = async_sessionmaker(engyne, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class TaskOrm(Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str | None]]
    price: Mapped[Optional[float]]
    tax: Mapped[Optional[float]]

async def create_db():
    async with engyne.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def delete_db():
    async with engyne.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
