import random

import requests
import os

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')


async def connect_to_ufa():
    response = requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api/stats/session")
    if response.status_code == 200:
        print("Подключение к гизмо ТЦБ успешно")
    else:
        print("Ошибка подключения к гизмо ТЦБ: ", response.status_code)


async def connect_to_dema():
    response = requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api/stats/session")
    if response.status_code == 200:
        print("Подключение к гизмо Дема успешно")
    else:
        print("Ошибка подключения к гизмо Дема: ", response.status_code)


async def get_all_status_pc(club_name: str):
    if club_name == "ufa":
        status_pc_array = []
        for current_pc in range(25):
            status_pc_array.append(random.randint(0, 2))
        return status_pc_array
    else:
        print()  # dema
