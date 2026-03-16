from fastapi import Request, APIRouter, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


template = Jinja2Templates(directory="frontend/template")

router = APIRouter(
    prefix="/login"
)


@router.get("", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_login_html(request: Request):
    return template.TemplateResponse(
        "login.html", {
            "request": request
        }
    )