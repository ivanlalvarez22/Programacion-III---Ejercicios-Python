"""
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla si es un palíndromo.
"""

# Solicitar al usuario que ingrese una palabra
palabra = input("Por favor, ingresa una palabra: ")

# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
