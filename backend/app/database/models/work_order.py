from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class WorkOrder(Base):
    __tablename__ = "work_orders"

    work_order_id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        primary_key=True,
    )

    request_id: Mapped[int] = mapped_column(
        ForeignKey("service_requests.service_request_id")
    )

    technician_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.user_id")
    )

    scheduled_date: Mapped[Optional[DateTime]] = mapped_column(
        DateTime(timezone=True)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="assigned"
    )

    request: Mapped["ServiceRequest"] = relationship(
        back_populates="work_orders"
    )

    technician: Mapped["User"] = relationship(
        back_populates="work_orders"
    )