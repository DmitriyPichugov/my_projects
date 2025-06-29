import os
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

TONE_PROMPTS = {
    "friendly": "Дружелюбный, позитивный, лёгкий. Пиши как будто совет другу.",
    "expert":   "Экспертный, уверенный, с опорой на факты и выгоду.",
    "funny":    "Весёлый, с юмором, можно использовать шутки или смайлы."
}

async def generate_post(title: str, description: str, tone: str = "friendly") -> str:
    style = TONE_PROMPTS.get(tone, TONE_PROMPTS["friendly"])
    prompt = f"""
    Название: {title}
    Описание: {description}
    Тон: {style}
    
    Напиши короткий и продающий рекламный пост (максимум 250 символов) для социальных сетей.
    """
    
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()
