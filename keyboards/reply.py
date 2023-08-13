from aiogram import types


def start_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.row(
        types.KeyboardButton(text="Сгенерировать"),
        # types.KeyboardButton(text="По фотографии"),
    )
    return kb
