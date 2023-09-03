from json import dumps

from api_clinet.base_api_client import BaseApiClient
from config import BASE_URI
from tests.helpers.people_api_helpers import generate_unique_name
from utils.request import APIRequest


class PeopleApiClient(BaseApiClient):

    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest()

    def create_user(self, body=None):
        last_name, response = self.__create_user_with_unique_last_name(body)
        return last_name, response

    def __create_user_with_unique_last_name(self, body=None):
        if body is None:
            last_name = f'Last{generate_unique_name()}'
            payload = dumps({
                'fname': 'FirstName',
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return last_name, response

    def delete_user(self, user_id):
        url = f'{BASE_URI}/{user_id}'
        return self.request.delete(url)

    def read_all_users(self):
        return self.request.get(self.base_url)

    def read_user_by_id(self, user_id):
        url = f'{BASE_URI}/{user_id}'
        return self.request.get(url)

    def update_user(self, user_id, first_name, last_name):
        url = f'{BASE_URI}/{user_id}'
        payload = dumps({
            'fname': first_name,
            'lname': last_name
        })
        return self.request.put(url, payload, self.headers)
