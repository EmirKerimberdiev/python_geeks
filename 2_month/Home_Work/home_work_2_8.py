import sqlite3

conn = sqlite3.connect('Tables.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area TEXT NOT NULL,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(title)
    )
''')


countries = [
    ('Кгызыстан',),
    ('Казакстан',),
    ('Япония',)
]
cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)


cursor.execute('SELECT id, title FROM countries')
country_dict = {title: id for id, title in cursor.fetchall()}

cities = [
    ('Бишкек', 127.0, country_dict.get('Кгызыстан')),
    ('Ош', 182.0, country_dict.get('Кгызыстан')),
    ('Каракол', 52.53, country_dict.get('Кгызыстан')),
    ('Астана', 797.33, country_dict.get('Казакстан')),
    ('Токио', 2194.0, country_dict.get('Япония')),
    ('Китагава', 196.2, country_dict.get('Япония')),
    ('Киото', 827.9, country_dict.get('Япония'))
]
cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)

students = [
    ('Иван', 'Иванов', 'Бишкек'),
    ('Петр', 'Петров', 'Ош'),
    ('Сергей', 'Сергеев', 'Каракол'),
    ('Алексей', 'Алексеев', 'Астана'),
    ('Михаил', 'Михайлов', 'Токио'),
    ('Анна', 'Андреева', 'Китагава'),
    ('Даниил', 'Данилов', 'Киото'),
    ('Елизавета', 'Елизарова', 'Китагава'),
    ('Артемий', 'Артемьев', 'Астана'),
    ('Мария', 'Марьянова', 'Токио'),
    ('Никита', 'Никитина', 'Киото'),
    ('Светлана', 'Светланова', 'Киото'),
    ('Александр', 'Александров', 'Астана'),
    ('Ирина', 'Иринина', 'Каракол'),
    ('Алина', 'Алинкова', 'Китагава'),
]
cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?,?,?)', students)


conn.commit()
conn.close()

print('1. Бишкек\n2. Ош\n3. Каракол\n4. Астана\n5. Токио\n6. Китагава\n7. Киото')
spisok = int(input('Вы моожете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:'))



if spisok == 0:
    exit()
elif spisok == 1:
    for student in students:
        if student[2] == 'Бишкек':
            print(student[0], student[1])
elif spisok == 2:
    for student in students:
        if student[2] == 'Ош':
            print(student[0], student[1])
elif spisok == 3:
    for student in students:
        if student[2] == 'Каракол':
            print(student[0], student[1])
elif spisok == 4:
    for student in students:
        if student[2] == 'Астана':
            print(student[0], student[1])
elif spisok == 5:
    for student in students:
        if student[2] == 'Токио':
            print(student[0], student[1])
elif spisok == 6:
    for student in students:
        if student[2] == 'Китагава':
            print(student[0], student[1])
elif spisok == 7:
    for student in students:
        if student[2] == 'Киото':
            print(student[0], student[1])
