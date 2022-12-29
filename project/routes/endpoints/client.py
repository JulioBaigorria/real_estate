import orjson
from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from project import deps
from project.database.sql import crud

from project import schemas

router = APIRouter()


@router.get('/', response_model=List[schemas.Client])
async def read_clients(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """Retrieve clients"""
    clients = crud.client.get_multi(db=db, skip=skip, limit=limit)
    return clients


@router.get('/{dni_client}/', response_model=schemas.Client)
async def read_client_by_dni(
        *,
        db: Session = Depends(deps.get_db),
        dni_client: int,
) -> Any:
    """Retrieve client by ID"""
    client = crud.client.get_by_dni(db=db, dni=dni_client)
    return client


@router.post("/", response_model=schemas.Client)
async def create_client(
        *,
        db: Session = Depends(deps.get_db),
        item_in: schemas.ClientCreate,
) -> Any:
    """
    Create new client.
    """

    client = crud.client.create(db=db, obj_in=item_in)
    return client
