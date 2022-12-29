from typing import List

from pydantic import EmailStr
from project.schemas.base import Base


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: int | None = None