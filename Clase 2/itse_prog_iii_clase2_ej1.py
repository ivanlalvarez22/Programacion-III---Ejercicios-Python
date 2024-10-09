"""
Escribir un programa que pregunte al usuario su edad y muestre 
por pantalla si es mayor de edad o no.
"""

edad = int(input("Ingrese su edad: "))
# bucle para validar la edad.
while edad <= 0:
    edad = int(input("\033[91mIngrese una edad válida: \033[0m"))

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
