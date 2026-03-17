from fastapi import APIRouter, status, Depends, Request, Cookie, HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.templating import Jinja2Templates
import jwt

from backend.app.api_v1.companies import crud
from backend.app.core import settings
from backend.app.database.models import db_helper,Company

router = APIRouter(
    prefix="/register"
)

template = Jinja2Templates(directory="frontend/template")


async def get_current_company(
        access_token: str = Cookie(None),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Company:
    if not access_token:
        return None
    try:
        payload = jwt.decode(access_token, settings.auth.secret_key, algorithms=[settings.auth.algorithm])
        company_id: str = payload.get("sub")
        if company_id is None:
            raise HTTPException(status_code=401)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401)

    # Ищем в базе (используй свой crud метод)
    company = await crud.get_company_id(company_id=int(company_id),session=session)
    return company



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