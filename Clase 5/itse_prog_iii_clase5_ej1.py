"""
Desarrollar un programa que cargue los datos de un triángulo. 
Implementar una clase con los métodos para inicializar los 
atributos, imprimir el valor del lado con un tamaño mayor y 
el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""


class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtener_lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

    def obtener_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "isósceles"
        else:
            return "escaleno"


# Función para cargar los datos del triángulo
def cargar_triangulo():
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))
    return lado1, lado2, lado3


# Función principal
def main():
    lado1, lado2, lado3 = cargar_triangulo()
    triangulo = Triangulo(lado1, lado2, lado3)

    print(f"El lado de mayor longitud mide: {triangulo.obtener_lado_mayor()}")
    print(f"El triángulo es de tipo: {triangulo.obtener_tipo()}")


if __name__ == "__main__":
    main()
