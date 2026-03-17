from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from decimal import Decimal
from .base import Base

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    work: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    required: Mapped[str] = mapped_column(
        String,
        nullable=True
    )

    text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    price: Mapped[Decimal] = mapped_column(
        DECIMAL,
        nullable=True,
        default=None

    )

    company_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("companies.id"),
        nullable=True
    )

    technical: Mapped[str] = mapped_column(
        String,
        ForeignKey("workers.name"),
        nullable=True
    )

    driver: Mapped[str] = mapped_column(
        String,
        ForeignKey("workers.name"),
        nullable=True
    )

    created_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now()
    )

    end_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="Заявка создана"
    )

    progress: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    technical_worker: Mapped["Worker"] = relationship(
        "Worker",
        foreign_keys=[technical],
        back_populates="technical_tasks"
    )

    driver_worker: Mapped["Worker"] = relationship(
        "Worker",
        foreign_keys=[driver],
        back_populates="driver_tasks"
    )


    task_company_obj: Mapped["Company"] = relationship(
        "Company",
        foreign_keys=[company_id],
        back_populates="tasks"
    )




