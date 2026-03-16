from fastapi import APIRouter, status, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates

from backend.app.database.models import db_helper

router = APIRouter(
    prefix="/register"
)

template = Jinja2Templates(directory="frontend/template")

@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_register(
        request: Request,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return template.TemplateResponse(
        "register.html",
        {
            "request": request
        }
    )