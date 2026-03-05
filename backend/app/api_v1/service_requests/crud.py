from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from backend.app.database.models import ServiceRequest
from .shemas import ServiceRequestCreate, ServiceRequestUpdate, ServiceRequestUpdatePartial

async def get_service_requests(session: AsyncSession) -> list[ServiceRequest]:
    stmt = select(ServiceRequest).order_by(ServiceRequest.service_request_id)
    result: Result = await session.execute(stmt)
    service_request = result.scalars().all()
    return list(service_request)


async def get_service_request(service_request_id: int, session: AsyncSession) -> ServiceRequest | None:
    return await session.get(ServiceRequest, service_request_id)


async def create_service_request(
        new_service_request: ServiceRequestCreate,
        session: AsyncSession,
) -> ServiceRequest:
    service_request = ServiceRequest(**new_service_request.model_dump())
    session.add(service_request)
    await session.commit()
    return service_request


async def update_service_request(
        upd_service_request: ServiceRequestUpdate | ServiceRequestUpdatePartial,
        service_request: ServiceRequest,
        session: AsyncSession,
        partial: bool = float
) -> ServiceRequest:
    for nums, value in upd_service_request.model_dump(exclude_unset=partial).items():
        setattr(service_request, nums, value)
    await session.commit()
    return service_request



async def delete_service_request(
        service_request: ServiceRequest,
        session: AsyncSession,
):
    await session.delete(service_request)
    await session.commit()