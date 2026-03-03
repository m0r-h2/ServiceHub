from pydantic import BaseModel, ConfigDict


class CustomerBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str

    model_config = ConfigDict(from_attributes=True)

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerUpdatePartial(CustomerBase):
    name: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None

class Customer(CustomerBase):
    customer_id: int