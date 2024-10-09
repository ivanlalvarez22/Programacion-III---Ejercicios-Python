"""
Escribir un programa que pida al usuario un número entero 
positivo y muestre por pantalla todos los números impares desde 
1 hasta ese número separados por comas.
"""

num = int(input("Ingrese un nro positivo: "))
while num <= 0:
    num = int(input("Ingrese un nro positivo: "))

print("[", end="")
for i in range(1, num + 1, 2):
    if i != num:
        print(i, end=", ")
    else:
        print(i, end="")
print("]")
