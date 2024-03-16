import requests
from requests.auth import HTTPBasicAuth
import time

basic = HTTPBasicAuth('majajashka', 'yTMKffX5AffivLDNDgYrydrv')
a = requests.get('https://danbooru.donmai.us/profile.json', auth=basic)

text_pattern = ("Image_url: {img_url}\n")  # 'Tags: <b>{tags}</b>\n'


def random_img(tags: str = '') -> tuple:
    params = {
        'tags': tags,
    }
    random1 = requests.get('https://danbooru.donmai.us/posts/random.json', auth=basic, params=params)
    data = random1.json()
    img_url = data['file_url']
    # tags = data['tag_string']
    # tags = tags.replace(' ', ', ')
    text = text_pattern.format(img_url=img_url)
    return text, img_url

