"""
Escribir en pantalla los números que son múltiplos de 3 y están comprendidos entre
1 y 10.
"""

num = int(input("Ingrese un nro (ingrese un negativo para salir): "))
while num >= 0:
    if num % 3 == 0 and num > 1 and num < 10:
        print(num)

    num = int(input("Ingrese un nro (ingresar negativo para salir): "))

print("Programa finalizado.")
