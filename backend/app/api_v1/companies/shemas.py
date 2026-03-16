from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal

class CompanyCreate(BaseModel):
    name: str
    email: str
    password: str
    phone: str
    city: str
    comment: str





class CompanyResponse(BaseModel):
    name: str
    email: str
    phone: str
    city: str
    rating: Decimal | None
    create_date: datetime
    comment: str

    model_config = ConfigDict(from_attributes=True)

