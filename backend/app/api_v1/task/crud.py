from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import Task
from sqlalchemy import select, Result

from .shemas import TaskCreate



async def get_tasks(session: AsyncSession, work: list = None, city: str = None) -> list[Task]:
    stmt = select(Task)

    if work:
        # Если в базе поле называется category
        stmt = stmt.where(Task.work.in_(work))

    if city and city != "Все регионы":
        stmt = stmt.where(Task.city == city)

    stmt = stmt.order_by(Task.id.desc())  # Новые сверху

    result = await session.execute(stmt)
    return list(result.scalars().all())


async def create_task(
        new_task: TaskCreate,
        session: AsyncSession
) -> Task:
    task = Task(**new_task.model_dump())
    session.add(task)
    await session.commit()
    return task