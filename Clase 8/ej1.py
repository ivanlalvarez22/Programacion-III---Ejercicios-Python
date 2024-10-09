"""
Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el
programa se blo1quee y además explica en un mensaje al usuario la causa y/o solución:
resultado = 10/0
"""

try:
    resultado = 10 / 0
except ZeroDivisionError as error:
    print("Error: División por cero.")
    print("Causa: La división entre cero no está definida en matemáticas.")
    print("Solución: Revisa el denominador en la operación y asegúrate de que no sea cero.")
