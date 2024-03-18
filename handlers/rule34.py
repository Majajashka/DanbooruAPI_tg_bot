from aiogram import Router, F
from aiogram.types import Message, URLInputFile

from service.rule34.random_img import get_random_img
from keyboard.resend_kb import photo_kb


router = Router()


@router.message(F.text.lower().startswith('rule34'))
async def rule34_img(message: Message):
    msg = message.text.split()
    if msg[1].isdigit():
        digit_len = len(msg[1]) + 1
        tags = message.text[7 + digit_len:].split()
        print(tags)
        for _ in range(int(msg[1])):
            try:
                text, img_url = get_random_img(tags)
                image = URLInputFile(url=img_url)
                await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
            except Exception as e:
                await message.answer(f'some error: {e}')
    else:
        tags = message.text[7:].split()
        print(tags)
        try:
            text, img_url = get_random_img(tags)
            image = URLInputFile(url=img_url)
            await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
        except Exception as e:
            await message.answer(f'some error: {e}')
