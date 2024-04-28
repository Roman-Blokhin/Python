import sqlite3

bd = sqlite3.connect('users_db.sqlite')
cur = bd.cursor()

cur.execute("""
create table if not exists USERS (
    name text,
    score integer
) """)

def get_best():
    cur.execute("""
    SELECT name gamer, max(score) score FROM USERS
    GROUP by name
    ORDER by score DESC
    LIMIT 3
    """)
    return cur.fetchall()

def insert_result(name, score):
    cur.execute("""
        insert into USERS values(?, ?)
    """, (name, score))
    bd.commit()


print(get_best())

# cur.close()
