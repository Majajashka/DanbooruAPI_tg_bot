from rule34Py import rule34Py

text = ('<b>Tags</b>: {tags}\n'
        '<b>Score</b>: {score}\n'
        '<b>Image_url</b>: {url}')


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


def get_random_img(search_tags: list, tags_display: bool = False):
    tags = None
    negative_tags = ['-futa', '-futanari', '-furry', '-gay', '-yaoi', '-femboy', '-huge_breasts', '-big_belly',
                     '-weight_gain', '-cannibalism', '-dead', '-death', '-murder', '-murdered', '-animal', '-male_only',
                     '-anthro', '-canine', '-canid', '-canis', '-mammal', '-wolf', '-fur', 'pokemon_(species)',
                     'animal_genitalia', 'animal_penis', 'feral'
                     ]
    rule34 = rule34Py()
    search = rule34.random_post(search_tags+negative_tags)
    if tags_display:
        tags = ', '.join(search.tags)
    formatted_text = text.format(url=search.image, score=search.score, tags=tags)
    return formatted_text, search.image
