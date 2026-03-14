from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from backend.app.database.models import db_helper
from .shemas import WorkerCreate, WorkerResponse

router = APIRouter(
    tags=["Workers"]
)


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[WorkerResponse])
async def get_workers(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_workers(session=session)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=WorkerResponse)
async def create_worker(
        new_worker: WorkerCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_worker(new_worker=new_worker,session=session)