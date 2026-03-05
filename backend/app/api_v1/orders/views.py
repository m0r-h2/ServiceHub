from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import db_helper

from .dependencies import get_order_id
from .shemas import Order, OrderCreate, OrderUpdate, OrderUpdatePartial, OrderBase
from . import crud


router = APIRouter(
    tags=["Orders"]
)


@router.get("/", response_model=list[Order],status_code=status.HTTP_200_OK)
async def get_orders(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_orders(session=session)


@router.get("/{order_id}/", status_code=status.HTTP_200_OK)
async def get_order(order: Order = Depends(get_order_id)):
    return order


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_order(new_order: OrderCreate,
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_order(
        new_order=new_order,
        session=session
    )



@router.put("/{order_id}/")
async def update_order(
        upd_order: OrderUpdate,
        order: Order = Depends(get_order_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_order(
        upd_order=upd_order,
        order=order,
        session=session
    )


@router.patch("/{order_id}/")
async def update_order_partial(
        upd_order: OrderUpdatePartial,
        order: Order = Depends(get_order_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_order(
        upd_order=upd_order,
        order=order,
        session=session,
        partial=True
    )

@router.delete("/{order_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(
        order: Order = Depends(get_order_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.delete_order(
        order=order,
        session=session
    )


