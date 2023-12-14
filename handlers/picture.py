from aiogram.filters import Command
from aiogram import Router, types
import os
import random


pic_router = Router()


@pic_router.message(Command('pic'))
async def send_pic(message: types.Message):
    files = [f for f in os.listdir('images') if os.path.isfile(os.path.join('images', f))]

    if files:
        # Генерируем случайный индекс с использованием цикла
        random_index = random.randint(0, len(files) - 1)
        while True:
            random_index = random.randint(0, len(files) - 1)
            break

        random_file = os.path.join('images', files[random_index])
        file = types.FSInputFile(random_file)
        await message.answer_photo(
            photo=file,
            caption='Cat'
        )
