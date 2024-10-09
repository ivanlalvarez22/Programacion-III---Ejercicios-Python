"""
Escribir una clase en python que calcule la potencia(x, n)
x = es la base
n = es el exponente
"""


class Potencia:
    def calcular_potencia(self, x, n):
        return x ** n


potencia = Potencia()
print(potencia.calcular_potencia(2, 3))
