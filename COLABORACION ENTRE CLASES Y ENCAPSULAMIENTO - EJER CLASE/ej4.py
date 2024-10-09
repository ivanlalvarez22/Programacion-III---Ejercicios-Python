"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar
una clase con los métodos para inicializar los atributos, imprimir el valor del
lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
isósceles o escaleno).
"""


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir_datos(self):
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")


# Ejemplo de uso
l1 = float(input("Ingrese el valor del primer lado: "))
l2 = float(input("Ingrese el valor del segundo lado: "))
l3 = float(input("Ingrese el valor del tercer lado: "))

triangulo = Triangulo(l1, l2, l3)
triangulo.imprimir_datos()
