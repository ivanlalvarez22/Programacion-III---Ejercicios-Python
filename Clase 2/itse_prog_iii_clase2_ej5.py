"""
Para tributar un determinado impuesto se debe ser mayor de 
16 años y tener unos ingresos iguales o superiores a 300000 
pesos mensuales. Escribir un programa que pregunte al usuario 
su edad y sus ingresos mensuales y muestre por pantalla si 
el usuario tiene que tributar o no.
"""

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Indique sus ingresos mensuales: "))

if edad >= 16 and ingresos >= 300000:
    print(f"\033[92mUsted debe tributar.\033[0m")
else:
    print(f"\033[92mUsted no debe tributar.\033[0m")
