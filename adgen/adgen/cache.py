import redis.asyncio as redis
import hashlib
import os


redis_client = redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

def hash_prompt(title: str, description: str, tone: str) -> str:
    h = hashlib.sha256(f"{title}|{description}|{tone}".encode()).hexdigest()
    return f"adpost:{h}"

async def get_cached_post(title: str, description: str, tone: str) -> str | None:
    key = hash_prompt(title, description, tone)
    return await redis_client.get(key)

async def cache_post(title: str, description: str, tone: str, content: str) -> str | None:
    key = hash_prompt(title, description, tone)
    await redis_client.set(key, content, ex=3600)
