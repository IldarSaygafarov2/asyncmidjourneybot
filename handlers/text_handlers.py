from aiogram import types

import api
import states
from data.loader import bot, dp
from data.middlewares import rate_limit


@dp.message_handler(lambda msg: msg.text == "По тексту")
async def generate_image_by_text_prompt(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Напишите ваш шаблон для генерации фотографии")
    await bot.send_message(chat_id, """
<b>Рекомендация:</b>

<i>Напишите ваш запрос на английском языке, для лучшей ее генерации с сохранением деталей.</i>
<i>
После генерации фотографии, вы можете скопировать её ссылку добавить в запрос и добавить для нее новое описание
Таким образом вы измените фотографию, которую получили
</i>
""", parse_mode="HTML", reply_markup=types.ReplyKeyboardRemove())
    await states.PromptStates.PROMPT.set()


@dp.message_handler(state="*")
@rate_limit(5)
async def get_prompt_generate_img(message: types.Message):
    chat_id = message.from_user.id
    try:
        resp = await api.make_reqeust(prompt=message.text)
        if resp.get("isNaughty"):
            await bot.send_message(chat_id, f"Вы написали недопустимое слово: {resp.get('phrase')}")
            return
        generated = await api.get_result_by_message_id(resp["messageId"])
        for img_url in generated["response"]["imageUrls"]:
            await bot.send_photo(chat_id, photo=img_url, caption=f"Ссылка на фотографию: {img_url}")

        await bot.send_message(chat_id,
                               "Вы можете скопировать ссылку нужной вам фотографии и добавить для нее описание"
                               "\nтаким способом ваша фотография изменится по новому примеру",
                               )
        await bot.send_message(chat_id, "Можете написать другой запрос для генерации фотографии")
    except Exception as e:
        print(e, e.__class__)
        await message.reply(f"Произошла ошибка попробуйте позже")
