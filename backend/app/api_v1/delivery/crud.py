from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from backend.app.api_v1.delivery.shemas import DeliveryCreate, DeliveryUpdate, DeliveryUpdatePartial
from backend.app.database.models import Delivery


async def get_all_delivery(session: AsyncSession) -> list[Delivery]:
    stmt = select(Delivery).order_by(Delivery.delivery_id)
    result: Result = await session.execute(stmt)
    delivery = result.scalars().all()
    return list(delivery)



async def get_delivery(delivery_id: int, session: AsyncSession) -> Delivery | None:
    return await session.get(Delivery, delivery_id)



async def create_delivery(new_delivery: DeliveryCreate, session: AsyncSession) -> Delivery:
    delivery = Delivery(**new_delivery.model_dump())
    session.add(delivery)
    await session.commit()
    return delivery



async def update_delivery(
        upd_delivery: DeliveryUpdate | DeliveryUpdatePartial,
        delivery: Delivery,
        session: AsyncSession,
        patrial: bool = False
) -> Delivery:
    for nums, volume in upd_delivery.model_dump(exclude_unset=patrial).items():
        setattr(delivery, nums, volume)
    await session.commit()
    return delivery


async def delete_delivery(delivery: Delivery, session: AsyncSession) -> None:
    await session.delete(delivery)
    await session.commit()


