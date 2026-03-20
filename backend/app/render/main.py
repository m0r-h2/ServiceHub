from fastapi import Request, Depends, APIRouter
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database.models import db_helper
from backend.app.api_v1.companies.shemas import CompanyResponse
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
        category: Optional[List[str]] = Query(None),
        region: Optional[str] = Query(None),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result_task = await crud_task.get_tasks(
        session=session,
        work=category,
        city=region
    )

    task = [TaskResponse.model_validate(t).model_dump(mode="json") for t in result_task]

    result_workers = await crud_companies.get_companies(session=session)
    company = [CompanyResponse.model_validate(c).model_dump(mode="json") for c in result_workers]

    return templates.TemplateResponse(
        "main.html",
        {
            "request": request,
            "orders": task,
            "performers": company,
            "selected_region": region,
            "selected_categories": category or []
        }
    )


@router.post("/create")
async def create_task(
        new_task: TaskCreate = Depends(TaskCreate.as_form),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    _ = await crud_task.create_task(new_task=new_task, session=session)
    return RedirectResponse(url="/", status_code=303)