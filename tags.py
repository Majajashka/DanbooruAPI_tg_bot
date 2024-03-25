tags = ''


def format_tags(tags: str):
    tags_format = tags.replace(', ', ' ')
    tags_format = tags_format.replace(',', ' ')
    tags_format = tags_format.split()
    formatted_tags = []
    for k in range(len(tags_format)):
        formatted_tags.append('-' + tags_format[k])
    return formatted_tags


print(format_tags(tags))
