"""
Escribir un programa que almacene en una lista los 
números del 1 al 10 y los muestre por pantalla en orden 
inverso separados por comas.
"""

# Crear una lista con los números del 1 al 10 utilizando la función range()
numeros = list(range(1, 11))

# Invierte la lista de números y la asigna a la variable numeros_inverso
numeros_inverso = numeros[::-1]

# Imprime la lista invertida por pantalla
print(numeros_inverso)
