from pydantic import BaseModel, Field
from beanie import Document
from project.database.nosql.types import OID
from datetime import datetime


class Base(Document):
    id: OID | None = Field(alias="_id")


class Collection(Base):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "collection_name"
