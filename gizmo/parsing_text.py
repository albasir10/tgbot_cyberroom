import datetime
import json
import requests
"""          parsing_user_sessions_active_info      ПОКА НЕ РАБОТАЕТ   """


async def parsing_user_sessions_active_info(login : str, password : str, ip_ufa : str, port :str):
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
    response_test = requests.get("http://google.com")
    for g in new_array_2:
        if g[7][1] == 'false':
            response_test = requests.get("http://" + login + ":" + password + "@" + ip_ufa + ":" + port + "/api/hostcomputers/"+g[1][2])
            break
    print(response_test.text)
    """
    for g in new_array_2:
        if g[7][1] == 'false':
            print(g, "\n")
    print("\n\n\n")
    """
    status_pc_str = 0
    # test
    """
    counts_pc = 0
    with open("global_info/info_ufa.txt", "r") as f:
        counts_pc = int(f.readline())
    states_pc = []
    for i in range(counts_pc):
        states_pc.append([])
        for j in range(2):
            states_pc[i].append(0)
    new_text = ""
    i = 0

    while i < len(text_for_number_pc):
        new_i = text_for_number_pc.find('hostNumber', i, len(text_for_number_pc))
        if new_i == -1:
            break
        new_i = text_for_number_pc.find('"', new_i, len(text_for_number_pc)) + 2
        split_text = text_for_number_pc.find(',', new_i, len(text_for_number_pc))
        current_pc = int(text_for_number_pc[new_i:split_text])
        if current_pc < 21:
            states_pc[current_pc - 1][0] = current_pc
        elif 20 < current_pc < 26:
            states_pc[current_pc - 6][0] = current_pc
        elif current_pc < 51:
            states_pc[current_pc - 26][0] = current_pc
        else:
            # плойка
            states_pc[len(states_pc) - 1][0] = current_pc
        i = new_i
    i = 0
    status_pc_str = ""  # удалить после проверок

    status_pc_str = "Текущий статус компьютеров и ps:\n\n⚫ - недоступен\n🔴 - занят\n🟢 - свободен\n\n"
    for i in range(25):  # пока не работает ⚫
        if i < 10:
            if states_pc[i][1] == -1:
                status_pc_str += "⚫   Premium " + str(i + 1) + "\n\n"
            elif states_pc[i][1] > 0:
                time_minutes = int(states_pc[i][1] / 60)
                time_hours = int(time_minutes / 24)
                status_pc_str += "🔴   Premium " + str(i + 1) + "  время:  " + str(time_hours) + " ч " + str(
                    time_minutes) + " м" + "\n\n"
            elif states_pc[i][1] == 0:
                status_pc_str += "🟢   Premium " + str(i + 1) + "\n\n"
        elif i < 15:
            if states_pc[i][1] == -1:
                status_pc_str += "⚫   BootCamp " + str(i + 1) + "\n\n"
            elif states_pc[i][1] > 0:
                time_minutes = int(states_pc[i][1] / 60)
                time_hours = int(time_minutes / 24)
                status_pc_str += "🔴   BootCamp " + str(i + 1) + "  время:  " + str(time_hours) + " ч " + str(
                    time_minutes) + " м" + "\n\n"
            elif states_pc[i][1] == 0:
                status_pc_str += "🟢   BootCamp " + str(i + 1) + "\n\n"
        elif i < 20:
            if states_pc[i][1] == -1:
                status_pc_str += "⚫   BootCamp " + str(i + 6) + "\n\n"
            elif states_pc[i][1] > 0:
                time_minutes = int(states_pc[i][1] / 60)
                time_hours = int(time_minutes / 24)
                status_pc_str += "🔴   BootCamp " + str(i + 6) + "  время:  " + str(
                    time_hours) + " ч " + str(time_minutes) + " м" + "\n\n"
            elif states_pc[i][1] == 0:
                status_pc_str += "🟢   BootCamp " + str(i + 6) + "\n\n"
        elif i < 23:
            if states_pc[i][1] == -1:
                status_pc_str += "⚫   Luxe " + str(i + 26) + "\n\n"
            elif states_pc[i][1] > 0:
                time_minutes = int(states_pc[i][1] / 60)
                time_hours = int(time_minutes / 24)
                status_pc_str += "🔴   Luxe " + str(i + 26) + "  время:  " + str(
                    time_hours) + " ч " + str(time_minutes) + " м" + "\n\n"
            elif states_pc[i][1] == 0:
                status_pc_str += "🟢   Luxe " + str(i + 26) + "\n\n"
        elif i < 24:
            if states_pc[i][1] == -1:
                status_pc_str += "⚫   Luxe 50\n\n"
            elif states_pc[i][1] > 0:
                time_minutes = int(states_pc[i][1] / 60)
                time_hours = int(time_minutes / 24)
                status_pc_str += "🔴   Luxe 50" + "  время:  " + str(
                    time_hours) + " ч " + str(time_minutes) + " м" + "\n\n"
            elif states_pc[i][1] == 0:
                status_pc_str += "🟢   Luxe 50\n\n"
        else:
            if states_pc[i][1] == -1:
                status_pc_str += "⚫   PS4\n\n"
            elif states_pc[i][1] > 0:
                time_minutes = int(states_pc[i][1] / 60)
                time_hours = int(time_minutes / 24)
                status_pc_str += "🔴   PS4  время:  " + str(time_hours) + " ч " + str(time_minutes) + " м" + "\n\n"
            elif states_pc[i][1] == 0:
                status_pc_str += "🟢   PS4\n\n"
    status_pc_str += "\nТекущий статус компьютеров и ps:\n⚫ - недоступен\n🔴 - занят\n🟢 - свободен"
    """
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



