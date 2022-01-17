# this is utils
import json


def is_valid_data(data):
    try:
        # print('this is try block of is_valid_data()')
        json.loads(data)
        valid = True
    except ValueError:
        # print('this is catch block of is_valid_data()')
        valid = False
    return valid
