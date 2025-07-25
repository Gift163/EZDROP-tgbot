
import os
import asyncio
from flask import Flask, render_template
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

# Flask App
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
    await message.answer("Привет! Это Telegram-бот EZDROP.")

async def start_bot():
    await dp.start_polling()

# Запуск Flask + Telegram
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())  # Запуск бота в фоне
    app.run(host="0.0.0.0", port=10000)
