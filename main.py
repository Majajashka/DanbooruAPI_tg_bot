import asyncio
import logging

from aiogram import Dispatcher, Bot

from config import config
from handlers import basic, random_image, rule34

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - [%(levelname)s] - %(name)s - "
                           "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")


async def main():
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(random_image.router, rule34.router, basic.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
