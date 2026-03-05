from typing import Annotated

from fastapi import status, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.delivery.shemas import Delivery
from backend.app.database.models import db_helper

from . import crud


async def get_delivery_id(
        delivery_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Delivery:
    delivery = await crud.get_delivery(
        delivery_id=delivery_id,
        session=session
    )
    if delivery is not None:
        return delivery
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Delivery id: {delivery_id} not found"
    )