import sqlite3

def start_timer():
    conn = sqlite3.connect('main.db')
    cur = conn.cursor()
    cmd = cur.execute('''CREATE TABLE IF NOT EXISTS timer (
                total_time INTEGER)''')
    qry = cur.execute('''SELECT total_time FROM timer''')

    rslts = qry.fetchone()
    if not rslts:
        cur.execute('''INSERT INTO timer (total_time) VALUES (1)''')
        conn.commit()
    cur.close()
    conn.close()

    return rslts


def increment_timer(new_time):
     
    conn = sqlite3.connect('main.db')
    cur = conn.cursor()

    cur.execute('''UPDATE timer SET total_time = (?)''',
                (new_time,))
    conn.commit()

    cur.close()
    conn.close()
