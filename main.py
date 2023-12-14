import asyncio
import logging
from aiogram import types
from aiogram.filters import Command
from bot import bot, dp
from handlers.picture import pic_router
from handlers.start import start_router
from handlers.myinfo import info_router
from handlers.echo import echo_router
from handlers.catalog import catalog_router













async def main():
    await bot.set_my_commands([

    ]
    )
    dp.include_router(pic_router)
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(catalog_router)



    dp.include_router(echo_router)



    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())