from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base



class Worker(Base):
    __tablename__ = "workers"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    phone: Mapped[String] = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    company_name: Mapped[str] = mapped_column(
        String,
        ForeignKey("companies.name"),
        nullable=True
    )


    job_title: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    company: Mapped["Company"] = relationship(
        "Company",
        back_populates="workers"
    )

    driver_tasks: Mapped[list["Task"]] = relationship(
        "Task",
        foreign_keys="Task.driver",
        back_populates="driver_worker"
    )

    technical_tasks: Mapped[list["Task"]] = relationship(
        "Task",
        foreign_keys="Task.technical",
        back_populates="technical_worker"
    )