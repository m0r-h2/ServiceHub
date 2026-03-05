from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import db_helper
from .shemas import Order
from . import crud


async def get_order_id(
        order_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Order:
    order = await crud.get_order(
        order_id=order_id,
        session=session
    )
    if order is not None:
        return order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order id: {order_id} not found"
    )



