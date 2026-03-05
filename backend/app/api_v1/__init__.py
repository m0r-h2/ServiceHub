
from fastapi import APIRouter

from .users.views import router as user_router
from .customers.views import router as customer_router
from .orders.views import router as order_router
from .delivery.views import router as delivery_router
from .service_requests.views import router as service_request_router

router = APIRouter()

router.include_router(
    router=user_router,
    prefix="/user"
)

router.include_router(
    router=customer_router,
    prefix="/customer"
)

router.include_router(
    router=order_router,
    prefix="/order"
)


router.include_router(
    router=delivery_router,
    prefix="/delivery"
)


router.include_router(
    router=service_request_router,
    prefix="/service_request"
)