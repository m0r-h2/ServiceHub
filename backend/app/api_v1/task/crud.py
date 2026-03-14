from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import Task
from sqlalchemy import select, Result

from .shemas import TaskCreate


async def get_tasks(session: AsyncSession) -> list[Task]:
    stmt = select(Task).order_by(Task.created_date.desc())
    result: Result = await session.execute(stmt)
    tasks = result.scalars().all()
    return list(tasks)



async def create_task(
        new_task: TaskCreate,
        session: AsyncSession
) -> Task:
    task = Task(**new_task.model_dump())
    session.add(task)
    await session.commit()
    return task