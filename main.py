from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart 
import json
import os

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def greet(message: Message):
    await message.answer("Привет! Это бот для записи на индивидуальные тренировки")

@dp.message(F.text)
async def create_record(message: Message):
    record = message.text

    with open("user_data.json", "w", encoding="utf-8") as f:
        json.dump(record, f, indent=4, ensure_ascii=False)

    await message.answer("Ваша запись внесена в базу, ожидайте подтверждения от тренера.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())