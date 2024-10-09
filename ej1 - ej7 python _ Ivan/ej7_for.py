"""
Dados 100 números, realizar la suma de los positivos y de los negativos.
"""

sumP = 0
sumN = 0

for i in range(0, 5, 1):
    num = int(input(f"Ingrese el {i + 1}° valor: "))

    if num > 0:
        sumP += num
    else:
        sumN += num

print(f"La suma de los positivos es: {sumP}")
print(f"La suma de los negativos es: {sumN}")

"""
sumP = 0
sumN = 0

for i in range(5): # por defecto i comienza en 0 y el incremento es +1
    num = int(input(f"Ingrese el {i + 1}° valor: "))

    if num > 0:
        sumP += num
    else:
        sumN += num

print(f"La suma de los positivos es: {sumP}")
print(f"La suma de los negativos es: {sumN}")

"""
