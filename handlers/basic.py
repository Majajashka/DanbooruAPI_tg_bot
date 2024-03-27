import re
import requests

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
        caption = message.reply_to_message.text
        if not caption:
            await message.answer('Отвечай на сообщение...')
            return
    link = re.search("(?P<url>https?://\S+)", caption).group("url")
    md5 = link[link.rfind('/') + 1: link.rfind('.')]
    response = requests.get(url=f'https://danbooru.donmai.us/posts.json?md5={md5}')
    data = response.json()['media_asset']['variants']
    url_dict = {variants['type']: variants['url'] for variants in data}
    text = ''
    for resolution, url in url_dict.items():
        text += (f'<b>{resolution}</b>: '
                 f'{url}\n')
    await message.answer(text=text, disable_web_page_preview=True)


@router.message(F.text.lower() == 'json')
async def get_md5(message: Message):
    caption = message.reply_to_message.caption
    if not caption:
        caption = message.reply_to_message.text
        if not caption:
            await message.answer('Отвечай на сообщение...')
            return
    link = re.search("(?P<url>https?://\S+)", caption).group("url")
    md5 = link[link.rfind('/') + 1: link.rfind('.')]
    json_link = f'https://danbooru.donmai.us/posts.json?md5={md5}'
    await message.answer(text='json:'
                              f'{json_link}')
