import datetime
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from project.database.sql.models import Base
from typing import Generic, Type, TypeVar

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, id: int, obj_in: UpdateSchemaType) -> ModelType:
        db_obj = self.get(db=db, id=id)

        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True, by_alias=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, id: int) -> ModelType:
        q = db.query(self.model).filter(self.model.id == id, self.model.DELETED_AT.is_(None)).first()
        if not q:
            raise HTTPException(
                status_code=404,
                detail=f"ID {id} not found"
            )
        return q

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return db.query(self.model).filter(self.model.DELETED_AT.is_(None)).offset(skip).limit(limit).all()

    def get_like(self, db: Session, *, column: str, search_key: str, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return db.query(self.model)\
            .filter(self.model.__getattribute__(column).like('%' + search_key + '%'))\
            .offset(skip)\
            .limit(limit)\
            .all()

    def soft_delete(self, db: Session, *, id: int) -> ModelType:
        db_obj = self.get(db=db, id=id)

        db_obj.DELETED_AT = datetime.datetime.utcnow()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> ModelType:
        # obj = db.query(self.model).get(id)
        obj = db.query(self.model).filter(self.model.id == id, self.model.DELETED_AT.is_not(None)).first()
        if not obj:
            raise HTTPException(
                status_code=404,
                detail=f"ID {id} not found"
            )
        db.delete(obj)
        db.commit()
        return obj
