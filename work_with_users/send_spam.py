import asyncio
import threading
import time
from datetime import datetime
import random
from handlers import client
from threading import Thread
from handlers.general_commands import mailing_commands


async def first_check_after_begin_work_bot():
    current_datetime = datetime.now()
    last_time = str(current_datetime.year) + "." + str(current_datetime.month) + "." + str(current_datetime.day)
    try:
        time_save_file = open("time/lastTime.txt", "x")
        time_save_file.writelines([last_time + "\n", str(current_datetime.weekday())])
        time_save_file.close()
        await update_time()
        await check_time_for_mailing_list()
    except:
        await check_time_for_mailing_list()
        print()


async def check_time_for_mailing_list():
    current_datetime = datetime.now()
    last_time_text = ""
    last_weekday = ""
    current_time_text = str(current_datetime.year) + "." + str(current_datetime.month) + "." + str(current_datetime.day)
    try:
        time_save_file = open("time/lastTime.txt", "r")
        last_time_text = str(time_save_file.readline())
        last_weekday = str(time_save_file.readline())
        time_save_file.close()
    except:
        print('error open file check_time_for_mailing_list')
    point1 = last_time_text.find('.')
    pointr1 = last_time_text.rfind('.')
    point2 = current_time_text.find('.')
    pointr2 = current_time_text.rfind('.')
    year_last_time = last_time_text[0:point1:1]
    year_current_time = current_time_text[0:point2:1]
    if int(year_current_time) == int(year_last_time):
        month_last_time = last_time_text[point1 + 1:last_time_text.find('.', point1 + 1):1]
        month_current_time = current_time_text[point2 + 1:current_time_text.find('.', point2 + 1):1]
        if int(month_last_time) == int(month_current_time):
            day_last_time = last_time_text[pointr1 + 1:len(last_time_text):1]
            day_current_time = current_time_text[pointr2 + 1:len(current_time_text):1]
            if int(day_current_time) == int(day_last_time):
                pass
            elif abs(int(day_current_time) - int(day_last_time) >= 7):
                await update_time()
            else:
                pass
        elif int(month_last_time) - int(month_current_time) == 1 and int(last_weekday) == int(
                current_datetime.weekday()):
            await update_time()
        elif int(month_last_time) - int(month_current_time) == 1:
            pass
        else:
            await update_time()
    else:
        await update_time()


async def update_time():
    current_datetime = datetime.now()
    last_time = str(current_datetime.year) + "." + str(current_datetime.month) + "." + str(current_datetime.day)
    time_save_file = open("time/lastTime.txt", "w")
    time_save_file.writelines([last_time + "\n", str(current_datetime.weekday())])
    time_save_file.close()
    generate_code_file = open("generate_text/code.txt", "w")
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = random.randint(8, 10)
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("НОВЫЙ ПРОМОКОД: ", password)
    generate_code_file.writelines(password)
    generate_code_file.close()
    await mailing_commands.writing_clients(password)
