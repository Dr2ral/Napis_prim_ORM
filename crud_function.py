import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()
def get_all_products():
    conn = sqlite3.connect("not_telegram.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL);
    ''')
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES(?,?,?)', (f'Продукт{i}', f'{i}', i*100))
    res = conn.cursor().execute("SELECT * FROM Products").fetchall()
    conn.commit()
    conn.close()
    return res


def initiate_db():
    conn = sqlite3.connect("not_telegram.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL 
    );
    """)
    conn.commit()

def add_user(username, email, age):
    conn = sqlite3.connect("not_telegram.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL 
        );
        """)
    conn.commit()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)",
                   (f"{username}", f"{email}", f"{age}"))
    conn.commit()

def is_included(username):
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL 
            );
            """)
    conn.commit()
    s = cursor.execute('SELECT username FROM Users').fetchall()
    connection.commit()
    return (username,) in s


