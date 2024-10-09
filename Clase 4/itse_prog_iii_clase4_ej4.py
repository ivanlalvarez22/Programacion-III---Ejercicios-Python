"""
Escribir una función que reciba una frase y devuelva un 
diccionario con las palabras que contiene y su longitud.
"""


def longitud_palabra(frase):
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario


print(longitud_palabra(input("Ingrese una frase: ")))
