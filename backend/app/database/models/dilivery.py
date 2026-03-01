import uuid
from typing import Optional
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base



class Delivery(Base):
    __tablename__ = "deliveries"

    delivery_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    order_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("orders.id")
    )

    driver_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id")
    )

    scheduled_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="planned"
    )

    order: Mapped["Order"] = relationship(
        back_populates="deliveries"
    )

    driver: Mapped["User"] = relationship(
        back_populates="deliveries"
    )