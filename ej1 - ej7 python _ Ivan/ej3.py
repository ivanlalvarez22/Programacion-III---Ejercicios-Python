"""
Leer dos números, almacenarlos en las variables X y Y respectivamente. Intercambiar el contenido de las variables de manera que el valor contenido en X pase a Y, y el valor contenido en Y pase a X.
"""

x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

aux = x
x = y
y = aux

print(f"El valor de x ahora es: {x}")
print(f"El valor de y ahora es: {y}")
