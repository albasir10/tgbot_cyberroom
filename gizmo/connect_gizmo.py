import requests
import os

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


async def connect_to_ufa():
    print(requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api"))


async def connect_to_dema():
    print(requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api"))
