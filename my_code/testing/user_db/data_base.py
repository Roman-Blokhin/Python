import sqlite3

bd = sqlite3.connect('users_db.sqlite')
cur = bd.cursor()

cur.execute("""
create table if not exists USERS (
    name text,
    score integer
) """)

cur.close()