import requests
from requests.auth import HTTPBasicAuth
import time

basic = HTTPBasicAuth('majajashka', 'yTMKffX5AffivLDNDgYrydrv')
a = requests.get('https://danbooru.donmai.us/profile.json', auth=basic)

text_pattern = ('Rating: <b>{rating}</b>\n'
                'Score: <b>{score}</b>\n'
                'Image_url: {img_url}')  # 'Tags: <b>{tags}</b>\n'


def random_img(tags: str = '') -> tuple:
    params = {
        'tags': tags,
    }
    random1 = requests.get('https://danbooru.donmai.us/posts/random.json', auth=basic, params=params)
    data = random1.json()
    print(data)
    img_url = data['file_url']
    rating = data['rating']
    score = data['score']
    # tags = data['tag_string']
    # tags = tags.replace(' ', ', ')
    text = text_pattern.format(rating=rating, score=score, img_url=img_url)
    print(img_url)
    return text, img_url


print(random_img('score:>1000'))
