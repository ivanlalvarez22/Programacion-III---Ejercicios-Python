"""
Escribir un programa que pida al usuario su nombre, su nacionalidad y su edad. Si
es un argentino y mayor a 18 años, mostrar su nombre. Si no, mostrar un mensaje
indicando que no puede ingresar.
"""

nombre = input("Ingrese su nombre: ")
nacionalidad = input("Ingrese su nacionalidad: ")
edad = int(input("Ingrese su edad: "))

if nacionalidad.lower() == "argentino" and edad >= 18:
    print(nombre)
else:
    print("No puede ingresar")
