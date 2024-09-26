import sqlite3

conn = sqlite3.connect('Test_1.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code TEXT VARCHAR(2) NOT NULL PRIMARY KEY,
        title TEXT VARCHAR(150) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT VARCHAR(250) NOT NULL,
        category_code TEXT VARCHAR(2) NOT NULL,
        unit_price FLOAT DEFAULT 0.0, 
        stock_quantity INTEGER NOT NULL DEFAULT 0,
        store_id INTEGER,
        
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES store(store_id)
    )
''')

categories = [
    ('FD', 'Food products'),
    ('DS', 'Electronics'),
    ('CL', 'Clothes')
]
cursor.executemany('INSERT OR IGNORE INTO categories (code, title) VALUES (?, ?)', categories)

stores = [
    ('Asia',),
    ('Globus',),
    ('Spar',)
]
cursor.executemany('INSERT OR IGNORE INTO store (title) VALUES (?)', stores)

products = [
    ('Chocolate', 'FD', 10.5, 100, 1),
    ('iPhone 12', 'DS', 5000.9, 50, 2),
    ('MacBook Pro', 'DS', 15000.5, 25, 2),
    ('Sweater', 'CL', 20.2, 75, 3),
    ('T-shirt', 'CL', 30.7, 45, 3)
]
cursor.executemany('''
    INSERT OR IGNORE INTO products (title, category_code, unit_price, stock_quantity, store_id)
    VALUES (?, ?, ?, ?, ?)
''', products)

conn.commit()

print('Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:')
print('1. Asia \n2. Globus \n3. Spar')

spisok = None
while spisok != 0:
    spisok = int(input("Введите id магазина: "))

    if spisok in [1, 2, 3]:
        cursor.execute('''
            SELECT products.title, categories.title, products.unit_price, products.stock_quantity
            FROM products
            JOIN categories ON products.category_code = categories.code
            WHERE products.store_id = ?
        ''', (spisok,))

        products_in_store = cursor.fetchall()

        if products_in_store:
            for product in products_in_store:
                print(f"Название продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")
                print('-' * 30)

    elif spisok == 0:
        break

conn.close()
