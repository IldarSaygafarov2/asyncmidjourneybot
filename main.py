import logging

from aiogram import types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

import api
import keyboards as kb
import states
from loader import bot, dp
from middlewares import rate_limit, ThrottlingMiddleware

logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=["start"])
@rate_limit(25, "/start")
async def command_start(message: types.Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name

    await bot.send_message(chat_id, f"Привет, {first_name}")
    await bot.send_message(chat_id, "Выбери один из вариантов для генерации фотографии из представленных ниже",
                           reply_markup=kb.start_menu())


@dp.message_handler(lambda msg: msg.text == "По тексту")
async def generate_image_by_text_prompt(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Напишите ваш шаблон для генерации фотографии")
    await bot.send_message(chat_id, """
<b>Рекомендация:</b>

<i>Напишите ваш запрос на английском языке, для лучшей ее генерации с сохранением делатей.</i>
""", parse_mode="HTML")
    await states.PromptStates.PROMPT.set()


@dp.message_handler(state="*")
@rate_limit(5)
async def get_prompt_generate_img(message: types.Message):
    chat_id = message.from_user.id
    # argument = message.get_args()
    # state = dp.current_state(user=chat_id)
    try:
        resp = await api.make_reqeust(prompt=message.text)
        generated = await api.get_result_by_message_id(resp["messageId"])

        for img_url in generated["response"]["imageUrls"]:
            await bot.send_photo(chat_id, photo=img_url)
        await bot.send_message(chat_id, "Можете написать другой запрос для генерации фотографии")
    except Exception as e:
        print(e)
        await message.reply(f"Произошла ошибка попробуйте позже")


@dp.message_handler(lambda msg: msg.text == "По фотографии")
async def generate_image_by_img_and_prompt(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Отправьте ссылку на фотографию и напишите ваш запрос для геренации")


if __name__ == '__main__':
    print("bot is running")

    dp.setup_middleware(ThrottlingMiddleware())
    dp.setup_middleware(LoggingMiddleware())
    executor.start_polling(dp)
