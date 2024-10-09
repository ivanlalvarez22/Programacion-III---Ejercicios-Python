"""
Escribir un programa que pregunte al usuario una cantidad a 
invertir, el interés anual y el número de años, y muestre por 
pantalla el capital obtenido en la inversión cada año que dura 
la inversión.
"""

cantidad_invertida = float(input("Ingrese la cantidad a invertir: "))
interes_anual = 1 + int(input("Ingrese el interes anual: ")) / 100
cantidad_anios = int(input("Ingrese la cantidad de años: "))
capital_obtenido = 0

for i in range(cantidad_anios):
    capital_obtenido = cantidad_invertida * interes_anual ** (i + 1)
    print("$", capital_obtenido)
