from aiogram import Router, types
from aiogram.filters import Command
import bot

info_router = Router()


@info_router.message(Command('myinfo'))
async def info_handler(message: types.Message):
    await message.answer(f"Вас зовут {message.from_user.first_name}, ваш ник {message.from_user.username}, фамилия ваша {message.from_user.last_name}, ваш id {message.from_user.id}")
