import logging

from aiogram import types

from data.loader import bot, dp
from data.middlewares import rate_limit
from keyboards import reply as kb

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
@rate_limit(25, "/start")
async def command_start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name

    await bot.send_message(chat_id, f"Привет, {first_name}")
    await bot.send_message(chat_id, "Нажмите на кнопку ниже для генерации фотографии",
                           reply_markup=kb.start_menu())


@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    chat_id = message.chat.id

    msg = """
Приветствую тебя, дорогой пользователь.
Данный бот служит для генерации изображений по вашему шаблону.

Шаблон желательно писать на английском языке, для лучшей генерации фотографий по вашему примеру.

Так же после того, как вы получите ваши фотографии, вы можете скопировать одну из ссылок на фотографию (будет под самой фотографией)
и добавить описание именно для нее.

Приятного использования!
"""
    await bot.send_message(chat_id, msg)
