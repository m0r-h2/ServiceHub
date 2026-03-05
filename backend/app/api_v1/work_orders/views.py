from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import get_work_order_id
from .shemas import WorkOrder, WorkOrderCreate, WorkOrdersUpdate, WorkOrdersUpdatePartial
from . import crud
from backend.app.database.models import db_helper

router = APIRouter(
    tags=["Work Orders🛠"]
)

@router.get("/", response_model=list[WorkOrder], status_code=status.HTTP_200_OK)
async def get_work_orders(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_work_orders(session=session)


@router.get("/{work_order_id}/", response_model=WorkOrder, status_code=status.HTTP_200_OK)
async def get_work_order(
        work_order: WorkOrder = Depends(get_work_order_id)
):
    return work_order


@router.post("/", response_model=WorkOrder, status_code=status.HTTP_201_CREATED)
async def create_work_order(
        new_work_order: WorkOrderCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_work_order(
        new_work_order=new_work_order,
        session=session
    )

@router.put("/{work_order_id}/", response_model=WorkOrder)
async def update_work_order(
        upd_work_order: WorkOrdersUpdate,
        work_order: WorkOrder = Depends(get_work_order_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_work_order(
        upd_work_order=upd_work_order,
        work_order=work_order,
        session=session
    )


@router.patch("/{work_order_id}/", response_model=WorkOrder)
async def update_work_order_partial(
        upd_work_order: WorkOrdersUpdatePartial,
        work_order: WorkOrder = Depends(get_work_order_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_work_order(
        upd_work_order=upd_work_order,
        work_order=work_order,
        session=session,
        partial=True
    )


@router.delete("/{work_order_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_work_order(
        work_order: WorkOrder = Depends(get_work_order_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.delete_work_order(
        work_order=work_order,
        session=session
    )
