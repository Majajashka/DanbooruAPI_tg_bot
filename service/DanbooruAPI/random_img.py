import time

import requests
from requests.auth import HTTPBasicAuth

basic = HTTPBasicAuth('majajashka', 'yTMKffX5AffivLDNDgYrydrv')
a = requests.get('https://danbooru.donmai.us/profile.json', auth=basic)

text_pattern = ('Rating: <b>{rating}</b>\n'
                'Score: <b>{score}</b>\n'
                'Image_url: {img_url}')  # 'Tags: <b>{tags}</b>\n'


def random_img(tags: str = '') -> tuple:
    start_time = time.time()
    params = {
        'tags': tags,
    }
    random1 = requests.get('https://danbooru.donmai.us/posts/random.json', params=params)  # auth=basic,
    data = random1.json()
    img_url = data['file_url']
    rating = data['rating']
    score = data['score']
    text = text_pattern.format(rating=rating, score=score, img_url=img_url)
    print(img_url)
    return text, img_url


def search_tag(tag: str):
    param = {
        'search[name_matches]': f'{tag}*',
        'search[hide_empty]': True,
        'search[order]': 'count'
    }
    response = requests.get('https://danbooru.donmai.us/tags.json', auth=basic, params=param)
    data = response.json()
    list_data = [tags['name'] for tags in data]
    post_count = [tags['post_count'] for tags in data]
    tags_dict = dict(zip(list_data, post_count))
    text = ''
    for key in tags_dict:
        text += f'<code>{key}</code>: {tags_dict.get(key)}\n'
    return text


def fuzzy_similar_tag(tag: str):
    param = {
        'search[fuzzy_name_matches]': f'{tag}*',
        'search[hide_empty]': True,
        'search[order]': 'count'
    }
    response = requests.get('https://danbooru.donmai.us/tags.json', auth=basic, params=param)
    data = response.json()
    list_data = [tags['name'] for tags in data]
    post_count = [tags['post_count'] for tags in data]
    tags_dict = dict(zip(list_data, post_count))
    text = ''
    for key in tags_dict:
        text += f'<code>{key}</code>: {tags_dict.get(key)}\n'
    return text
