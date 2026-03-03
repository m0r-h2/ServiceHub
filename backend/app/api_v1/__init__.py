
from fastapi import APIRouter

from .users.views import router as user_router
from .customers.views import router as customer_router
router = APIRouter()

router.include_router(
    router=user_router,
    prefix="/user"
)

router.include_router(
    router=customer_router,
    prefix="/customer"
)