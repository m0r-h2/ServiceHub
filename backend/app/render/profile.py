from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates
from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse

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
        company: CompanyResponse = Depends(get_current_company)
):
    return template.TemplateResponse(
        "profile.html",{
            "request": request,
            "company": company
        }
    )
