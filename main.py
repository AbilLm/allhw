import asyncio
import logging
from aiogram import types
from aiogram.filters import Command
from bot import bot, dp, scheduler
from handlers import (
    start_router,
    pic_router,
    catalog_router,
    echo_router,
    hw3_router,
    info_router,
    delay_answer_router,
    bot_router

)

from db.queries import init_db, create_tables, populate_tables
from handlers.catalog import get_catalog_router





async def on_startup(dispatcher):
    print('Бот в онлайне')
    init_db()
    create_tables()
    populate_tables()

async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start_quest", description='Опросник'),
        types.BotCommand(command='my_products', description='Товары'),
        types.BotCommand(command='ban', description='бан')
    ]
    )
    dp.include_router(pic_router)
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(catalog_router)
    dp.include_router(hw3_router)
    dp.include_router(get_catalog_router)
    dp.include_router(delay_answer_router)
    dp.include_router(bot_router)


    scheduler.start()



    dp.startup.register(on_startup)


    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())