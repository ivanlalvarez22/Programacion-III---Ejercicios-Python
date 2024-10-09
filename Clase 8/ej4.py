"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 15 + "20"
"""

try:
    resultado = 15 + "20"
except TypeError as error:
    print("Error: Tipos de datos incompatibles.")
    print("Causa: Estás intentando realizar una operación entre un entero y una cadena.")
    print("Solución: Asegúrate de que los tipos de datos involucrados en la operación sean compatibles.")
