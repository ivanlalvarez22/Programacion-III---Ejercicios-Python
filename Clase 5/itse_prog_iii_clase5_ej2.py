"""
Realizar un programa en el cual se declaren dos 
valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora
"""


class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        # Validación para evitar división por cero
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "No se puede dividir entre cero."


def main():
    valor1 = int(input("Ingrese el primer valor entero: "))
    valor2 = int(input("Ingrese el segundo valor entero: "))

    calculadora = Calculadora(valor1, valor2)

    print("Suma:", calculadora.suma())
    print("Resta:", calculadora.resta())
    print("Multiplicación:", calculadora.multiplicacion())
    print("División:", calculadora.division())


if __name__ == "__main__":
    main()
