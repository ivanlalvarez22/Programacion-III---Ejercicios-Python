"""
Escribir un programa que reciba una cadena de caracteres y 
devuelva un diccionario con cada palabra que contiene y su 
frecuencia. Escribir otra función que reciba el diccionario 
generado con la función anterior y devuelva una tupla con 
la palabra más repetida y su frecuencia.
"""


def contar_palabras(frase):
    palabras = frase.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


def palabra_mas_repetida(diccionario):
    palabra_mas_frecuente = ""
    frecuencia_maxima = 0
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_maxima:
            palabra_mas_frecuente = palabra
            frecuencia_maxima = frecuencia
    return (palabra_mas_frecuente, frecuencia_maxima)


# Ejemplo de uso:
frase_ejemplo = "Esta es una frase de ejemplo es una prueba"
frecuencia_palabras = contar_palabras(frase_ejemplo)
print("Diccionario de frecuencia de palabras:", frecuencia_palabras)

palabra_max_rep, frecuencia_max_rep = palabra_mas_repetida(frecuencia_palabras)
print("Palabra más repetida:", palabra_max_rep)
print("Frecuencia de la palabra más repetida:", frecuencia_max_rep)

# frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
# Agrega palabras al diccionario frecuencia.
# Si la palabra ya existe en el diccionario, simplemente
# incrementa su frecuencia en 1. Si la palabra no existe en
# el diccionario, se inicializa su frecuencia en 1.
