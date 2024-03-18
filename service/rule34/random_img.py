from rule34Py import rule34Py

text = ('Score: {score}\n'
        'Image_url: {url}')


# def get_random_img(tags):
#     params = {
#         'tags': tags,
#         'limit': 1
#     }
#     response = requests.get(url='https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&json=1', params=params)
#     data = response.json()[0]
#     score = data['score']
#     img_url = data['file_url']
#     formatted_text = text.format(url=img_url, score=score)
#     return formatted_text, img_url


def get_random_img(tags: list):
    rule34 = rule34Py()
    search = rule34.random_post(tags)
    formatted_text = text.format(url=search.image, score=search.score)
    return formatted_text, search.image
