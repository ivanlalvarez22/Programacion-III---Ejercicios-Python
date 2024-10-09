"""
Escribir un programa que pregunte por consola por los 
productos de una cesta de la compra, separados por 
comas, y muestre por pantalla cada uno de los productos 
en una línea distinta.
"""

productos = input(
    "Por favor, ingresa los productos de la cesta de la compra separados por comas: ")

lista_productos = productos.split(',')

for producto in lista_productos:
    # Utilizamos strip() para eliminar espacios en blanco alrededor del producto, si los hay
    print(producto.strip())
