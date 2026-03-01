import uuid

from .base import Base

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(Text)

    orders: Mapped["Order"] = relationship(
        back_populates="customer"
    )

    service_requests: Mapped[list["ServiceRequest"]] = relationship(
        back_populates="customer"
    )