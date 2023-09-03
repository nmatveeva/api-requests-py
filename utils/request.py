from dataclasses import dataclass

import requests


@dataclass
class Response:
    status_code: int
    test: str
    as_dict: object
    headers: dict


class APIRequest:

    def get(self, url):
        response = requests.get(url)
        return self.__get_response(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_response(response)

    def delete(self, url):
        response = requests.delete(url)
        return self.__get_response(response)

    def put(self, url, payload, headers):
        response = requests.put(url, data=payload, headers=headers)
        return self.__get_response(response)

    def __get_response(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )
