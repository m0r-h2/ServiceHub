from decimal import Decimal
from datetime import datetime

from sqlalchemy import Integer, String, DECIMAL, Text, DateTime, func

from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
        primary_key=True
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        Integer,
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )

    rating: Mapped[Decimal]  = mapped_column(
        DECIMAL,
        default=None,
        nullable=True
    )

    city: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    create_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=func.now()
    )

    comment: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    workers: Mapped[list["Worker"]] = relationship(
        "Worker",
        back_populates="company"
    )


    tasks: Mapped[list["Task"]] = relationship(
        "Task",
        back_populates="task_company_obj"
    )

