"""
Usando el módulo pymysql crea una base de datos que permita registrar
y hacer un seguimiento de las ventas de un negocio. Que permita registrar detalles
de las ventas, como el producto vendido, la cantidad, el precio y la fecha y consultas
para generar informes de ventas diarias, mensuales o anuales.
"""


# Asegúrate de que el módulo pymysql esté instalado en tu entorno de Python.
# Puedes instalarlo usando pip:
# pip install pymysql

import pymysql

# Conectar a la base de datos
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='su_contraseña',
    db='ventas_db'
)
cursor = conn.cursor()

# Crear la tabla de ventas
cursor.execute('''
CREATE TABLE IF NOT EXISTS ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(255),
    cantidad INT,
    precio DECIMAL(10, 2),
    fecha_venta DATE
)
''')

# Función para registrar una venta


def agregar_venta(nombre_producto, cantidad, precio, fecha_venta):
    cursor.execute('''
    INSERT INTO ventas (nombre_producto, cantidad, precio, fecha_venta)
    VALUES (%s, %s, %s, %s)
    ''', (nombre_producto, cantidad, precio, fecha_venta))
    conn.commit()


# Ejemplo de uso
agregar_venta('Laptop', 2, 1500.00, '2024-06-10')
agregar_venta('Mouse', 5, 100.00, '2024-06-13')
agregar_venta('Monitor', 9, 500.00, '2024-06-17')

# Cerrar la conexión
conn.close()
