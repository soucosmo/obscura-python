class Client:
    _url: str
    _token: str
    _headers = dict

    def __init__(self, url: str, token: str):
        self._url = url + '/api'
        self._token = token
        self._headers = {
            'Authorization': 'Bearer {}'.format(token)
        }

    def get_url(self, path: str) -> str:
        if not path:
            return path

        return '{}/{}'.format(self._url, path)

    def get_headers(self) -> dict:
        return self._headers
