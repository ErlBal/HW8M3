import asyncio
import logging
from handlers.start import start_router
from handlers.info import info_router
from handlers.pictures import picture_router
from handlers.shop import shop_router
from bot import bot, dp, scheduler
from handlers.question import questions_router
from db.shopdb import init_db, create_tables, populate_tables
from aiogram.types import BotCommand
from handlers.schedular import scheduler_router, remind_me
from parser.mashinakg import dbcars


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()
    await remind_me()
    dbcars()



async def main():
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Начать"),
            BotCommand(command="myinfo", description="Получи инфромацию о себе"),
            BotCommand(command="picture", description="Получить картинку"),
            BotCommand(command="ask", description="Опросник"),
            BotCommand(command="shop", description="Магазин"),
        ]
    )

    dp.startup.register(on_startup)

    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    dp.include_router(scheduler_router)

    scheduler.start()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

