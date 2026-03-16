from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api_v1.companies.shemas import CompanyResponse

from backend.app.database.models import db_helper
from fastapi import Request, Depends, APIRouter
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from backend.app.api_v1.task.shemas import TaskResponse, TaskCreate
from backend.app.api_v1.task import crud as crud_task
from backend.app.api_v1.companies import crud as crud_companies

router = APIRouter()
templates = Jinja2Templates(directory="frontend/template")

from fastapi import Query
from typing import List, Optional


@router.get("/", response_class=HTMLResponse)
async def get_main(
        request: Request,
        # Добавляем параметры фильтрации из URL
        category: Optional[List[str]] = Query(None),
        region: Optional[str] = Query(None),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    # Передаем фильтры в CRUD метод для задач (ленты)
    result_task = await crud_task.get_tasks(
        session=session,
        work=category,
        city=region
    )

    # Оставляем вашу логику валидации (убедитесь, что from_attributes=True в схемах)
    task = [TaskResponse.model_validate(t).model_dump(mode="json") for t in result_task]

    # Компании (исполнители) обычно не фильтруются фильтрами ленты, оставляем как есть
    result_workers = await crud_companies.get_companies(session=session)
    company = [CompanyResponse.model_validate(c).model_dump(mode="json") for c in result_workers]

    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "orders": task,
            "performers": company,
            "selected_region": region,  # чтобы сохранить выбор в селекте после перезагрузки
            "selected_categories": category or []  # чтобы подсветить активные кнопки
        }
    )


@router.post("/create")
async def create_task(
        new_task: TaskCreate = Depends(TaskCreate.as_form),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud_task.create_task(new_task=new_task, session=session)
    return RedirectResponse(url="/", status_code=303)