from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StateGroup, State
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import F
from aiogram.filters import CommandStart
import aiohttp
import asyncio
import os
from dotenv import load_dotenv


load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(storage=MemoryStorage())

class PostForm(StateGroup):
    title = State()
    description = State()
    tone = State()

tone_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Дружелюбный", callback_data="friendly")],
    [InlineKeyboardButton(text="Экспертный", callback_data="expert")],
    [InlineKeyboardButton(text="Юмористичный", callback_data="funny")],
])

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer("Привет! Я помогу тебе с созданием рекламного поста с твоим товаром, подберу наиболее интересные варианты продвижения. Введи название товара:")
    await state.set_state(PostForm.title)

@dp.message(PostForm.title)
async def get_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer("Теперь опиши товар:")
    await state.set_state(PostForm.description)

@dp.message(PostForm.description)
async def get_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Выбери стиль поста:", reply_markup=tone_keyboard)
    await state.set_state(PostForm.tone)

@dp.callback_query(F.data.in_(["friendly", "expert", "funny"]))
async def tone_selected(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(tone=callback.data)
    data = await state.get_data()
    await callback.message.answer("Генерирую пост...")
    
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8003/generate", json={
            "title": data["title"],
            "description": data["description"],
            "tone": data["tone"]
        }) as resp:
            result = await resp.json()
            await callback.message.answer(result["text"])
        
        await state.clear()

if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))
