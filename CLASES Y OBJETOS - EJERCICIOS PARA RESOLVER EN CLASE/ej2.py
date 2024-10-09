"""
Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"
"""


class ReversorCadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def revertir(self):
        palabras = self.cadena.split()
        palabras_revertidas = palabras[::-1]
        cadena_revertida = ' '.join(palabras_revertidas)
        return cadena_revertida


# Ejemplo de uso:
reversor = ReversorCadena("Mi Diario Python")
print(reversor.revertir())
