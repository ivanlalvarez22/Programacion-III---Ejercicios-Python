"""
Dados tres números A, B y C imprimir el mayor de ellos.
"""

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
c = int(input("Ingrese el valor de C: "))

if a > b:
    if a > c:
        print(f"El mayor es: {a}")
    else:
        print(f"El mayor es: {c}")

else:
    if b > c:
        print(f"El mayor es: {b}")
    else:
        print(f"El mayor es: {c}")
