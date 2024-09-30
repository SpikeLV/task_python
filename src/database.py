from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

//DB_URL = 'mysql://username:password@localhost:3306/mydatabase'
engyne = create_async_engine("sqlite+aiosqlite:///./tasks.db")
new_session = async_sessionmaker(engyne, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UserOrs(Model);
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str] = mapped_column(String(255), deferred=True)
    name: Mapped[str]
    user_type:Mapped[int]
    company_id: Mapped[int]
    ship_id:Mapped[int]
    created_at: Column(DateTime(timezone=True), server_default=func.now())
    deleted_at: 
    
    async def create_db():
        async with engyne.begin() as conn:
            await conn.run_sync(Model.metadata.create_all)
    
    async def delete_db():
        async with engyne.begin() as conn:
            await conn.run_sync(Model.metadata.drop_all)
    
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
