import datetime
import json

"""          parsing_user_sessions_active_info      ПОКА НЕ РАБОТАЕТ   """


async def parsing_user_sessions_active_info(text_for_number_pc: str, text_for_time: str):
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
    k = 0
    for j in range(len(states_pc)):
        if states_pc[j][0] == 0:
            continue
        new_i = text_for_time.find('endTime', k, len(text_for_number_pc))
        if new_i == -1:
            break
        new_i = text_for_time.find('"', new_i, len(text_for_number_pc)) + 2
        split_text = text_for_time.find(',', new_i, len(text_for_number_pc))
        new_text = text_for_time[new_i:split_text]
        end_time_year = int(new_text[0:new_text.find("-")])
        end_time_month = int(new_text[new_text.find("-") + 1: new_text.find("-", new_text.find("-") + 1)])
        end_time_day = int(new_text[new_text.find("-", new_text.find("-") + 1) + 1:new_text.find("T")])
        end_time_hours = int(new_text[new_text.find("T") + 1:new_text.find(":")])
        end_time_minutes = int(new_text[new_text.find(":") + 1:new_text.find(":", new_text.find(":") + 1)])
        # end_time_seconds = new_text[new_text.find(":", new_text.find(":")+1):new_text.find(".")]

        current_span = float(new_text)
        states_pc[j][1] = current_span
        k = new_i
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



