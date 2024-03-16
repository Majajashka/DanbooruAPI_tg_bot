from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, URLInputFile

from keyboard.resend_kb import photo_kb
from keyboard.set_tags import form_set_tags_kb

from service.DanbooruAPI.random_img import random_img

router = Router()


@router.message(F.text.lower() == 'more neko!!!')
async def more_neko(message: Message):
    text, img_url = random_img()
    image = URLInputFile(url=img_url)
    await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)


@router.message(F.text.lower() == '10 neko!!!')
async def ten_neko(message: Message):
    for _ in range(10):
        text, img_url = random_img()
        image = URLInputFile(url=img_url)
        await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)


@router.message(F.text.lower().startswith('set tags'))
async def set_tags(message: Message):
    await message.answer(text=message.text[4:],
                         reply_markup=form_set_tags_kb(message.text[4:]))


@router.message(F.text.lower().startswith('tags'))
async def tags(message: Message):
    msg = message.text.split()
    if msg[1].isdigit():
        digit_len = len(msg[1]) + 1
        search_tags = message.text[5 + digit_len:]
        print(search_tags)
        for _ in range(int(msg[1])):
            try:
                text, img_url = random_img(search_tags)
                image = URLInputFile(url=img_url)
                await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
            except Exception as e:
                await message.answer(f'some error: {e}')
    else:
        try:
            text, img_url = random_img(message.text[5:])
            image = URLInputFile(url=img_url)
            await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
        except Exception as e:
            await message.answer(f'some error: {e}')


@router.callback_query(F.data == 'approve')
async def resend(callback: CallbackQuery):
    msg_id = callback.message.message_id
    await callback.message.copy_to(chat_id=-1002026876514)
    await callback.message.edit_reply_markup(reply_markup=None)
