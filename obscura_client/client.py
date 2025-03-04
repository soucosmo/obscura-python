from requests import get

class Client:
    _url: str
    _token: str
    http = get

    def __init__(self, url: str, token: str) -> Client:
        self._url = url
        self._token = token

    def get_url(self, path: str) -> str:
        if not path:
            return path

        return '{}/{}'.format(self._url, path)

    def get_token(self) -> str:
        return self._token
