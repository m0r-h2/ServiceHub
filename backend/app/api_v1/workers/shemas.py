from typing import Literal

from pydantic import BaseModel, Field


class WorkerResponse(BaseModel):
    phone: str
    name: str
    company_name: str | None
    job_title: str
    status: str


class WorkerCreate(BaseModel):
    phone: str = Field(pattern=r"^\+7\d{10}$")
    name: str
    company_name: str | None
    job_title: Literal[
        "Администратор",
        "Водитель",
        "Техник",
        "Босс"
    ]
    status: Literal[
        "Свободен",
        "На выезде",
        "Освобожден от работы"
    ]
