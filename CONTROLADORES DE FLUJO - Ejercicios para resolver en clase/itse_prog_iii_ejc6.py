"""
Escribir un programa que pida al usuario un número entero. Si es mayor de 10,
mostrar si es par o impar.
"""

num = int(input("Ingresar un nro: "))

if num > 10:
    if num % 2 == 0:
        print("El nro ingresado es mayor a 10 y es par.")
    else:
        print("El nro ingresado es mayor a 10 y es impar")
else:
    print("El nro es menor a 10")
