from uuid import uuid4

import requests
from assertpy import assert_that
from jsonpath_ng import parse
from json import loads, dumps

from config import BASE_URI


def test_person_can_be_added_with_a_json_template(create_data):
    create_person_with_unique_lastname(create_data)

    response = requests.get(BASE_URI)
    peoples = loads(response.text)

    # Get all last names for any object in the root array
    # Here $ = root, [*] represents any element in the array
    # Read full syntax: https://pypi.org/project/jsonpath-ng/
    jsonpath_expr = parse("$.[*].lname")
    result = [match.value for match in jsonpath_expr.find(peoples)]
    print(result)

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)


def create_person_with_unique_lastname(body=None):
    if body is None:
        # Ensure a user with a unique last name is created everytime the test runs
        # Note: json.dumps() is used to convert python dict to json string
        unique_last_name = f'User {str(uuid4())}'
        payload = dumps({
            'fname': 'New',
            'lname': unique_last_name
        })
    else:
        unique_last_name = body['lname']
        payload = dumps(body)

    # Setting default headers to show that the client accepts json
    # And will send json in the headers
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # We use requests.post method with keyword params to make the request more readable
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)
    return unique_last_name
