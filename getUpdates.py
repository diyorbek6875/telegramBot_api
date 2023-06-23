import requests
from pprint import pprint

TOKEN = '6089863461:AAGuL8gKw5QdjXaqwcNY6dZmQmezYVgtDUg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'


response = requests.get(url=BASE_URL)
updates=response.json()['result']
pprint(response.json())
# print each update
