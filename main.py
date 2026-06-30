from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart 
import os

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def greet(message: Message):
    await message.answer("Привет! Это бот для записи на индивидуальные тренировки")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())