from aioredis import Redis
from datetime import timedelta
from project.config import get_settings

config = get_settings()


class Cache:
    client: Redis = None


cache = Cache()


async def connect(host: str = config.REDIS.HOST, port: int = config.REDIS.PORT):
    cache.client = await Redis(host=host, port=port, decode_responses=True)


async def insert(key: str, value: str, expire: timedelta):
    await cache.client.setex(key, expire, value)


async def get(key: str):
    return await cache.client.get(key)


async def close():
    await cache.client.close()
