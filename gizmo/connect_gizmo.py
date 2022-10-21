import random
from gizmo import parsing_text
import requests
import os
import re

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
ip_ufa = os.getenv("IPUFA")
port = os.getenv("PORT")
ip_dema = os.getenv("IPDEMA")


async def connect_to_ufa():
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/usersessions/activeinfo")
    if response.status_code == 200:
        print("Подключение к гизмо ТЦБ успешно\n")
        await parsing_text.parsing_user_sessions_active_info(login, password, ip_ufa, port)
        # response_activeinfo = requests.get("http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/usersessions/activeinfo")
        # response_active = requests.get("http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/usersessions/active")
        # status_pc_array = await parsing_text.parsing_user_sessions_active_info(response_activeinfo.text, response_active.text)
        # print(status_pc_array)
    else:
        print("Ошибка подключения к гизмо ТЦБ: ", response.status_code)


async def connect_to_dema():
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/usersessions/activeinfo")
    if response.status_code == 200:
        print("Подключение к гизмо Дема успешно")
    else:
        print("Ошибка подключения к гизмо Дема: ", response.status_code)


async def get_all_status_pc(club_name: str):
    if club_name == "ufa":
        response_activeinfo = requests.get(
            "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/usersessions/activeinfo")
        response_active = requests.get(
            "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/usersessions/active")
        status_pc_array = await parsing_text.parsing_user_sessions_active_info(response_activeinfo.text,
                                                                               response_active.text)
        return status_pc_array
    else:
        print()  # dema
