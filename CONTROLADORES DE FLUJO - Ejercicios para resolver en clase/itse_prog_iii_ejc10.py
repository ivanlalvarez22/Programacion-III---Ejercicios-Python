"""
Escribir en pantalla los números enteros entre dos números enteros que se piden al
usuario
"""

num1 = int(input("Ingrese un nro: "))
num2 = int(input("Ingrese otro nro: "))

for i in range(num1 + 1, num2, 1):
    print(i)
