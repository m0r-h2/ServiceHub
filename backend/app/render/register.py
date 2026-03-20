from fastapi import APIRouter, status, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(
    prefix="/register"
)

template = Jinja2Templates(directory="frontend/template")


@router.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def get_register(
        request: Request,
):
    return template.TemplateResponse(
        "register.html",
        {
            "request": request
        }
    )