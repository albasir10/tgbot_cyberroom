import sqlite3 as sq

base = sq.connect('cyber_room_ufa.db')


def sql_start():
    global base
    base = sq.connect('cyber_room_ufa.db')
    cur = base.cursor()
    if base:
        print('База данных подключена')
    base.execute('CREATE TABLE IF NOT EXISTS clients(id INT PRIMARY KEY, name TEXT)')
    base.commit()


async def sql_get_info(id: int):
    global base
    search_text = "SELECT * FROM clients WHERE id LIKE '%" + str(id) + "%'"
    cur = base.cursor()
    cur.execute(search_text)
    records = cur.fetchall()
    if len(records) == 0:
        return None
    else:
        return 1


async def sql_get_all_users():
    global base
    search_text = "SELECT * FROM clients"
    cur = base.cursor()
    cur.execute(search_text)
    records = cur.fetchall()
    if len(records) == 0:
        return None
    else:
        return records


async def sql_add_client(id: int, name: str):
    try:
        global base
        cur = base.cursor()
        cur.execute("INSERT INTO clients (id, name) VALUES(?,?)", (id, name))
        base.commit()
        print(str(id) + " зарегистрировался")
        return 1
    except:
        print(str(id) + " ошибка, не смог зарегестрироваться")
        return 0
