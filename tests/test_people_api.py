import requests

from api_clinet.people_api_client import PeopleApiClient
from tests.assertions.people_api_asserts import *
from tests.helpers.people_api_helpers import *

client = PeopleApiClient()


def test_user_created_with_a_json_template(create_data):
    client.create_user(create_data)

    response = client.read_all_users()
    users = response.as_dict

    result = search_nodes_using_json_path(users, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)


def test_user_created():
    last_name, response = client.create_user()
    assert_that(response.status_code, description='User not created').is_equal_to(requests.codes.no_content)

    users = client.read_all_users().as_dict
    is_new_user_created = search_user_created_in(users, last_name)
    assert_user_is_present(is_new_user_created)
