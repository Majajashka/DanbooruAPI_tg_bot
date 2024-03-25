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
    if len(message.text.split()) < 2:
        await message.answer("Please provide both the number of images and tags.")
        return
    msg.remove(msg[0])
    tags = " ".join(msg)
    if tags[0].isdigit():
        post_count = msg[0]
        tags = tags[len(post_count) + 1:]
    else:
        post_count = 1
    print(f'post count: {post_count}\n'
          f'tags: {tags}')
    for i in range(int(post_count)):
        try:
            request = danb.image(tags=tags)
            img_url, text = request.file_url, form.format_image(request)
            image = URLInputFile(url=img_url)
            await message.answer_photo(photo=image, caption=text, reply_markup=photo_kb)
        except ApiError as e:
            await message.answer(f'{e}')
        except Exception as e:
            await message.answer(f'Post Number: [{i + 1}]\n'
                                 f'Some error: {e}\n'
                                 f'Image_url: {img_url if img_url else "None"}')


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
