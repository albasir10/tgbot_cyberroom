import datetime
import json
import requests

"""          parsing_user_sessions_active_info      ПОКА НЕ РАБОТАЕТ   """


async def parsing_user_sessions_active_info(login: str, password: str, ip_ufa: str, port: str):
    response = requests.get(
        "http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/hostcomputers")
    # test
    new_text = response.text[response.text.find('[') + 2:len(response.text)]
    new_text = new_text.replace('[', '')
    new_text = new_text.replace('{', '')
    new_text = new_text.replace('}', '')
    new_text = new_text.replace(']', '')
    new_text = new_text.replace('"', '')
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
    i = 0
    new_array_2 = []
    new_array.pop(len(new_array) - 1)
    new_array.pop(len(new_array) - 2)
    new_array.pop(len(new_array) - 3)
    new_array.pop(len(new_array) - 4)
    while 13 * (i + 1) <= len(new_array):
        new_array_2.append([new_array[g + 13 * i] for g in range(13)])
        i += 1
    response_test = None
    for g in new_array_2:
        if g[7][1] == 'false':
            print(g)
    """
    for g in new_array_2:
        if g[7][1] == 'false':
            print(g, "\n")
    print("\n\n\n")
    """
    status_pc_str = 0
    # test
    return status_pc_str


async def parsing_reservations_for_pc(date: str, contact_phone: str, note: str, duration: int, hosts: list):
    with open("generate_text/reservation_create.json") as f:
        reservation_create_blank = json.load(f)
    pin = "dsdado"
    reservation_create_blank['date'] = "tt"
    reservation_create_blank['duration'] = duration
    reservation_create_blank['contactPhone'] = contact_phone
    reservation_create_blank['contactEmail'] = ""
    reservation_create_blank['note'] = note
    reservation_create_blank['pin'] = pin
    reservation_create_blank['status'] = 0
    reservation_create_blank['hosts'] = []
    for i in range(len(hosts)):
        reservation_create_blank['hosts'].append({'hostId': hosts[i]})
    print()


date_text = str(datetime.datetime.now())
date_text = date_text.replace(' ', 'T')
date_text += "Z"
print(date_text)
