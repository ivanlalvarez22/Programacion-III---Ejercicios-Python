"""
Escribir un programa que pregunte por consola por los 
productos de una cesta de la compra, separados por 
comas, y muestre por pantalla cada uno de los productos 
en una línea distinta.
"""

productos = input(
    "Ingrese los productos de la cesta de compras separados por comas: ")

lista_productos = productos.split(",")

for producto in lista_productos:
    print(producto.strip())
