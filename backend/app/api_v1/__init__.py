
from fastapi import APIRouter

from .users.views import router as user_roter

router = APIRouter()

router.include_router(
    router=user_roter,
    prefix="/user"
)