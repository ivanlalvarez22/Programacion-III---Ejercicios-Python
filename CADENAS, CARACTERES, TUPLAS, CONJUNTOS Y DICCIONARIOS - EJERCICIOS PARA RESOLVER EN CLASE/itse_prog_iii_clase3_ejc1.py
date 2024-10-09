"""
Escribir un programa que pregunte al usuario la 
fecha de su nacimiento en formato dd/mm/aaaa y 
muestra por pantalla, el día, el mes y el año.
"""

from datetime import datetime


def validar_fecha(fecha):
    try:
        # Intentar crear un objeto datetime a partir de la cadena de fecha
        datetime.strptime(fecha, '%d/%m/%Y')  # string parse time
        return True
    except ValueError:
        # Si ocurre un ValueError, la fecha no es válida
        return False


fecha_nacimiento = input(
    "Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

# Validar la fecha ingresada por el usuario
while not validar_fecha(fecha_nacimiento):
    fecha_nacimiento = input(
        "Fecha inválida. Por favor, ingrese una fecha en el formato correcto (dd/mm/aaaa).")

dia, mes, anio = fecha_nacimiento.split('/')
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)
