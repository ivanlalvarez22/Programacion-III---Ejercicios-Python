"""
Leer números enteros, y contar la cantidad de pares e impares que se han ingresado
hasta que se ingrese un número negativo.
"""

contador_pares = 0
contador_impares = 0

numero = int(
    input("Ingrese un número entero (ingrese un número negativo para salir): "))

while numero >= 0:
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

    numero = int(
        input("Ingrese un número entero (ingrese un número negativo para salir): "))

print(f"Cantidad de números pares: {contador_pares}")
print(f"Cantidad de números impares: {contador_impares}")
