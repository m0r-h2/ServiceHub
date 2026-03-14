from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from backend.app.api_v1.workers.shemas import WorkerCreate
from backend.app.database.models import Worker


async def get_workers(session: AsyncSession) -> list[Worker]:
    stmt = select(Worker).order_by(Worker.id)
    result: Result = await session.execute(stmt)
    workers = result.scalars().all()
    return list(workers)


async def create_worker(new_worker: WorkerCreate, session: AsyncSession) -> Worker:
    worker = Worker(**new_worker.model_dump())
    session.add(worker)
    await session.commit()
    return worker
