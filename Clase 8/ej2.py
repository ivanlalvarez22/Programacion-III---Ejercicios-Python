"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
lista = [1, 2, 3, 4, 5]
lista[10]
"""

lista = [1, 2, 3, 4, 5]

try:
    valor = lista[10]
except IndexError as error:
    print("Error: Índice fuera de rango.")
    print("Causa: Estás intentando acceder a un índice que está más allá del tamaño de la lista.")
    print("Solución: Asegúrate de que el índice al que estás accediendo esté dentro del rango válido de la lista.")
