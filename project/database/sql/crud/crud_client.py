from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

# from app.core.security import get_password_hash, verify_password
from project.database.sql.crud.base import CRUDBase
from project.database.sql.models import Client
from project.schemas.client import ClientCreate, ClientUpdate


class CRUDClient(CRUDBase[Client, ClientCreate, ClientUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[Client]:
        _Owner = db.query(Client).filter(Client.email == email).first()
        return db.query(Client).filter(Client.email == email).first()

    def get_by_dni(self, db: Session, *, dni: int) -> Optional[Client]:
        _Client = db.query(Client).filter(Client.dni == dni).first()
        return db.query(Client).filter(Client.dni == dni).first()

    def create(self, db: Session, *, obj_in: ClientCreate) -> Client:
        db_obj = Client(
            dni=obj_in.dni,
            type=obj_in.type,
            name=obj_in.name,
            last_name=obj_in.last_name,
            email=obj_in.email,
            tel=obj_in.tel,
            address=obj_in.address.json(),
            comment=obj_in.comment
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(
    #         self, db: Session, *, db_obj: Owner, obj_in: Union[OwnerUpdate, Dict[str, Any]]
    # ) -> Owner:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.dict(exclude_unset=True)
    #     if update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)


client = CRUDClient(Client)
