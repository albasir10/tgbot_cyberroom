from data_base import sqlite_db
from generate_text import generate_qr_code
from create_bot import bot


# рассылка

async def writing_clients(password: str):
    clients_for_mail = await sqlite_db.sql_get_all_users()
    qr_code_bytes = await generate_qr_code.create_qr_code(password)
    try:
        text_for_clients = "📪 Привет! Хотите получить 1 час бесплатно? Берите QR код!\nПодойдите к стойке " \
                           "администрации для активации. Код активируется, лишь, для первого показавшего. "
        for i in clients_for_mail:
            await bot.send_photo(i[0], photo=qr_code_bytes, caption=text_for_clients)
    except:
        print("error ", writing_clients)
