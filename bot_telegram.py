# -*- coding:utf -8 -*-
from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db
from work_with_users import send_spam


async def on_startup(_):
    print('Бот вкл')
    sqlite_db.sql_start()
    await send_spam.first_check_after_begin_work_bot()


client.register_handlers_client(dp)
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
