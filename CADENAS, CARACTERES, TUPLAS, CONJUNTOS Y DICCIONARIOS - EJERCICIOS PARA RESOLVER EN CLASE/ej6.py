"""
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla si es un palíndromo.
"""

palabra = input("Ingrese una palabra: ")

if palabra == palabra[::-1]:
    print("Es palíndromo")
else:
    print("No es palíndromo")
