"""
Dado un número que representa la cantidad de lados de un polígono, determinar si se trata de un triángulo, cuadrilátero o de un pentágono; en caso de no tratarse de una de estas figuras, imprimir un mensaje.
"""

num = int(input("Ingrse un nro: "))

if num == 3:
    print("Triángulo")
elif num == 4:
    print("Cuadrilátero")
elif num == 5:
    print("Pentágono")
else:
    print("Error")  # este es un comentario

"""
lados = int(input("Ingrese los lados del poligono: "))

match(lados):
    case 3:
        print("Triángulo")
    case 4:
        print("Cuadrilátero")
    case 5:
        print("Pentágono")
    case _:
        print("error")

"""
