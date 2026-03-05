from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper
from .dependencies import get_service_request_id
from .shemas import ServiceRequest,ServiceRequestCreate, ServiceRequestUpdate, ServiceRequestUpdatePartial
from . import crud

router = APIRouter(
    tags=["Service Request🔧"]
)

@router.get("/", response_model=list[ServiceRequest], status_code=status.HTTP_200_OK)
async def get_service_requests(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> list[ServiceRequest]:
    return await crud.get_service_requests(session=session)

@router.get("/{service_request_id}/", response_model=ServiceRequest, status_code=status.HTTP_200_OK)
async def get_service_request(
        service_request: ServiceRequest = Depends(get_service_request_id)
) -> ServiceRequest:
    return service_request


@router.post("/", response_model=ServiceRequest, status_code=status.HTTP_201_CREATED)
async def create_service_request(
        new_service_request: ServiceRequestCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ServiceRequest:
    return await crud.create_service_request(
        new_service_request=new_service_request,
        session=session
    )


@router.put("/{service_request_id}/", response_model=ServiceRequest)
async def update_service_request(
        upd_service_request: ServiceRequestUpdate,
        service_request: ServiceRequest = Depends(get_service_request_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_service_request(
        upd_service_request=upd_service_request,
        service_request=service_request,
        session=session
    )


@router.patch("/{service_request_id}/", response_model=ServiceRequest)
async def update_service_request_patrial(
        upd_service_request: ServiceRequestUpdatePartial,
        service_request: ServiceRequest = Depends(get_service_request_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_service_request(
        upd_service_request=upd_service_request,
        service_request=service_request,
        session=session,
        partial=True
    )


@router.delete("/{service_request_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_service_request(
        service_request: ServiceRequest = Depends(get_service_request_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    await crud.delete_service_request(
        service_request=service_request,
        session=session
    )