import sqlite3
import os


def init_db():
    path = os.getcwd()
    if not os.path.isfile('main.db'):
        with open(os.path.join(path, 'main.db'), 'w+') as file:
            pass


def increment_timer(new_time):

    conn = sqlite3.connect('main.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS timer (
                total_time INTEGER)''')
    cur.execute('''UPDATE timer SET total_time = (?)''',
                (new_time,))
    conn.commit()

    cur.close()
    conn.close()
