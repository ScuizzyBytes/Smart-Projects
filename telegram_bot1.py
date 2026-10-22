import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

TOKEN = "8754531363:AAGiUlJFwCTEkElghbZ10QQtP86XSTB5TtM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def make_account_link_kb(username: str , button_text: str) -> InlineKeyboardMarkup:
    """Creates an inline keyboard with a button that links to the user's Telegram account."""
    clean_username = username.lstrip("@")

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=button_text,
                    url=f"https://t.me/{clean_username}"
                )
            ]
        ]
    )

@dp.message(Command("Second_acc"))
async def start_second_acc(message: Message):

    MY_USERNAME = "@S5ckmytick"

    kb = make_account_link_kb(MY_USERNAME, "Go to my Telegram account")
    await message.answer("Click the button below to go to my Telegram account:", reply_markup=kb)

@dp.message(F.text == "Hello")
async def handle_hello(message: Message):
    await message.answer("Hello there!")

@dp.message(F.text == "How are you?")
async def handle_how_are_you(message: Message):
    await message.answer("I'm doing well, thank you!")

@dp.message(F.text)
async def handle_hi(message: Message):
    await message.answer(f"You said: {message.text}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
logging.basicConfig(stream=sys.stdout, level=logging.INFO)