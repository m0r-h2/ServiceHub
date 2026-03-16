from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class WorkerResponse(BaseModel):
    phone: str
    name: str
    company_name: str | None
    job_title: str
    status: str

    model_config = ConfigDict(from_attributes=True)


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
