from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates
from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from backend.app.api_v1.workers.shemas import WorkerResponse
from backend.app.api_v1.task.shemas import TaskResponse
from backend.app.api_v1.task import crud as crud_task
from backend.app.api_v1.workers import crud as crud_workers
from backend.app.api_v1.companies.shemas import CompanyResponse
from backend.app.database.models import db_helper
from backend.app.api_v1.companies.dependencies import get_current_company

router = APIRouter(
    prefix="/company_profile",
)


template = Jinja2Templates(directory="frontend/template")


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_profile(
        request: Request,
        company: CompanyResponse = Depends(get_current_company),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    if not company:
        return RedirectResponse("/register")

    result_workers = await crud_workers.get_workers_from_the_company(
        company_name=company.name,
        session=session
    )
    workers = [WorkerResponse.model_validate(w).model_dump(mode="json") for w in result_workers]


    result_task = await crud_task.get_tusk_id_company(
        company_id=company.id,
        session=session
    )

    task = [TaskResponse.model_validate(t).model_dump(mode="json") for t in result_task]



    return template.TemplateResponse(
        "company_profile.html",{
            "request": request,
            "workers": workers,
            "company": company,
            "orders": task
        }
    )
