
import os
import asyncio
from flask import Flask, render_template
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, Message

# Flask-приложение
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Telegram Bot
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

async def start_bot():
    await dp.start_polling()

# Запуск Flask + Telegram одновременно
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())  # запускаем бота в фоне
    app.run(host="0.0.0.0", port=10000)
