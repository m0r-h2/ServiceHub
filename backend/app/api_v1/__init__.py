from fastapi import APIRouter

from .workers.views import router as worker_router
from .companies.views import router as companies_router
from .task.views import router as task_router

router_v1 = APIRouter()

router_v1.include_router(
    router=worker_router,
    prefix="/workers"
)

router_v1.include_router(
    router=companies_router,
    prefix="/companies"
)

router_v1.include_router(
    router=task_router,
    prefix="/tasks"
)