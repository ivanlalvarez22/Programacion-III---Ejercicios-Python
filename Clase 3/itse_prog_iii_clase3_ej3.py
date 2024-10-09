"""
Escribir un programa que pregunte el nombre de un 
producto, su precio y un número de unidades y
muestre por pantalla una cadena con el nombre 
del producto seguido de su precio unitario con 
6 dígitos enteros y 2 decimales, el número de 
unidades con tres dígitos y el coste total con 8 
dígitos enteros y 2 decimales.
"""

nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
numero_unidades = int(input("Ingrese el número de unidades: "))

costo_total = precio_unitario * numero_unidades

print(f"Nombre del producto: {nombre_producto}\n"
      f"Precio unitario: $ {precio_unitario:09.2f}\n"
      f"Número de unidades: {numero_unidades:03}\n"
      f"Costo total: $ {costo_total:011.2f}\n")
