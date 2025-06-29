import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

async def generate_post(title: str, description: str, tone: str = "friendly") -> str:
    style = {
        "friendly": "Дружелюбный, позитивный, лёгкий. Пиши как будто совет другу.",
        "expert": "Экспертный, уверенный, с опорой на факты и выгоду.",
        "funny": "Весёлый, с юмором, можно использовать шутки или смайлы."
    }.get(tone, "Дружелюбный, позитивный, лёгкий. Пиши как будто совет другу.")
    
    prompt = f"""
    Название: {title}
    Описание: {description}
    Тон: {style}
    
    Напиши короткий и продающий рекламный пост на русском языке (максимум 250 символов) для социальных сетей.
    """
    
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    
    json_data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(OPENROUTER_URL, headers=headers, json=json_data)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
