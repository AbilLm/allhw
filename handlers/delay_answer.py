from aiogram import Router, F, types
from aiogram.filters import Command
from bot import bot, scheduler



delay_answer_router = Router()




@delay_answer_router.message(Command("remind"))
async def reminder(message: types.Message):
    await message.answer('Что вам напомнить?\n'
                         '(напишите "напомни" перед тем как установите задачу)')

@delay_answer_router.message(F.text.startswith("напомни"))
async def reminderr(message: types.Message):
    reminder_text = message.text[7:]  # Убираем "напомни " из начала строки
    await message.answer(f"Напоминаю: {reminder_text}")


    scheduler.add_job(
        send_reminder,
        trigger="interval",
        seconds=10,
        args=[message.chat.id, reminder_text]
    )

async def send_reminder(chat_id, text):
    await bot.send_message(chat_id=chat_id, text=f"Напоминаю: {text}")