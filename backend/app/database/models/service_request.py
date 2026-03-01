import uuid
from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ServiceRequest(Base):
    __tablename__ = "service_requests"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id")
    )

    description: Mapped[str] = mapped_column(Text)
    priority: Mapped[str] = mapped_column(String(20), default="medium")
    status: Mapped[str] = mapped_column(String(50), default="new")
    created_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    customer: Mapped["Customer"] = relationship(
        back_populates="service_requests"
    )

    work_orders: Mapped[list["WorkOrder"]] = relationship(
        back_populates="request"
    )