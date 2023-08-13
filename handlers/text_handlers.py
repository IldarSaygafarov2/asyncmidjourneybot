from aiogram import types

import api
import states
from data.loader import bot, dp
from data.middlewares import rate_limit


@dp.message_handler(lambda msg: msg.text == "Сгенерировать")
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
@rate_limit(30)
async def get_prompt_generate_img(message: types.Message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id,
                           "<i>Ваша фотография генерируется, это может занять до одной минуты.</i> "
                           "<b>Убедительая просьба не писать сообщения в течении минуты</b>",
                           parse_mode="HTML")
    try:
        resp = await api.make_reqeust(prompt=message.text)
        if resp.get("isNaughty"):
            await bot.send_message(chat_id, f"<i>Вы написали недопустимое слово: {resp.get('phrase')}</i>",
                                   parse_mode="HTML")
            return
        generated = await api.get_result_by_message_id(resp["messageId"])
        for img_url in generated["response"]["imageUrls"]:
            await bot.send_photo(chat_id, photo=img_url, caption=f"Ссылка на фотографию: {img_url}")

        await bot.send_message(chat_id,
                               "<i>Вы можете скопировать ссылку нужной вам фотографии, поставить пробел и добавить для нее описание"
                               "\nтаким способом ваша фотография изменится по новому примеру</i>",
                               parse_mode="HTML")
        await bot.send_message(chat_id, "Напишите другой запрос для генерации изображений")
    except Exception as e:
        print(e, e.__class__)
        await message.reply(f"<b>Произошла ошибка попробуйте позже</b>", parse_mode="HTML")
