from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.database.models import db_helper
from fastapi import Request, Depends, APIRouter
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates
from backend.app.api_v1.task.shemas import TaskResponse, TaskCreate
from backend.app.api_v1.task import crud

router = APIRouter()
templates = Jinja2Templates(directory="frontend/template")


@router.get("/", response_class=HTMLResponse)
async def get_index(request: Request, session: AsyncSession = Depends(db_helper.scoped_session_dependency)):

    result = await crud.get_tasks(session=session)
    orders = [TaskResponse.model_validate(o).model_dump(mode="json") for o in result]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "orders": orders  # Передаем список в шаблон
        }
    )


@router.post("/create")
async def create_task(
        new_task: TaskCreate = Depends(TaskCreate.as_form),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    result = await crud.create_task(new_task=new_task, session=session)

    return RedirectResponse(url="/", status_code=303)