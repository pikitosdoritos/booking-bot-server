from dotenv import load_dotenv
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import CommandStart, Command
import json
import os

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def greet(message: Message):
    await message.answer("Привет! Это бот для записи на индивидуальные тренировки")

@dp.message(Command("record"))
async def record_for_training(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Открыть анкету для записи", web_app=WebAppInfo(url=WEB_APP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer("Нажмите кнопку ниже, чтобы заполнить форму:", reply_markup=keyboard)

@dp.message(F.web_app_data)
async def processing_web_data(message: Message):
    raw_data = message.web_app_data.data
    json_data = json.loads(raw_data)

    name = raw_data.get("name")
    phone_number = raw_data.get("phone")
    date = raw_data.get("date")

    response_text = f"🎉 **Дані успішно отримано!**\n\n Имя: {name}\n Телефон: {phone_number}\n Дата: {date}\n\n Ожидайте подтверждение от тренера"
    await message.answer(response_text, parse_mode="Markdown")
    await bot.send_message(
        ADMIN_ID, 
        f"Имя: {name}\n Телефон: {phone_number}\n Дата: {date}",
        reply_markup= InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                    text="✅ Подтвердить",
                    callback_data="confirm"
                ), 
                InlineKeyboardButton(
                    text="❌ Отклонить",
                    callback_data="decline"
                )
                ]
            ]
        ))

@dp.callback_query(F.data == "confirm")
async def confirm_request(callback: CallbackQuery):
    await callback.answer("Заявка подтверждена")

@dp.callback_query(F.data == "decline")
async def confirm_request(callback: CallbackQuery):
    await callback.answer("Заявка отклонена")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())