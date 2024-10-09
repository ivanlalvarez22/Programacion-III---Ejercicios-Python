"""
Escribir una clase en python con 2 métodos: 
get_string y print_string. get_string acepta una 
cadena ingresada por el usuario y print_string 
imprime la cadena en
mayúsculas.
"""


class ManipuladorTexto:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Ingrese una cadena: ")

    def print_string(self):
        print(f"La cadena ingresada es {self.string.upper()}")


imprimir = ManipuladorTexto()
imprimir.get_string()
imprimir.print_string()
