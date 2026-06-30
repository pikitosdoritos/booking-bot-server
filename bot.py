import asyncio
import json
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart

TOKEN = "8810629058:AAE4THdq4wX6-7P7vxDszBpJHipMKelG2MY"
# Посилання на вашу завантажену HTML-сторінку (обов'язково HTTPS)
WEB_APP_URL = "http://127.0.0.1:5500/index.html" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    # Створюємо кнопку, яка відкриває UI форму всередині Telegram
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Відкрити анкету", web_app=WebAppInfo(url=WEB_APP_URL))]
        ],
        resize_keyboard=True
    )
    await message.answer("Привіт! Натисніть кнопку нижче, щоб заповнити форму:", reply_markup=keyboard)

# Хендлер, який отримує дані після закриття форми
@dp.message(F.web_app_data)
async def handle_web_app_data(message: Message):
    # Отримуємо JSON-рядок з форми
    raw_data = message.web_app_data.data
    data = json.loads(raw_data)
    
    # Витягуємо збережені користувачем дані
    user_name = data.get("name")
    user_city = data.get("city")
    
    response_text = f"🎉 **Дані успішно отримано!**\n\n👤 Ім'я: {user_name}\n📍 Місто: {user_city}"
    await message.answer(response_text, parse_mode="Markdown")

async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
