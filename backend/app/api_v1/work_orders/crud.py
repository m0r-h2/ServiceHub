from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from backend.app.database.models import WorkOrder
from .shemas import WorkOrdersUpdate, WorkOrdersUpdatePartial, WorkOrderCreate

async def get_work_orders(session: AsyncSession) -> list[WorkOrder]:
    stmt = select(WorkOrder).order_by(WorkOrder.work_order_id)
    result: Result = await session.execute(stmt)
    work_order = result.scalars().all()
    return list(work_order)


async def get_work_order(work_order_id: int, session: AsyncSession) -> WorkOrder | None:
    return await session.get(WorkOrder, work_order_id)


async def create_work_order(new_work_order: WorkOrderCreate, session: AsyncSession) -> WorkOrder:
    work_order = WorkOrder(**new_work_order.model_dump())
    session.add(work_order)
    await session.commit()
    return work_order


async def update_work_order(
        work_order: WorkOrder,
        upd_work_order: WorkOrdersUpdate | WorkOrdersUpdatePartial,
        session: AsyncSession,
        partial: bool = False,
) -> WorkOrder:
    for nums, value in upd_work_order.model_dump(exclude_unset=partial).items():
        setattr(work_order, nums, value)
    await session.commit()
    return work_order


async def delete_work_order(work_order: WorkOrder, session: AsyncSession) -> None:
    await session.delete(work_order)
    await session.commit()
