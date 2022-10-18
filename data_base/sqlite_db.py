import sqlite3 as sq


def sql_start():
    global base, cur
    base = sq.connect('cyber_room_ufa.db')
    cur = base.cursor()
    if base:
        print('База данных подключена')
    base.execute('CREATE TABLE IF NOT EXISTS clients(id INT PRIMARY KEY, name TEXT, number TEXT, points INT)')
    base.commit()


async def sql_get_info(id: int):
    search_text = "SELECT * FROM clients WHERE id LIKE '%" + str(id) + "%'"
    cur.execute(search_text)
    records = cur.fetchall()
    if len(records) == 0:
        return None
    else:
        return records[0][3]


async def sql_add_client(id: int, name: str, number: str):
    # "INSERT INTO clients (id, name, number, points) VALUES(" + str(id) + "," + name + "," + number + ",0)"
    try:
        cur.execute("INSERT INTO clients (id, name, number, points) VALUES(?,?,?,0)", (id, name, number))
        base.commit()
        print(str(id) + " зарегистрировался")
        return 1
    except:
        print(str(id) + " ошибка, не смог зарегестрироваться")
        return 0
