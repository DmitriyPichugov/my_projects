from fastapi import FastAPI
from models import PostRequest
from gpt import generate_post
from cache import get_cached_post, cache_post


app = FastAPI()

@app.post("/generate")
async def generate_ad(request: PostRequest):
    cached = await get_cached_post(request.title, request.description, request.tone)
    if cached:
        return {"text": cached}
    result = await generate_post(request.title, request.description, request.tone)
    await cache_post(request.title, request.description, request.tone, request.content)
    return {"text": result}
