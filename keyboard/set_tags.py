from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


def form_set_tags_kb(message: str):
    tags_builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=message)
    back = KeyboardButton(text='Back')
    tags_builder.row(button, back, width=1)
    tags_kb = tags_builder.as_markup(
        resize_keyboard=True
    )
    return tags_kb
