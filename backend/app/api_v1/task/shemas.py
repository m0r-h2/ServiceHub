from typing import Literal
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict
from fastapi import Form

class TaskResponse(BaseModel):
    id: int

    title: str = Field(max_length=100)

    phone: str = Field(pattern=r"^\+7\d{10}$")

    work: Literal[
        "Доставка",
        "Ремонт",
        "Сервисное Обслуживание"
    ]

    city: str

    address: str

    required: str

    text: str = Field(max_length=1000)

    company: str | None = None

    technical: str | None = None

    driver: str | None = None

    created_date: datetime

    end_date: datetime | None = None

    status: Literal[
        "Заявка создана",
        "Принято",
        "В пути",
        "Идет работа",
        "Отказ",
        "На проверке",
        "Сбор материалов",
        "Доставлено"
    ]
    price: Decimal | None

    model_config = ConfigDict(from_attributes=True)




class TaskCreate(BaseModel):
    title: str = Field(max_length=100)

    phone: str

    work: Literal[
        "Доставка",
        "Ремонт",
        "Сервисное Обслуживание"
    ]

    city: str

    address: str

    required: str | None

    text: str = Field(max_length=1000)

    price: None | Decimal

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        phone: str = Form(...),
        work: str = Form(...),
        city: str = Form(...),
        address: str = Form(...),
        required: str = Form(""),
        text: str = Form(""),
        price: int = Form(0)
    ):
        return cls(
            title=title, phone=phone, work=work, city=city,
            address=address, required=required, text=text, price=price
        )






