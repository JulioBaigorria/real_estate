from fastapi import HTTPException
from pydantic import BaseModel
from typing import Generic, Type, TypeVar
from project.database.nosql.models import Base, OID


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

    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        db_obj = await self.model.insert_one(self.model(**obj_in.dict(by_alias=True)))
        return db_obj

    async def update(self, *, id: OID, obj_in: UpdateSchemaType) -> ModelType:
        db_obj = await self.get(id)

        update_data = obj_in.dict(exclude_unset=True, by_alias=True)

        await db_obj.set(update_data)
        return db_obj

    async def get(self, id: OID) -> ModelType:
        db_obj = await self.model.get(id)
        if not db_obj:
            raise HTTPException(
                status_code=404,
                detail="ID %s not found" % id
            )
        return db_obj

    async def get_multi(self, *, skip: int = 0, limit: int = 100) -> list[ModelType]:
        return await self.model.find_all().skip(skip).limit(limit).to_list()

    async def find(self, *, search_dict: dict, skip: int = 0, limit: int = 100) -> list[ModelType]:
        objs = await self.model.find(search_dict).skip(skip).limit(limit).to_list()
        return objs

    # def soft_delete(self, *, id: int) -> ModelType:
    #     db_obj = self.get( id=id)
    #
    #     db_obj.DELETED_AT = datetime.datetime.utcnow()
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    async def delete(self, *, id: OID) -> ModelType:
        obj = await self.get(id)
        await obj.delete()
        return obj
