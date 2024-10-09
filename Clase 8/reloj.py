"""
Desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora
actual. Hazlo en un script llamado reloj.py y ejecútalo en la terminal
"""


import datetime


def mostrar_reloj():
    ahora = datetime.datetime.now()
    hora = ahora.hour
    minutos = ahora.minute
    segundos = ahora.second

    print(f"{hora:02d}:{minutos:02d}:{segundos:02d}")


if __name__ == "__main__":
    mostrar_reloj()
