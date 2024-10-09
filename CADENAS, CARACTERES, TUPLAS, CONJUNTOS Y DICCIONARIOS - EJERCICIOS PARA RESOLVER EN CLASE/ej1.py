"""
Escribir un programa que pregunte al usuario la
fecha de su nacimiento en formato dd/mm/aaaa y
muestra por pantalla, el día, el mes y el año.
"""
from datetime import datetime


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False


fecha_nacimiento = input(
    "Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

while not validar_fecha(fecha_nacimiento):
    fecha_nacimiento = input(
        "Fecha inválida. Por favor ingrese la fecha en formato dd/mm/aaaa: ")

dia, mes, anio = fecha_nacimiento.split("/")

print(dia)
print(mes)
print(anio)
