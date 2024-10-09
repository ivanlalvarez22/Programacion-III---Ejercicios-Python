"""
Usando el módulo sqlite3 crea una base de datos para administrar las
reservas de habitaciones de un hotel. Que permita registrar nuevas reservas,
verificar la disponibilidad de habitaciones en fechas específicas (consulta por
número de habitación y fecha) y generar consultas sobre las reservas actuales y
futuras.
"""

import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('hotel_reservations.db')
cursor = conn.cursor()

# Crear la tabla de reservas
cursor.execute('''
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number INTEGER,
    start_date TEXT,
    end_date TEXT,
    guest_name TEXT
)
''')

# Función para registrar una nueva reserva


def add_reservation(room_number, start_date, end_date, guest_name):
    cursor.execute('''
    INSERT INTO reservations (room_number, start_date, end_date, guest_name)
    VALUES (?, ?, ?, ?)
    ''', (room_number, start_date, end_date, guest_name))
    conn.commit()

# Función para verificar la disponibilidad de una habitación en una fecha específica


def check_availability(room_number, date):
    cursor.execute('''
    SELECT * FROM reservations
    WHERE room_number = ? AND ? BETWEEN start_date AND end_date
    ''', (room_number, date))
    return cursor.fetchall()


# Ejemplo de uso
add_reservation(101, '2024-06-15', '2024-06-20', 'John Doe')
print(check_availability(101, '2024-06-16'))

# Cerrar la conexión
conn.close()
