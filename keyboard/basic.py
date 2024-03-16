from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

start_builder = ReplyKeyboardBuilder()

start_buttons = [
    KeyboardButton(text='More Neko!!!'),
    KeyboardButton(text='10 Neko!!!')
]

start_builder.row(*start_buttons, width=1)
start_kb = start_builder.as_markup(
    resize_keyboard=True
)
