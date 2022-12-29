from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase
from project.config import get_settings
from beanie import init_beanie
from project.database.nosql.models import Base

import logging


config = get_settings()


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()

logger = logging.getLogger(config.APP_NAME).getChild('MONGO')


async def get_database() -> AsyncIOMotorDatabase:
    return getattr(db.client, config.MONGO.NAME)


async def connect():
    logger.info("Connecting to MongoDB.")
    document_models = [cls for cls in Base.__subclasses__()]
    db.client = AsyncIOMotorClient(
        config.MONGO.CONN_URL,
        maxPoolSize=10,
        minPoolSize=5
    )
    await init_beanie(database=await get_database(), document_models=document_models)
    logger.info("Connected to MongoDB.")


async def close_connection():
    logger.info("Closing connection with MongoDB.")
    db.client.close()
    logger.info("Closed connection with MongoDB.")

