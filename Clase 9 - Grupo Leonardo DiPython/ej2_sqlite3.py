"""
Usando el módulo sqlite3 o pymysql crea una base de datos para gestionar el
inventario de una biblioteca. Permite agregar nuevos libros, registrar préstamos y
devoluciones y consultas para buscar libros por título, autor o género
"""

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('library_inventory.db')
cursor = conn.cursor()

# Crear la tabla de libros
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    genre TEXT,
    available INTEGER
)
''')

# Crear la tabla de préstamos
cursor.execute('''
CREATE TABLE IF NOT EXISTS loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER,
    borrower_name TEXT,
    loan_date TEXT,
    return_date TEXT
)
''')

# Función para agregar un nuevo libro


def add_book(title, author, genre):
    cursor.execute('''
    INSERT INTO books (title, author, genre, available)
    VALUES (?, ?, ?, ?)
    ''', (title, author, genre, 1))
    conn.commit()

# Función para registrar un préstamo


def register_loan(book_id, borrower_name, loan_date):
    cursor.execute('''
    UPDATE books SET available = 0 WHERE id = ?
    ''', (book_id,))
    cursor.execute('''
    INSERT INTO loans (book_id, borrower_name, loan_date)
    VALUES (?, ?, ?)
    ''', (book_id, borrower_name, loan_date))
    conn.commit()


# Ejemplo de uso
add_book('1984', 'George Orwell', 'Dystopian')
register_loan(1, 'Jane Doe', '2024-06-10')

# Cerrar la conexión
conn.close()
