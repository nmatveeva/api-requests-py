from jsonpath_ng import parse


def search_nodes_using_json_path(users, json_path):
    jsonpath = parse(json_path)
    return [match.value for match in jsonpath.find(users)]


def search_user_created_in(users, last_name):
    return [user for user in users if user['lname'] == last_name][0]
