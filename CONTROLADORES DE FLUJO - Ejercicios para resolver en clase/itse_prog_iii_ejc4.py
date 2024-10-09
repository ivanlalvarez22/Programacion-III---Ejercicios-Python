"""
Escribir un programa que pida al usuario dos números muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error.
"""

dividendo = int(input("Ingrese un nro: "))
divisor = int(input("Ingrese otro nro: "))

if divisor == 0:
    print("Error. El divisor es 0")
else:
    print(dividendo / divisor)
