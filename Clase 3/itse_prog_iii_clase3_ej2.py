"""
Escribir un programa que pregunte el correo 
electrónico del usuario en la consola y muestre 
por pantalla otro correo electrónico con el 
mismo nombre (la parte delante de la arroba @) 
pero con dominio gob.ar.
"""

import re


def validar_correo(email):
    # Definir el patrón de expresión regular para validar el correo electrónico
    patron = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    # Comprobar si el correo electrónico coincide con el patrón
    return patron.match(email)


correo_electronico = input("Ingrese su correo electrónico: ")
while not validar_correo(correo_electronico):
    correo_electronico = input(
        "Por favor, ingrese un correo electrónico válido: ")

partes = correo_electronico.split("@")
nuevo_correo = partes[0] + "@gob.ar"
print(nuevo_correo)
