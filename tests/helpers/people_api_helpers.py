from uuid import uuid4
from pprint import pprint
from jsonpath_ng import parse


def search_nodes_using_json_path(users, json_path):
    jsonpath = parse(json_path)
    return [match.value for match in jsonpath.find(users)]


def search_user_created_in(users, last_name):
    return [user for user in users if user['lname'] == last_name][0]


def generate_unique_name() -> str:
    return f'Name{str(uuid4())}'


def pretty_print(msg, indent=2):
    print()
    pprint(msg, indent=indent)
