from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from backend.app.database.models import Order as OrderModel
from .shemas import Order, OrderCreate, OrderUpdate, OrderUpdatePartial


async def get_orders(session: AsyncSession) -> list[Order]:
    stmt = select(OrderModel).order_by(OrderModel.order_id)
    result: Result = await session.execute(stmt)
    order = result.scalars().all()
    return list(order)


async def get_order(order_id: int, session: AsyncSession) -> Order | None:
    return await session.get(OrderModel, order_id)


async def create_order(new_order: OrderCreate, session: AsyncSession) -> Order:
    order = OrderModel(**new_order.model_dump())
    session.add(order)
    await session.commit()
    return order


async def update_order(
        order: Order,
        upd_order: OrderUpdate | OrderUpdatePartial,
        session: AsyncSession,
        partial: bool = False,
) -> OrderModel:
    for nums, value in upd_order.model_dump(exclude_unset=partial).items():
        setattr(order, nums, value)
    await session.commit()
    return order


async def delete_order(order: Order , session: AsyncSession) -> None:
    await session.delete(order)
    await session.commit()

