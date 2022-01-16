import requests

# BASE_URL = 'http://localhost:8000/withoutrest/'
BASE_URL = 'https://api.coinmarketcap.com/v1/ticker'
# END_POINT = 'json_empapi/'
resp = requests.get(BASE_URL)
# print("Type of response is " + str(type(resp.json())))
# data = resp.json()
print(resp)

