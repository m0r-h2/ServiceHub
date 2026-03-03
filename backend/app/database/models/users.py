
from .base import Base

from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        Integer,
        index=True,
        primary_key=True,
    )
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50))
    role: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(50))

    deliveries: Mapped[list["Delivery"]] = relationship(
        back_populates="driver"
    )

    work_orders: Mapped[list["WorkOrder"]] = relationship(
        back_populates="technician"
    )
