import os
import requests

TOKEN = '6089863461:AAGuL8gKw5QdjXaqwcNY6dZmQmezYVgtDUg'

def sendMessage(chat_id:str, text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    params={
        'chat_id':chat_id,
        'text':text
    }
    r=requests.get(url=URL,params=params)
    
    return r.json()

print(sendMessage(chat_id='1937466761',text='salom'))
sendMessage(chat_id='1937466761',text='salom')
