import random
from gizmo import parsing_text
import requests
import os
import re

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
ip = os.getenv("IP")
port = os.getenv("PORT")


async def connect_to_ufa():
    response = requests.get("http://" + login + ":" + password + "@" + ip + ":" + port + "/api/usersessions/activeinfo")
    if response.status_code == 200:

        print("Подключение к гизмо ТЦБ успешно\n")
        response = requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api/hostcomputers")
        # test
        """
        new_text = response.text[response.text.find('[') + 2:len(response.text)]
        new_text = new_text.replace('[', '')
        new_text = new_text.replace('{', '')
        new_text = new_text.replace('}', '')
        new_text = new_text.replace(']', '')
        new_text = new_text.replace('"','')
        new_array = new_text.split(',')
        i = 0
        for g in range(len(new_array)):
            new_array[g] = new_array[g].split(':')
        while i < len(response.text):
            new_i = response.text.find('name', i, len(response.text))
            if new_i == -1:
                break
            new_i = response.text.find(':', new_i, len(response.text)) + 2
            split_text = response.text.find(',', new_i, len(response.text)) - 1
            current_pc = response.text[new_i:split_text]
            i = new_i
        for g in new_array:
            print(g)
        # test
        """
        # response_activeinfo = requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api/usersessions/activeinfo")
        # response_active = requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api/usersessions/active")
        # status_pc_array = await parsing_text.parsing_user_sessions_active_info(response_activeinfo.text, response_active.text)
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
        response_activeinfo = requests.get(
            "http://" + login + ":" + password + "@127.0.0.1:80/api/usersessions/activeinfo")
        response_active = requests.get("http://" + login + ":" + password + "@127.0.0.1:80/api/usersessions/active")
        status_pc_array = await parsing_text.parsing_user_sessions_active_info(response_activeinfo.text,
                                                                               response_active.text)
        return status_pc_array
    else:
        print()  # dema
