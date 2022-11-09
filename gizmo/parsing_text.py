import datetime
import json
import requests
import os
import random

"""          parsing_user_sessions_active_info      ПОКА НЕ РАБОТАЕТ   """
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
ip_ufa = os.getenv("IPUFA")
port = os.getenv("PORT")
ip_dema = os.getenv("IPDEMA")


async def parsing_reservations_for_pc(chat_id: int):
    with open("clients_data/create_reservation_data/" + str(chat_id) + ".txt", 'r') as f:
        number_pc = f.readline()
        date_pc = f.readline()
        contact_phone = f.readline()
        note = f.readline()
        duration = f.readline()
    number_pc = number_pc[number_pc.find('=') + 1:number_pc.find('\n')]
    number_pc_int = int(number_pc)

    with open("generate_text/hostid_change_to_realid.json") as f:
        host_id_change_file = json.load(f)
    host_id = int(host_id_change_file["PC" + str(number_pc_int)])
    date_pc = date_pc[date_pc.find("=") + 1: date_pc.find('\n')]
    if len(date_pc[date_pc.rfind(' ') + 1:]) == 1:
        date_pc = date_pc[:date_pc.rfind(' ') + 1] + "0" + date_pc[date_pc.rfind(' ') + 1:]
    new_date_pc = ""
    new_date_pc += date_pc[date_pc.rfind('.') + 1:date_pc.rfind(' ')] + "-"
    new_date_pc += date_pc[date_pc.find('.') + 1:date_pc.rfind('.')] + "-"
    new_date_pc += date_pc[:date_pc.find('.')] + 'T'
    new_date_pc += date_pc[date_pc.rfind(' ') + 1:] + ":00:00.00Z"
    contact_phone = contact_phone[contact_phone.find("=") + 1: contact_phone.find('\n')]
    note = note[note.find("=") + 1: note.find('\n')]
    duration = int(duration[duration.find("=") + 1: duration.find('\n')]) * 60
    with open("generate_text/reservation_create.json") as f:
        reservation_create_blank = json.load(f)
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/users/" + "89170412666" + "/username")
    if response.text.find('"httpStatusCode":200') >= 0:
        user_id = response.text[response.text.find('"id"') + 5:]
        user_id = user_id[:user_id.find('}')]
    else:
        return None
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 6
    pin = ""
    for i in range(length):
        pin += random.choice(chars)
    try:
        reservation_create_blank["userId"] = int(user_id)
    except:
        return None
    reservation_create_blank["date"] = new_date_pc
    reservation_create_blank["duration"] = duration
    reservation_create_blank["contactPhone"] = contact_phone
    reservation_create_blank["contactEmail"] = "dddd@mail.ru"
    reservation_create_blank["note"] = note
    reservation_create_blank["pin"] = pin
    reservation_create_blank["users"] = []
    reservation_create_blank["status"] = 0
    reservation_create_blank["hosts"] = [dict(hostId=host_id)]
    return reservation_create_blank


async def parsing_reservations_for_pc_test(chat_id: int, date_pc: str):
    with open("clients_data/create_reservation_data/" + str(chat_id) + ".txt", 'r') as f:
        number_pc = f.readline()
    if len(date_pc[date_pc.rfind(' ') + 1:]) == 1:
        date_pc = date_pc[:date_pc.rfind(' ') + 1] + "0" + date_pc[date_pc.rfind(' ') + 1:]
    with open("generate_text/hostid_change_to_realid.json") as f:
        host_id_change_file = json.load(f)
    number_pc = number_pc[number_pc.find('=') + 1:]
    number_pc_int = int(number_pc)
    host_id = int(host_id_change_file["PC" + str(number_pc_int)])
    new_date_pc = ""
    new_date_pc += date_pc[date_pc.rfind('.') + 1:date_pc.rfind(' ')] + "-"
    new_date_pc += date_pc[date_pc.find('.') + 1:date_pc.rfind('.')] + "-"
    new_date_pc += date_pc[:date_pc.find('.')] + 'T'
    new_date_pc += date_pc[date_pc.rfind(' ') + 1:] + ":00:00.00Z"
    contact_phone = "89170412666"
    note = "hey"
    duration = 60
    with open("generate_text/reservation_create.json") as f:
        reservation_create_blank = json.load(f)
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/users/" + contact_phone + "/username")
    if response.text.find('"httpStatusCode":200') >= 0:
        user_id = response.text[response.text.find('"id"') + 5:]
        user_id = user_id[:user_id.find('}')]
    else:
        user_id = None
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = 6
    pin = ""
    for i in range(length):
        pin += random.choice(chars)
    reservation_create_blank["userId"] = int(user_id)
    reservation_create_blank["date"] = new_date_pc
    reservation_create_blank["duration"] = duration
    reservation_create_blank["contactPhone"] = contact_phone
    reservation_create_blank["contactEmail"] = "dddd@mail.ru"
    reservation_create_blank["note"] = note
    reservation_create_blank["pin"] = pin
    reservation_create_blank["users"] = []
    reservation_create_blank["status"] = 0
    reservation_create_blank["hosts"] = [dict(hostId=host_id)]
    return reservation_create_blank
