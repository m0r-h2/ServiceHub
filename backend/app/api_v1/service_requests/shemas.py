from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class ServiceRequestBase(BaseModel):

    customer_id: int

    description: str
    priority: Literal[
        "low",
        "medium",
        "high",
        "urgent",
    ]
    status: Literal[
        "new",
        "assigned",
        "in_progress",
        "completed",
        "cancelled",
    ]
    created_date: datetime


class ServiceRequestCreate(ServiceRequestBase):
    pass


class ServiceRequestUpdate(ServiceRequestBase):
    pass

class ServiceRequestUpdatePartial(ServiceRequestBase):
    customer_id: int | None = None

    description: str | None = None
    priority: Literal[
        "low",
        "medium",
        "high",
        "urgent",
    ] | None = None
    status: Literal[
        "new",
        "assigned",
        "in_progress",
        "completed",
        "cancelled",
    ] | None = None
    created_date: datetime | None = None



class ServiceRequest(BaseModel):
    service_request_id: int

    model_config = ConfigDict(from_attributes=True)