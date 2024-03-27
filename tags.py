text = 'balls_bigger_than_body, balls_bigger_than_head, balls_bigger_than_torso, belly_bigger_than_body, belly_bigger_than_building, breasts_bigger_than_head, colossal_belly, colossal_penis hyper, hyper_balls, hyper_belly, hyper_breasts, hyper_penis, impossible_fit, penis_bigger_than_body, penis_longer_than_knee'


def format_tags(tags: str):
    tags_format = tags.replace(', ', ' ')
    tags_format = tags_format.replace(',', ' ')
    tags_format = tags_format.split()
    formatted_tags = []
    for k in range(len(tags_format)):
        formatted_tags.append('-' + tags_format[k])
    return formatted_tags


print(format_tags(text))
