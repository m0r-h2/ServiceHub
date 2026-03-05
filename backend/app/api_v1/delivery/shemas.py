from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class DeliveryBase(BaseModel):

    order_id: int
    driver_id: int
    scheduled_date: datetime
    status: Literal[
        "planned",
        "assigned",
        "in_progress",
        "failed",
        "cancelled",
    ]

class DeliveryCreate(DeliveryBase):
    pass


class DeliveryUpdate(DeliveryBase):
    pass


class DeliveryUpdatePartial(DeliveryBase):
    order_id: int | None = None
    driver_id: int | None = None

    scheduled_date: datetime | None = None
    status: Literal[
        "planned",
        "assigned",
        "in_progress",
        "failed",
        "cancelled",
    ] | None = None


class Delivery(DeliveryBase):

    delivery_id: int

    model_config = ConfigDict(from_attributes=True)

