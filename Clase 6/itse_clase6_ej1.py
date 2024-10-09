"""
Crear una clase "Empleado" que pertenecen a una institución con atributos
como nombre, salario y fecha de inicio de su actividad en la institución.
Implementa métodos para obtener los datos del empleado, establecer la
antigüedad del empleado y calcular el aumento de salario en función de la
antigüedad. La institución requiere un listado de los empleados ingresados
a la institución. Definir como atributo privado el salario y definir los métodos
adecuados para leerlo o bien establecer un nuevo valor.
"""

from datetime import date


class Empleado:
    def __init__(self, nombre, salario, fecha_inicio):
        self.nombre = nombre
        self.__salario = salario  # Atributo privado
        self.fecha_inicio = fecha_inicio

    # Método para obtener los datos del empleado
    def obtener_datos(self):
        return {
            "Nombre": self.nombre,
            "Salario": self.__salario,
            "Fecha de Inicio": self.fecha_inicio,
            "Antigüedad": self.calcular_antiguedad()
        }

    # Método para calcular la antigüedad del empleado
    def calcular_antiguedad(self):
        fecha_actual = date.today()
        antiguedad = fecha_actual.year - self.fecha_inicio.year
        if fecha_actual.month < self.fecha_inicio.month or (fecha_actual.month == self.fecha_inicio.month and fecha_actual.day < self.fecha_inicio.day):
            antiguedad -= 1
        return antiguedad

    # Método para calcular el aumento de salario en función de la antigüedad
    def calcular_aumento_salario(self, porcentaje_anual):
        antiguedad = self.calcular_antiguedad()
        aumento = self.__salario * \
            ((1 + (porcentaje_anual / 100)) ** antiguedad - 1)
        return aumento

    # Método para leer el salario
    def obtener_salario(self):
        return self.__salario

    # Método para establecer un nuevo valor de salario
    def establecer_salario(self, nuevo_salario):
        self.__salario = nuevo_salario


# Lista de empleados
empleados = []

# Función para agregar empleados a la lista


def agregar_empleado(nombre, salario, fecha_inicio):
    nuevo_empleado = Empleado(nombre, salario, fecha_inicio)
    empleados.append(nuevo_empleado)


# Ejemplo de uso
agregar_empleado("Juan Perez", 30000, date(2018, 5, 10))
agregar_empleado("Ana Gomez", 32000, date(2020, 3, 15))

# Mostrar datos de los empleados
for empleado in empleados:
    datos = empleado.obtener_datos()
    print(f"Nombre: {datos['Nombre']}, Salario: {datos['Salario']}, Fecha de Inicio: {
          datos['Fecha de Inicio']}, Antigüedad: {datos['Antigüedad']} años")

# Calcular aumento de salario para un empleado
porcej_anual = 5  # Ejemplo: 5% de aumento anual
for empleado in empleados:
    incremento_salario = empleado.calcular_aumento_salario(porcej_anual)
    print(f"Aumento de salario para {
          empleado.nombre}: {incremento_salario:.2f}")
