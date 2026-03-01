import uuid
from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class WorkOrder(Base):
    __tablename__ = "work_orders"

    work_order_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    request_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("service_requests.id")
    )

    technician_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        ForeignKey("users.id")
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