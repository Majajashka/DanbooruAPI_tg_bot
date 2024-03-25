from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, URLInputFile

from keyboard.resend_kb import photo_kb
from keyboard.set_tags import form_set_tags_kb
from service.DanbooruAPI.danbooru import Danbooru, Format, ApiError

router = Router()
danb = Danbooru()
form = Format()


@router.message(F.text.lower().startswith('set'))
async def set_tags(message: Message):
    await message.answer(text=message.text[4:],
                         reply_markup=form_set_tags_kb(message.text[4:]))


@router.message(F.text.lower().startswith('tags'))
async def random_image(message: Message):
    msg = message.text.split()
    msg.remove(msg[0])
    tags = " ".join(msg)
    if msg[0].isdigit():  # message.text example - tags 10 solo rating:g
        tags = tags[len(tags[0]) + 1:]
        for i in range(int(tags[0])):
            try:
                request = danb.image(tags=tags)
                img_url, text = request.file_url, form.format_image(request)
                image = URLInputFile(url=img_url)
                await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
            except ApiError as e:
                await message.answer(e)
            except Exception as e:
                await message.answer(f'[{i + 1}] some error: {e}\n'
                                     f'image_url: {img_url if img_url else None}')
    else:
        try:
            request = danb.image(tags=tags)
            img_url, text = request.file_url, form.format_image(request)
            image = URLInputFile(url=img_url)
            await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
        except ApiError as e:
            await message.answer(e)
        except Exception as e:
            await message.answer(f'some error: {e}')


@router.message(F.text.lower().startswith('search'))
async def find_tag(message: Message):
    tag = message.text[7:]
    text = danb.tags(tag)
    await message.answer(text=text)


@router.callback_query(F.data == 'approve')
async def resend(callback: CallbackQuery):
    msg_id = callback.message.message_id
    await callback.message.copy_to(chat_id=-1002026876514)
    await callback.message.edit_reply_markup(reply_markup=None)
