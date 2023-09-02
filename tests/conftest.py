from json import dumps
from uuid import uuid4

import pytest
import requests
from assertpy import assert_that

from config import BASE_URI
from utils.file_reader import read_json_file
import random


@pytest.fixture
def create_data():
    payload = read_json_file('create_person.json')

    random_no = random.randint(0, 1000)
    last_name = f'LastName{random_no}'

    payload['lname'] = last_name
    yield payload
