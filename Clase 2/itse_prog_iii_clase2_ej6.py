"""
Escribir un programa para una empresa que tiene salas de juegos 
para todas las edades y quiere calcular de forma automática el 
precio que debe cobrar a sus clientes por entrar. El programa 
debe preguntar al usuario la edad del cliente y mostrar el precio 
de la entrada. Si el cliente es menor de 4 años puede entrar 
gratis, si tiene entre 4 y 18 años debe pagar 3000 pesos y si es 
mayor de 18 años, 10.000 pesos.
"""


edad = int(input("Por favor, introduce tu edad: "))

if edad < 4:
    precio = 0
elif 4 <= edad <= 18:
    precio = 3000
else:
    precio = 10000


print(f"\033[92mEl precio de la entrada es ${precio}.\033[0m")
