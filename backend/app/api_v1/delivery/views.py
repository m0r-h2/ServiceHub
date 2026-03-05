from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from app.api_v1.delivery.shemas import Delivery, DeliveryCreate, DeliveryUpdate, DeliveryUpdatePartial
from . import crud
from .dependencies import get_delivery_id
from ...database.models import db_helper

router = APIRouter(
    tags=["Delivery🚚"]
)

@router.get("/", response_model=list[Delivery], status_code=status.HTTP_200_OK)
async def get_all_delivery(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_all_delivery(
        session=session
    )

@router.get("/{delivery_id}/",response_model=Delivery ,status_code=status.HTTP_200_OK)
async def get_delivery(delivery: Delivery = Depends(get_delivery_id)):
    return delivery


@router.post("/", response_model=Delivery, status_code=status.HTTP_201_CREATED)
async def create_delivery(
        new_delivery: DeliveryCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_delivery(
        new_delivery=new_delivery,
        session=session
    )


@router.put("/{delivery_id}", response_model=Delivery)
async def update_delivery(
        upd_delivery: DeliveryUpdate,
        delivery: Delivery = Depends(get_delivery_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_delivery(
        upd_delivery=upd_delivery,
        delivery=delivery,
        session=session
    )


@router.patch("/{delivery_id}/", response_model=Delivery)
async def update_delivery_partial(
        upd_delivery: DeliveryUpdate | DeliveryUpdatePartial,
        delivery: Delivery = Depends(get_delivery_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_delivery(
        upd_delivery=upd_delivery,
        delivery=delivery,
        session=session,
        patrial=True
    )


@router.delete("/{delivery_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_delivery(
        delivery: Delivery = Depends(get_delivery_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.delete_delivery(
        delivery=delivery,
        session=session
    )