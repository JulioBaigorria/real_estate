import orjson
from pydantic import BaseModel, validator
import json
from typing import Dict
from project.schemas.types import DNI
from pydantic import EmailStr
from project.schemas.base import Base


class Address(Base):
    post_code: str
    locale: str | None
    street_name: str | None
    street_number: str | None
    neighborhood: str | None
    province: str | None
    lat: float | None
    long: float | None
    comment: str | None


class Client(Base):
    id: int
    dni: DNI
    type: str
    name: str
    last_name: str
    email: EmailStr
    tel: str
    address: Address | None
    comment: str

    @validator('address', pre=True)
    def format_address(cls, v):
        return orjson.loads(v)

    class Config:
        orm_mode = True


class ClientCreate(Base):
    dni: DNI
    type: str
    name: str
    last_name: str
    email: EmailStr
    tel: str
    address: Address | None
    comment: str


class ClientUpdate(Base):
    dni: DNI | None
    type: str | None
    name: str | None
    last_name: str | None
    email: EmailStr | None
    tel: str | None
    address: Address | None
    comment: str | None
