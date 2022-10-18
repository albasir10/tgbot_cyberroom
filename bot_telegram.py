import asyncio
# -*- coding:utf -8 -*-
from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db
from datetime import datetime
import random


async def on_startup(_):
    print('Бот вкл')
    sqlite_db.sql_start()
    current_datetime = datetime.now()
    last_time = str(current_datetime.year) + "." + str(current_datetime.month) + "." + str(current_datetime.day)
    res = await sqlite_db.sql_get_all_users()
    print(res)
    """
    try:
        time_save_file = open("time/lastTime.txt", "x")
        time_save_file.writelines([last_time + "\n", str(current_datetime.weekday())])
        time_save_file.close()
        await update_time()
    except:
        await check_time_for_mailing_list()
    """

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
    f = last_time_text.find('.')
    year_last_time = last_time_text[0:last_time_text.find('.'):1]
    year_current_time = current_time_text[0:current_time_text.find('.'):1]
    if int(year_current_time) == int(year_last_time):
        month_last_time = last_time_text[
                          last_time_text.find('.') + 1:last_time_text.find('.', last_time_text.find('.') + 1):1]
        month_current_time = current_time_text[current_time_text.find('.') + 1:current_time_text.find('.',
                                                                                                      current_time_text.find(
                                                                                                          '.') + 1):1]
        if int(month_last_time) == int(month_current_time):
            day_last_time = last_time_text[last_time_text.rfind('.') + 1:len(last_time_text):1]
            day_current_time = current_time_text[current_time_text.rfind('.') + 1:len(current_time_text):1]
            if int(day_current_time) == int(day_last_time):
                await asyncio.sleep(86400)
                return await check_time_for_mailing_list()
            elif abs(int(day_current_time) - int(day_last_time) >= 7):
                await update_time()
            else:
                await asyncio.sleep(86400)
                return await check_time_for_mailing_list()
        elif int(month_last_time) - int(month_current_time) == 1 and int(last_weekday) == int(
                current_datetime.weekday()):
            await update_time()
        elif int(month_last_time) - int(month_current_time) == 1:
            await asyncio.sleep(86400)
            return await check_time_for_mailing_list()
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
    generate_code_file = open("generateText/code.txt", "w")
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = random.randint(4, 6)
    password = ""
    for i in range(length):
        password += random.choice(chars)
    print("НОВЫЙ КОД: ", password)
    #await client.writing_clients(password)


client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
