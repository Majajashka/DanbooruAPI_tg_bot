import re

from aiogram import Router, F
from aiogram.types import Message

from keyboard.basic import start_kb

router = Router()


@router.message(F.text == '/start')
async def start(message: Message):
    await message.answer(text=f'Приветствую, {message.from_user.first_name}', reply_markup=start_kb)


@router.message(F.text.lower() == 'md5')
async def get_md5(message: Message):
    caption = message.reply_to_message.caption
    if not caption:
        await message.answer('Отвечай на сообщение...')
    link = re.search("(?P<url>https?://\S+)", caption).group("url")
    md5 = link[link.rfind('/') + 1: link.rfind('.')]
    await message.answer(text=md5)


@router.message(F.text.lower() == 'json')
async def get_md5(message: Message):
    caption = message.reply_to_message.caption
    if not caption:
        await message.answer('Отвечай на сообщение...')
    link = re.search("(?P<url>https?://\S+)", caption).group("url")
    md5 = link[link.rfind('/') + 1: link.rfind('.')]
    json_link = f'https://danbooru.donmai.us/posts.json?md5={md5}'
    await message.answer(text='json:\n'
                              f'{json_link}')
