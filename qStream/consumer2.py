import requests

BASE_URL = 'http://localhost:8000/withoutrestm/'
END_POINT = 'empapi/'


def get_resource():
    resp = requests.get(BASE_URL + END_POINT)
    print('Status code ' + str(resp.status_code))
    print(resp.json())


get_resource()
