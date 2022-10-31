import json
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
        await create_reservation_pc(774508651)
        # await create_reservation_pc_test()
    else:
        print("Ошибка подключения к гизмо ТЦБ: ", response.status_code)


async def connect_to_dema():
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/usersessions/activeinfo")
    if response.status_code == 200:
        print("Подключение к гизмо Дема успешно")
    else:
        print("Ошибка подключения к гизмо Дема: ", response.status_code)


async def create_reservation_pc(chat_id):

    reservation_create_blank = await parsing_text.parsing_reservations_for_pc("2022-10-31T17:00:00", "89170412666",
                                                                              "hey", 120, [8])
    response = requests.get("http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/v2.0/reservations")
    # response = requests.post("http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/v2.0/reservations", json=reservation_create_blank)


async def create_reservation_pc_test(chat_id : int):
    check_id = ""
    reservation_create_blank = await parsing_text.parsing_reservations_for_pc("2022-10-31T17:00:00", "89170412666",
                                                                              "hey", 120, [8])
    response = requests.post("http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/v2.0/reservations",
                             json=reservation_create_blank)
    if response.text.find('"httpStatusCode":200') >= 0:
        check_id = response.text[response.text.find('id') + 4:]
        check_id = check_id[:check_id.find('}')]
        response = requests.delete(
            "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/v2.0/reservations/" + check_id)
        print("Не занято")
    elif response.text.find('"httpStatusCode":400') >= 0:
        print("занято")
