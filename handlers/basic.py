from aiogram import Router, F
from aiogram.types import Message

from keyboard.basic import start_kb

router = Router()


@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer(text=f'Приветствую, {message.from_user.first_name}', reply_markup=start_kb)


@router.message(F.text.lower().startswith('пидор'))
async def pidor(message: Message):
    await message.answer(text='Сам такой!')


# @router.message(F.chat_type == private)
# async def echo(message: Message):
#     await message.answer(text=f'Ёпт, пиши нормально!')