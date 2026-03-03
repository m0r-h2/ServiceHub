from typing import Annotated
from fastapi import Path, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper, Customer

from . import crud

async def get_customer_id(
        customer_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Customer:
    customer = await crud.get_customer(
        customer_id=customer_id,
        session=session
    )
    if customer is not None:
        return customer
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Customer id: {customer_id} not found"
    )