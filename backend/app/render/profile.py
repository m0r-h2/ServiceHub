from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates
from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse

from backend.app.api_v1.task.shemas import TaskResponse
from backend.app.api_v1.task import crud as crud_task
from backend.app.api_v1.companies.shemas import CompanyResponse
from backend.app.database.models import db_helper
from backend.app.render.register import get_current_company

router = APIRouter(
    prefix="/profile",
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
    result_task = await crud_task.get_tusk_id_company(company_id=company.id, session=session)

    task = [TaskResponse.model_validate(t).model_dump(mode="json") for t in result_task]



    return template.TemplateResponse(
        "profile.html",{
            "request": request,
            "company": company,
            "orders": task
        }
    )
