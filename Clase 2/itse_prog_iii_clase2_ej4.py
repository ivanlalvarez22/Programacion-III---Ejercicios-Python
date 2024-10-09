"""
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es par o impar.
"""

num = int(input("Ingrese un nro: "))
if num % 2 == 0:
    print(f"\033[92mEl número {num} es par\033[0m")
else:
    print(f"\033[92mEl número {num} es impar\033[0m")
