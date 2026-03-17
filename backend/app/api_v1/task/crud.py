from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import Task
from sqlalchemy import select, Result

from .shemas import TaskCreate, TaskUpdateCompanyPartial


async def get_tasks(session: AsyncSession, work: list = None, city: str = None) -> list[Task]:
    stmt = select(Task)

    if work:
        stmt = stmt.where(Task.work.in_(work))

    if city and city != "Все регионы":
        stmt = stmt.where(Task.city == city)

    stmt = stmt.order_by(Task.id.desc())

    result = await session.execute(stmt)
    return list(result.scalars().all())


async def get_task(task_id: int,session: AsyncSession):
    return await session.get(Task, task_id)


async def get_tusk_id_company(company_id: int, session: AsyncSession) -> list[Task] :
    stmt = select(Task).where(Task.company_id == company_id).order_by(Task.created_date.desc())
    result: Result = await session.execute(stmt)
    task = result.scalars().all()
    return list(task)


async def create_task(
        new_task: TaskCreate,
        session: AsyncSession
) -> Task:
    task = Task(**new_task.model_dump())
    session.add(task)
    await session.commit()
    return task


async def update_task(task: Task, task_update: TaskUpdateCompanyPartial,session: AsyncSession):
    for name,value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, name, value)
    await session.commit()
    return task