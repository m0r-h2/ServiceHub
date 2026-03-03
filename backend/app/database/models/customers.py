from .base import Base

from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        primary_key=True,
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