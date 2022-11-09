import json
import random
from gizmo import parsing_text
import requests
import os
from create_bot import bot, dp

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
ip_ufa = os.getenv("IPUFA")
port = os.getenv("PORT")
ip_dema = os.getenv("IPDEMA")
chat_id_work_number = os.getenv("CHATIDWORKNUMBER")


async def connect_to_ufa():
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/usersessions/activeinfo")
    if response.status_code == 200:
        print("Подключение к гизмо ТЦБ успешно\n")
    else:
        print("Ошибка подключения к гизмо ТЦБ: ", response.status_code)


async def connect_to_dema():
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/usersessions/activeinfo")
    if response.status_code == 200:
        print("Подключение к гизмо Дема успешно")
    else:
        print("Ошибка подключения к гизмо Дема: ", response.status_code)


async def create_reservation_pc(chat_id: int):
    with open("clients_data/create_reservation_data/" + str(chat_id) + ".txt", 'r') as f:
        number_pc = f.readline()
    reservation_create_blank = await parsing_text.parsing_reservations_for_pc(chat_id)
    response = requests.post("http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/v2.0/reservations",
                             json=reservation_create_blank)
    if response.text.find('"httpStatusCode":200') >= 0:
        await bot.send_message(chat_id_work_number, "Клиент: \nНомер:" + str(reservation_create_blank['contactPhone']) +
                               "\nЗабронил " + number_pc[number_pc.find('=')+1:] + " пк \nВ " + reservation_create_blank['date'] +
                               "\nНа " + str(reservation_create_blank['duration'] / 60) + " часов")
        return True
    elif response.text.find('"httpStatusCode":400') >= 0:
        return False


async def create_reservation_pc_test(chat_id: int, date_pc: str):
    check_id = ""
    reservation_create_blank = await parsing_text.parsing_reservations_for_pc_test(chat_id, date_pc)
    if reservation_create_blank is None:
        return False
    response = requests.post("http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/v2.0/reservations",
                             json=reservation_create_blank)

    if response.text.find('"httpStatusCode":200') >= 0:
        check_id = response.text[response.text.find('id') + 4:]
        check_id = check_id[:check_id.find('}')]
        requests.delete(
            "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/v2.0/reservations/" + check_id)
        return True
    elif response.text.find('"httpStatusCode":400') >= 0:
        return False
