from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import db_helper, Task
from .dependencies import get_task_id
from .shemas import TaskCreate, TaskResponse, TaskUpdateWorking, TaskUpdateCompanyPartial
from . import crud
from backend.app.database.models import Company
from backend.app.api_v1.companies.dependencies import get_current_company

router = APIRouter(
    tags=["Tasks"]
)

@router.post("/create" ,status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
async def create_task(
        new_task: TaskCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_task(new_task=new_task,session=session)



@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TaskResponse])
async def get_tasks(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_tasks(session=session)


@router.patch("/{task_id}")
async def task_update_company(
        task_update: TaskUpdateCompanyPartial,
        task: Task = Depends(get_task_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.update_task(
        task_update=task_update,
        task=task,session=session
    )


@router.patch("/{task_id}/take", status_code=status.HTTP_200_OK, response_model=TaskResponse)
async def take_task_into_work(
        task_id: int,
        current_company: Company = Depends(get_current_company),  # Твоя зависимость авторизации
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):

    task = await crud.get_task(session=session, task_id=task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    if task.company_id is not None:
        raise HTTPException(status_code=400, detail="Этот заказ уже взят другим исполнителем")

    update_data = TaskUpdateWorking(
        company_id=current_company.id,
        status="Принято",
        progress=0
    )

    return await crud.update_task(
        task=task,
        task_update=update_data,
        session=session
    )
