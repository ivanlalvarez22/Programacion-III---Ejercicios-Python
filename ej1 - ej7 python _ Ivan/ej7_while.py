"""
Dados 100 números, realizar la suma de los positivos y de los negativos.
"""

sumP = 0
sumN = 0

i = 0
while i < 5:
    num = int(input(f"Ingrese el {i + 1}° nro: "))

    if num > 0:
        sumP += num
    else:
        sumN += num

    i += 1

print(f"La suma de los positivos es {sumP}")
print(f"La suma de los negativos es {sumN}")
