import requests

TOKEN = '6089863461:AAGuL8gKw5QdjXaqwcNY6dZmQmezYVgtDUg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'


response = requests.get(url=BASE_URL)
if response.status_code == 200:
    info = response.json()
    print(info)