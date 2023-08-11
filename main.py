import logging

from aiogram import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from data.loader import dp
from data.middlewares import ThrottlingMiddleware
import handlers

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    print("bot is running")

    dp.setup_middleware(ThrottlingMiddleware())
    dp.setup_middleware(LoggingMiddleware())
    executor.start_polling(dp)
