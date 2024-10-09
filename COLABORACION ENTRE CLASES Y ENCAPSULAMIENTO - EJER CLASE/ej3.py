"""
Modelar un sanatorio donde los pacientes tienen los siguientes atributos:
DNI, obra social, nombre, apellido, número habitación, estado (habitación
común, terapia intermedia, terapia intensiva). Implementar métodos que
permitan ver los datos de los pacientes, ver su estado y cambiar de estado.
Definir como atributo privado el DNI y estado y definir los métodos
adecuados para leerlos o bien establecer un nuevo valor.
"""


class Paciente:
    def __init__(self, dni, obra_social, nombre, apellido, numero_habitacion, estado):
        self.__dni = dni
        self.obra_social = obra_social
        self.nombre = nombre
        self.apellido = apellido
        self.numero_habitacion = numero_habitacion
        self.__estado = estado

    def ver_datos(self):
        return {
            "DNI": self.__dni,
            "Obra Social": self.obra_social,
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "Número de Habitación": self.numero_habitacion,
            "Estado": self.__estado
        }

    def ver_estado(self):
        return self.__estado

    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def ver_dni(self):
        return self.__dni

    def cambiar_dni(self, nuevo_dni):
        self.__dni = nuevo_dni


# Ejemplo de uso
paciente1 = Paciente("12345678", "Obra Social A", "Juan",
                     "Pérez", 101, "habitación común")

print(paciente1.ver_datos())

print(paciente1.ver_estado())

paciente1.cambiar_estado("terapia intensiva")
print(paciente1.ver_estado())
