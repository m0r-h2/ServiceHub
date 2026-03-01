import uuid
from sqlalchemy import String, Text, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    customer_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("customers.id")
    )

    description: Mapped[str] = mapped_column(Text)
    created_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    status: Mapped[str] = mapped_column(String(50), default="new")

    customer: Mapped["Customer"] = relationship(
        back_populates="orders"
    )

    deliveries: Mapped[list["Delivery"]] = relationship(
        back_populates="order"
    )