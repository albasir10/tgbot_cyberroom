import datetime
import json
import requests
import os

"""          parsing_user_sessions_active_info      ПОКА НЕ РАБОТАЕТ   """
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
ip_ufa = os.getenv("IPUFA")
port = os.getenv("PORT")
ip_dema = os.getenv("IPDEMA")


async def parsing_reservations_for_pc(date: str, contact_phone: str, note: str, duration: int, hosts: list):
    with open("generate_text/reservation_create.json") as f:
        reservation_create_blank = json.load(f)
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_dema + ":" + port + "/api/users/" + contact_phone + "/username")
    user_id = response.text[response.text.find('"id"') + 5:]
    user_id = user_id[:user_id.find('}')]
    pin = "dsdado"
    reservation_create_blank["userId"] = int(user_id)
    reservation_create_blank["date"] = date
    reservation_create_blank["duration"] = duration
    reservation_create_blank["contactPhone"] = contact_phone
    reservation_create_blank["contactEmail"] = "dddd@mail.ru"
    reservation_create_blank["note"] = note
    reservation_create_blank["pin"] = pin
    reservation_create_blank["users"] = []
    reservation_create_blank["status"] = 0
    reservation_create_blank["hosts"] = [dict(hostId=hosts[0])]
    return reservation_create_blank
