from fastapi import Request, APIRouter, status, Response, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.core import settings
from backend.app.database.models import db_helper
from backend.app.core.auth_utils import create_access_token, verify_password
from backend.app.api_v1.companies import crud

template = Jinja2Templates(directory="frontend/template")

router = APIRouter(
    prefix="/login"
)


@router.post("/auth")
async def login(
        response: Response,
        email: str = Form(...),
        password: str = Form(...),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    company = await crud.get_companies_email(email, session=session)

    if not verify_password(password=password,hashed_password=company.password):
       raise HTTPException(status_code=401, detail="Неверная почта или пароль")

    access_token = create_access_token(data={"sub": str(company.id)})

    response = RedirectResponse(url="/profile/", status_code=303)
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=settings.auth.access_token_expire_minutes * 60,
        samesite="lax"
    )
    return response


@router.get("", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_login_html(request: Request):
    return template.TemplateResponse(
        "login.html", {
            "request": request
        }
    )