"""
Escribir en pantalla los múltiplos de 3 entre 1 y 100. Sumarlos, y mostrar la suma al
final.
"""

sum = 0
num = int(input("Ingrese un nro (ingrese un negativo para salir): "))

while num >= 0:
    if num % 3 == 0 and num > 1 and num < 100:
        sum += num
    num = int(input("Ingrese un nro (ingrese un negativo para salir: )"))

print(f"La suma es: {sum}")
