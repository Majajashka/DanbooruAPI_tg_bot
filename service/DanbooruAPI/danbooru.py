import requests
from requests.auth import HTTPBasicAuth


class ApiError(Exception):
    """Api Error"""
    pass


class Danbooru:
    """Danbooru API wrapper"""

    def __init__(self):
        """Constructor"""
        self.password = 'yTMKffX5AffivLDNDgYrydrv'
        self.login = 'majajashka'
        self.auth = HTTPBasicAuth(self.login, self.password)
        self.base_url = 'https://danbooru.donmai.us'

    @staticmethod
    def _handle_error(response):
        data = response.json()
        if response.status_code != 200:
            raise ApiError(f'Error code: {response.status_code}\n'
                           f'Error: {data.get("message", "unknown error")}')
        elif data.get('file_url') is None:
            raise ApiError('URL not found')
        return data

    def image(self, tags: str = ''):
        """Returns link and info of random image

        :param tags: Tags seperated by space
        :type tags: str

        :return: Tuple of text and image url
        """
        params = {'tags': tags}
        response = requests.get(f'{self.base_url}/posts/random.json', params=params, auth=self.auth)
        data = self._handle_error(response)
        return Post.from_json(data)

    def tags(self, tag: str) -> str:
        """Returns tags

        :param tag: Tag
        :type tag: str

        :return: Tags sorted by post count
        """
        param = {
            'search[name_regex]': f'.*{tag}.*',
            'search[hide_empty]': True,
            'search[order]': 'count'
        }
        response = requests.get(f'{self.base_url}/tags.json', auth=self.auth, params=param)
        data = response.json()
        list_data = [tags['name'] for tags in data]
        post_count = [tags['post_count'] for tags in data]
        tags_dict = dict(zip(list_data, post_count))
        return Format().format_tags(tags=tags_dict)


class Format:
    def __init__(self):
        self.templates = {
            'tags': 'Tags: <b>{}</b>',
            'rating': 'Rating: <b>{}</b>',
            'file_url': 'Image_URL: {}',
            'score': 'Score: <b>{}</b>'
        }

    def format_image(self, post) -> str:
        required_info = {
            'tags': False,
            'rating': True,
            'score': True,
            'file_url': True
        }
        text = ''
        if required_info['tags'] is True:
            text += self.templates['tags'].format(post.tags) + '\n'
        if required_info['rating'] is True:
            text += self.templates['rating'].format(post.rating) + '\n'
        if required_info['score'] is True:
            text += self.templates['score'].format(post.score) + '\n'
        if required_info['file_url'] is True:
            text += self.templates['file_url'].format(post.file_url) + '\n'
        return text

    @staticmethod
    def format_tags(tags: dict) -> str:
        if not tags:
            return "Probably nothing..."
        text = ''
        for key in tags:
            text += f'<code>{key}</code>: {tags.get(key)}\n'
        return text


class Post:
    @staticmethod
    def from_json(json):
        pfile_url = json["file_url"]
        pid = json["id"]
        pscore = json["score"]
        prating = json['rating']
        file_ext = json['file_ext']
        tags = json['tag_string']

        return Post(pid, pfile_url, pscore, prating, file_ext, tags)

    def __init__(self, id: int, url: str, score: int, rating: str, file_ext: str, tags: str):
        self._id = id
        self._url = url
        self._score = score
        self._rating = rating
        self._file_ext = file_ext
        self._tags = tags

    @property
    def id(self) -> int:
        return self._id

    @property
    def file_url(self) -> str:
        return self._url

    @property
    def rating(self) -> str:
        return self._rating

    @property
    def score(self) -> int:
        return self._score

    @property
    def file_ext(self) -> str:
        return self._file_ext

    @property
    def tags(self) -> str:
        return self._tags


if __name__ == '__main__':
    danboru = Danbooru()
    edit = Format()
    a = danboru.image('dick')
    print(a.file_ext)
    print(edit.format_image(a))
