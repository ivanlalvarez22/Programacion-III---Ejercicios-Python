"""
Crear una función que calcule la temperatura media de un día a 
partir de la temperatura máxima y mínima. Crear un programa 
principal, que utilizando la función anterior, vaya pidiendo la 
temperatura máxima y mínima de cada día y vaya mostrando la media. 
El programa pedirá el número de días que se van a introducir.
"""


def calcular_temperatura_media(temperatura_maxima, temperatura_minima):
    return (temperatura_maxima + temperatura_minima) / 2


num_dias = int(input("Ingrese el número de días: "))

for dia in range(1, num_dias + 1):
    temp_max = float(
        input(f"Ingrese la temperatura máxima del día {dia}: "))
    temp_min = float(
        input(f"Ingrese la temperatura mínima del día {dia}: "))

    temperatura_media = calcular_temperatura_media(
        temp_max, temp_min)

    print(f"La temperatura media del día {dia} es: {temperatura_media}")
