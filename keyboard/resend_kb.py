from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

PhotoButtons = [
    InlineKeyboardButton(
        text='✅',
        callback_data='approve'
    )
]

photo_builder = InlineKeyboardBuilder()
photo_builder.row(*PhotoButtons)
photo_kb = photo_builder.as_markup(
    resize_keyboard=True
)
