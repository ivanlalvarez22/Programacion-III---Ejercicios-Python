"""
Escribir un programa que pida al usuario dos números y 
muestre por pantalla su división. Si el divisor es cero el 
programa debe mostrar un error.
"""

dividendo = int(input("Ingrese el numerador: "))
divisor = int(input("Ingrese el denominador: "))

if divisor == 0:
    print("\033[91m¡Error! División por 0.\033[0m")
else:
    resultado = dividendo / divisor
    print(f"\033[92m{dividendo} dividido {divisor} es: {
        resultado}\033[0m")
