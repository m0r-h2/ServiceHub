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

class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserUpdatePartial(UserBase):
    full_name: str | None = None
    email: str | None = None
    password: str | None = None
    role: Literal[
              "administrator",
              "dispatcher",
              "driver",
              "technician"
          ] | None = None
    phone: str | None = None


class User(UserBase):

    user_id: int

    model_config = ConfigDict(from_attributes=True)