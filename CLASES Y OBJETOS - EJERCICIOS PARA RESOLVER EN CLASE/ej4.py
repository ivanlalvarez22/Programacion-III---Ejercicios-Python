"""
Escribir una clase en python llamada circulo 
que contenga un radio, con un método 
que devuelva el área y otro que devuelva 
el perímetro del circulo.
"""

import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


# Ejemplo de uso:
circulo = Circulo(5)
print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())
