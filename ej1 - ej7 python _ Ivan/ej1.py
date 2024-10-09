"""
Leer tres números en las variables A, B y C, realizar los siguientes cálculos e imprimir los resultados:
a- La suma de los tres
b- La diferencia del primero respecto del segundo
c- El producto de los dos últimos
d- La división entre el primero y el tercero
"""

a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
c = int(input("Ingrese el valor de C: "))

sum = a + b + c
rest = a - b
mult = b * c

if c != 0:
    div = a / c
    print(f"El resultado de la division es: {div}")
else:
    print("Eror, división por 0")

print(f"El resultado de la suma es {sum}")
print(f"El resultado de la resta es {rest}")
print(f"El resultado de la mult es: {mult}")
