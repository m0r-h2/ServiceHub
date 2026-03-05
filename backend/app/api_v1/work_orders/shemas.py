from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class WorkOrderBase(BaseModel):

    request_id: int

    technician_id: int

    scheduled_date: datetime

    status: Literal[
        "assigned",
        "in_progress",
        "on_hold",
        "done",
        "cancelled",
    ]

class WorkOrderCreate(WorkOrderBase):
    pass


class WorkOrdersUpdate(WorkOrderBase):
    pass


class WorkOrdersUpdatePartial(WorkOrderBase):
    request_id: int | None = None

    technician_id: int | None = None

    scheduled_date: datetime | None = None

    status: Literal[
        "assigned",
        "in_progress",
        "on_hold",
        "done",
        "cancelled",
    ] | None = None


class WorkOrder(WorkOrderBase):
    work_order_id: int

    model_config = ConfigDict(from_attributes=True)

