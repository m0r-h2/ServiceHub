from fastapi import status, HTTPException, Depends, Path
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper
from .shemas import WorkOrder
from . import crud

async def get_work_order_id(
        work_order_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> WorkOrder:
    work_order = await crud.get_work_order(
        session=session,
        work_order_id=work_order_id
    )
    if work_order is not None:
        return work_order
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Work Order id: {work_order_id} not found"
    )
