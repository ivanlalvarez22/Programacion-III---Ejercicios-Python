"""
Escribir un programa que asigne a una variable un
dato (int, float, cadena, etc.) y muestre por consola su
tipo de dato.
"""

entero = 10
flotante = 3.14
cadena = "Hola mundo"
booleano = False
lista = [1, 3, 4, 7, 1]
tupla = (1, 2, 3)
diccionario = {"clave1": 22, "clave2": True}
conjunto = {1, 2, 3}

print(f"{type(entero)} {type(flotante)} {type(cadena)} {
    type(booleano)} {type(lista)} {type(tupla)} {
    type(diccionario)} {type(conjunto)}")
