from fastapi import status, Depends, HTTPException, Path
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper
from .shemas import ServiceRequest
from . import crud

async def get_service_request_id(
        service_request_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> ServiceRequest:
    service_request = await crud.get_service_request(
        service_request_id=service_request_id,
        session=session
    )
    if service_request is not None:
        return service_request
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Service request id: {service_request_id} not found"
    )