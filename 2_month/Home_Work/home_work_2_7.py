import sqlite3

conn = sqlite3.connect('homework_7.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
    price REAL NOT NULL DEFAULT 0.0 CHECK(price >= 0),
    quantity INTEGER NOT NULL DEFAULT 0 CHECK(quantity >= 0)
)
''')

conn.commit()

def add_products():
    products = [
        ('Хлеб', 10.99, 50),
        ('Детское мыло', 5.99, 20),
        ('Хлеб ржаной', 100.50, 5),
        ('Жвачка', 0.99, 100),
        ('Яица', 49.99, 10),
        ('Колбоса', 79.99, 2),
        ('Сыр', 150.25, 1),
        ('Мыло', 9.99, 0),
        ('Жидкое мыло', 25.99, 25),
        ('Дегтярное мыло', 11.49, 10),
        ('Нож', 4.59, 300),
        ('Мясо', 55.55, 3),
        ('Перец', 8.75, 15),
        ('Лук', 95.00, 7),
        ('Ваниль', 3.99, 200),
    ]
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)
    ''', products)
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('''
        UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('''
        UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id,))
    conn.commit()

def select_all_products():
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def select_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('''
        SELECT * FROM products WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def search_products_by_title(keyword):
    cursor.execute('''
        SELECT * FROM products WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# add_products()

# select_all_products()

# update_quantity(1, 75)

# update_price(2, 7.99)

# delete_product(3)

# select_all_products()

# select_products_by_price_and_quantity(100, 5)

# search_products_by_title('мыло')

conn.close()