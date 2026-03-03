from typing import Literal

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    full_name: str
    email: str
    password: str
    role: Literal[
        "administrator",
        "dispatcher",
        "driver",
        "technician"
    ]
    phone: str
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserUpdatePartial(UserBase):
    full_name: str | None
    email: str | None
    password: str | None
    role: Literal[
              "administrator",
              "dispatcher",
              "driver",
              "technician"
          ] | None
    phone: str | None


class User(UserBase):
    user_id: int
