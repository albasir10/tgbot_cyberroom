# -*- coding:utf -8 -*-
import asyncio
from aiogram.utils import executor
from create_bot import dp
from handlers import client
from data_base import sqlite_db
from work_with_users import send_spam
from gizmo import connect_gizmo
import aioschedule


async def scheduler():
    aioschedule.every().monday.at("12:00").do(send_spam.check_time_for_mailing_list)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    print('Бот вкл')
    asyncio.create_task(scheduler())
    sqlite_db.sql_start()
    await connect_gizmo.connect_to_dema()
    await connect_gizmo.connect_to_ufa()
    await send_spam.first_check_after_begin_work_bot()


client.register_handlers_client(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
