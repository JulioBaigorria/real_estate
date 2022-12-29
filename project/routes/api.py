from fastapi import APIRouter

from .endpoints import client

api_router = APIRouter()
api_router.include_router(client.router, prefix='/clients', tags=['clients'])