from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import db_helper, Task
from .dependencies import get_task_id
from .shemas import TaskCreate, TaskResponse, TaskUpdateCompanyPartial, TaskUpdateGlobalPartial
from . import crud

router = APIRouter(
    tags=["Tasks"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TaskResponse])
async def get_tasks(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_tasks(session=session)


@router.post("/create" ,status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
async def create_task(
        new_task: TaskCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_task(new_task=new_task,session=session)


@router.patch("/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskResponse)
async def update_task(
        task_update: TaskUpdateCompanyPartial,
        task: Task = Depends(get_task_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_task(
        task=task,
        task_update=task_update,
        session=session,
    )


@router.patch("/global/{task_id}", status_code=status.HTTP_200_OK, response_model=TaskResponse)
async def update_task_global(
        task_update: TaskUpdateGlobalPartial,
        task: Task = Depends(get_task_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_task(
        task=task,
        task_update=task_update,
        session=session,
    )
