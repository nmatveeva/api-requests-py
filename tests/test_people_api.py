import requests
from assertpy import soft_assertions

from api_clinet.people_api_client import PeopleApiClient
from tests.assertions.people_api_asserts import *
from tests.helpers.people_api_helpers import *

client = PeopleApiClient()


def test_user_created_with_a_json_template(create_data):
    """
    Test the People API can be used to create a new user via JSON file
    """
    _, response = client.create_user(create_data)
    assert_that(response.status_code, description='User not created').is_equal_to(requests.codes.no_content)

    response = client.read_all_users()
    users = response.as_dict

    result = search_nodes_using_json_path(users, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)


def test_user_created():
    """
    Test the People API can be used to create a new user
    """
    last_name, response = client.create_user()
    assert_that(response.status_code, description='User not created').is_equal_to(requests.codes.no_content)

    users = client.read_all_users().as_dict
    is_new_user_created = search_user_created_in(users, last_name)
    assert_user_is_present(is_new_user_created)


def test_user_deleted():
    """
    Test the People API can be used to delete a user
    """
    last_name, _ = client.create_user()

    users = client.read_all_users().as_dict
    user_id = search_user_created_in(users, last_name)['person_id']

    response = client.delete_user(user_id)
    assert_that(response.status_code, description="User not deleted").is_equal_to(requests.codes.ok)

    deleted_user = client.read_user_by_id(user_id)
    assert_that(deleted_user.status_code, description='User found').is_equal_to(requests.codes.not_found)


def test_user_updated():
    """
    Test the People API can be used to update a user
    """
    last_name, _ = client.create_user()
    users = client.read_all_users().as_dict
    user_id = search_user_created_in(users, last_name)['person_id']

    new_first_name = f'First{generate_unique_name()}'
    new_last_name = f'Last{generate_unique_name()}'
    response = client.update_user(user_id, new_first_name, new_last_name)
    assert_that(response.status_code, description='User not updated').is_equal_to(requests.codes.ok)

    updated_user = client.read_user_by_id(user_id)

    with soft_assertions():
        assert_that(updated_user.as_dict['fname'], description='First Name not updated').is_equal_to(new_first_name)
        assert_that(updated_user.as_dict['lname'], description='Last Name not updated').is_equal_to(new_last_name)
