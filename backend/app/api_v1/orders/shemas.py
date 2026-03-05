from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict


class OrderBase(BaseModel):
    customer_id: int
    description: str
    created_date: datetime
    status: Literal[
        "new",
        "confirmed",
        "in_progress",
        "completed",
        "cancelled",
    ]



class OrderCreate(BaseModel):
    customer_id: int
    description: str



class OrderUpdate(OrderBase):
    pass

class OrderUpdatePartial(BaseModel):
    customer_id: int | None = None
    description: str | None = None
    status: Literal[
        "new",
        "confirmed",
        "in_progress",
        "completed",
        "cancelled",
    ] | None = None

class Order(OrderBase):
    order_id: int

    model_config = ConfigDict(from_attributes=True)