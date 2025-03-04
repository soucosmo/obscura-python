from .client import Client
from requests import get, RequestException


class ConfigMap:
    _client: Client

    def __init__(self, client: Client):
        self._client = client

    def read(self, key: str) -> dict:
        key = key.lstrip("/")  # Remove the leading slash if present

        url = self._client.get_url(
            "config-map/{}".format(key)
        )

        try:
            res = get(
                url,
                headers=self._client.get_headers()
            )

            if res.status_code == 200:
                return res.json()  # Returns the response json
            elif res.status_code == 404:
                raise Exception('Path not found') # Path not found
            else:
                raise Exception(res.text)  # Unknown error

        except RequestException as e:
            raise e  # Returns error as string

    def read_with_prefix(self, key: str) -> list:
        key = key.lstrip("/")  # Remove the leading slash if present

        url = self._client.get_url(
            "config-map/{}/prefix".format(key)
        )

        try:
            res = get(
                url,
                headers=self._client.get_headers()
            )

            if res.status_code == 200:
                return res.json()  # Returns the response json
            elif res.status_code == 404:
                raise Exception('Path not found') # Path not found
            else:
                raise Exception(res.text)  # Unknown error

        except RequestException as e:
            raise e  # Returns error as string
