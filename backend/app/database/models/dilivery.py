from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base



class Delivery(Base):
    __tablename__ = "deliveries"

    delivery_id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        primary_key=True,
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.order_id")
    )

    driver_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id")
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