from fastapi import APIRouter
from .profile import router as router_profile
from .main import router as router_main
from .register import router as router_register
from .login import router as router_login

router_render = APIRouter()

router_render.include_router(router=router_login)
router_render.include_router(router=router_profile)
router_render.include_router(router=router_main)
router_render.include_router(router=router_register)