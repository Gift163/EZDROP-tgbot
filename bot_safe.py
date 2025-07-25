
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, Message
from aiogram.utils import executor

# Получаем токен из переменных окружения
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🎁 Open Case", web_app=WebAppInfo(url="https://ezdrop-tgbot.onrender.com")),
        InlineKeyboardButton("💸 Top Up Balance", callback_data="topup"),
        InlineKeyboardButton("👥 Invite Friends", callback_data="referral")
    )

    welcome_text = (
        "👋 Welcome to *EZDROP*, {}!

"
        "🎮 Play & win real tokens and NFTs right inside Telegram.

"
        "💎 Open daily cases
"
        "⚡ Upgrade items
"
        "🎯 Complete missions
"
        "👑 Earn ranks & rewards

"
        "Ready to drop? Let’s go! 🚀"
    )

    await message.answer(welcome_text.format(message.from_user.first_name), reply_markup=keyboard, parse_mode="Markdown")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
