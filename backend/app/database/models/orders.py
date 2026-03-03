from sqlalchemy import String, Text, DateTime, ForeignKey, func, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        primary_key=True,
    )

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customers.customer_id")
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