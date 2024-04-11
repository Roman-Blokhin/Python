# СОЗДАЕМ БАЗУ ДАННЫХ

# 1. импортируем модуль
import sqlite3

# 2. создаем коннект с базой данных, создастся файл
bd = sqlite3.connect('2048.sqlite')

# 3. создаем курсор
cur = bd.cursor()

# 5. создаем таблицу в базе данных, прописываем команду создания таблицы, ее название
# указываем название колонок и типы данных для хранения
# 5.1 if not exists - означает "если таблица еще не создана", прописываем, если будет еще sql запрос далее
cur.execute("""
create table if not exists RECORDS (  
    name text,
    score integer
)""")

# 6. создаем новую таблицу с корректным запросом вывода информации
cur.execute("""
SELECT name gamer, max(score) score FROM RECORDS
GROUP by name
ORDER by score DESC
LIMIT 3
""")

# 7. выводим результат запроса базы данных в консоль и сохраняем в переменную
result = cur.fetchall()
print(result)

# 4. закрываем курсор
cur.close()

# -----------------------
# SELECT ROWID, name, score FROM RECORDS - вывести данные из таблицы во вкладке sql
# (ROWID - стандартное поле порядка строк, все числа уникальные, при удалении не восстанавливаются)
# ORDER by score - сортировка по колонке score от меньшего к большему
# ORDER by score DESC - сортировка по колонке score от большего к меньшему
# LIMIT 3 - выводит только первые 3 строки после сортировки
# GROUP by name - группировка по колонке name
# SELECT name, max(score) FROM RECORDS - max(score) выводит максимальное число по колонке score после группировки