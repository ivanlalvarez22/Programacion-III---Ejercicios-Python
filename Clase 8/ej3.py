"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
colores['blanco']
"""


colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}

try:
    valor = colores['blanco']
except KeyError as error:
    print("Error: Clave no encontrada.")
    print("Causa: Estás intentando acceder a una clave que no existe en el diccionario.")
    print("Solución: Asegúrate de que la clave que estás buscando esté presente en el diccionario.")
