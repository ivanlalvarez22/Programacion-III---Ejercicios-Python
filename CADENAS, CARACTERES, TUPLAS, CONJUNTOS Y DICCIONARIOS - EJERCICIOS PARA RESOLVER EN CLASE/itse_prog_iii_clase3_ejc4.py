"""
Escribir un programa que pregunte al usuario los números 
ganadores de la lotería de un determinado día, los 
almacene en una lista y los muestre por pantalla ordenados 
de menor a mayor.
"""

numeros_ganadores_str = input(
    "Ingrese los números ganadores de la lotería separados por comas: ")

# Convertir la cadena de números en una lista de enteros
numeros_ganadores = [int(numero)
                     for numero in numeros_ganadores_str.split(',')]

# Ordenar la lista de números ganadores de menor a mayor
numeros_ganadores.sort()

# Mostrar los números ganadores ordenados por pantalla
print("Números ganadores ordenados de menor a mayor:")
for numero in numeros_ganadores:
    print(numero, end=" ")
