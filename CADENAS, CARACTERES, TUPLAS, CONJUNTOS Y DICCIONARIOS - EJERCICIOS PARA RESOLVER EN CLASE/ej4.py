"""
Escribir un programa que pregunte al usuario los números 
ganadores de la lotería de un determinado día, los 
almacene en una lista y los muestre por pantalla ordenados 
de menor a mayor.
"""

numeros_ganadores_str = input(
    "Ingrese los numeros ganadores separados por comas: ")

numeros_ganadores_int = [int(numero)
                         for numero in numeros_ganadores_str.split(",")]

numeros_ganadores_int.sort()

print(numeros_ganadores_int)
