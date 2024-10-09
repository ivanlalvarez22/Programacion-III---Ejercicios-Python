"""
Realizar un programa que tenga una clase Persona con las 
siguientes características. La clase tendrá como atributos 
el nombre y la edad de una persona. Implementar los métodos 
necesarios para inicializar los atributos, mostrar los datos 
e indicar si la persona es mayor de edad o no.
"""


class Persona:
    def __init__(self, nombre_persona, edad_persona):
        self.nombre_persona = nombre_persona
        self.edad_persona = edad_persona

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre_persona}")
        print(f"Edad: {self.edad_persona}")

    def es_mayor_de_edad(self):
        return self.edad_persona >= 18


# Ejemplo de uso:
nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))

persona = Persona(nombre, edad)
persona.mostrar_datos()
if persona.es_mayor_de_edad():
    print("Esta persona es mayor de edad.")
else:
    print("Esta persona no es mayor de edad.")
