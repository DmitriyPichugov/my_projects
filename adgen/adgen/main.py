from fastapi import FastAPI
from adgen.models import PostRequest
from adgen.gpt import generate_post
from adgen.cache import get_cached_post, cache_post


app = FastAPI()

@app.post("/generate")
async def generate_ad(request: PostRequest):
    cached = await get_cached_post(request.title, request.description, request.tone)
    if cached:
        return {"text": cached}
    result = await generate_post(request.title, request.description, request.tone)
    await cache_post(request.title, request.description, request.tone, result)
    return {"text": result}
