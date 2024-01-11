from aiogram import types, Router, F
from aiogram.filters import Command

bot_router = Router()

bad = ('дурак', 'лох', 'ебан')

@bot_router.message(F.chat.type.in_({'group', 'supergroup'}))


@bot_router.message(F.chat.type == 'group')
async def catch(message: types.Message):
    text = message.text.lower()
    # Получаем информацию об администраторах чата
    admins = await message.bot.get_chat_administrators(message.chat.id)
    admin_ids = [admin.user.id for admin in admins]

    # Получаем информацию о чате
    chat_info = await message.bot.get_chat(message.chat.id)

    # Проверяем, является ли отправитель владельцем чата
    if message.from_user.id == chat_info.id:
        await message.reply('Вы владелец чата. Я не могу вас забанить.')
    elif message.from_user.id not in admin_ids:
        for word in bad:
            if word in text:
                # Отправляем ответ и затем забаним пользователя
                await message.reply('Не выражайся. Вы забанены.')
                await message.bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                break
    elif message.from_user.id in admin_ids:
        for word in bad:
            if word in text:
                await message.reply('Вы администратор чата. Я не могу вас забанить.')

