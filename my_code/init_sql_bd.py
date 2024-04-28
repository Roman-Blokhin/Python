import sqlite3

bd = sqlite3.connect('test.sqlite')  # замени test
cur = bd.cursor()

# замени test
cur.execute("""
create table if not exists test (
    name text,
    score integer
) """)

cur.close()