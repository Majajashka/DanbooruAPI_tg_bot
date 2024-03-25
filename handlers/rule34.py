from aiogram import Router, F
from aiogram.types import Message, URLInputFile

from keyboard.resend_kb import photo_kb
from service.rule34.random_img import get_random_img

router = Router()


@router.message(F.text.lower().startswith('rule34'))
async def rule34_img(message: Message):
    msg = message.text.split()
    if msg[1].isdigit():
        if int(msg[1]) > 50:
            await message.answer(text='Куда тебе столько?')
            return
        digit_len = len(msg[1]) + 1
        first_word = len(msg[0]) + 1
        tags = message.text[first_word + digit_len:].split()
        for _ in range(int(msg[1])):
            try:
                text, img_url = get_random_img(tags)
                image = URLInputFile(url=img_url)
                await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
            except Exception as e:
                await message.answer(f'some error: {e}')
    else:
        tags = message.text[7:].split()
        try:
            text, img_url = get_random_img(tags)
            image = URLInputFile(url=img_url)
            await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
        except Exception as e:
            await message.answer(f'some error: {e}')


@router.message(F.text.lower().startswith('showtags rule34'))
async def rule34_img(message: Message):
    msg = message.text.split()
    if msg[2].isdigit():
        if int(msg[2]) > 50:
            await message.answer(text='Куда тебе столько?')
            return
        digit_len = len(msg[2]) + 1
        search_word = len(msg[0]) + len(msg[1]) + 2
        tags = message.text[search_word + digit_len:].split()
        for _ in range(int(msg[2])):
            try:
                text, img_url = get_random_img(tags, True)
                image = URLInputFile(url=img_url)
                if len(text) >= 1024:
                    await message.answer_photo(photo=image, reply_markup=photo_kb)
                    await message.answer(text=text)
                else:
                    await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
            except Exception as e:
                await message.answer(f'some error: {e}')
    else:
        tags = message.text[16:].split()
        try:
            text, img_url = get_random_img(tags, True)
            image = URLInputFile(url=img_url)
            await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
        except Exception as e:
            await message.answer(f'some error: {e}')
