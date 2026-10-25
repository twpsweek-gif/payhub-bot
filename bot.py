from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import asyncio

BOT_TOKEN = "8815407012:AAHob5sUFfmw3XPgfLtqxuXdWup8w1Ufz8U"
# Твоя ссылка на Netlify (проверь, что она правильная!)
WEBAPP_URL = "https://musical-sfogliatella-db59bf.netlify.app" 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    # Красивая кнопка
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="✨ Открыть PayHub", web_app=WebAppInfo(url=WEBAPP_URL))]],
        resize_keyboard=True
    )
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"Добро пожаловать в экосистему PayHub.\n"
        f"Нажми кнопку ниже, чтобы войти в пространство 👇",
        reply_markup=kb
    )

async def main():
    print("✅ БОТ ГОТОВ! Жду пользователей...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())