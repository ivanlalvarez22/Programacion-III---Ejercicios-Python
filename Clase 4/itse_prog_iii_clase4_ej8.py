"""
Utilizar la función incorporada map() para crear una función 
que retorne una lista con la longitud de cada palabra 
(separada por espacios) de una frase. La función recibe una 
cadena de texto y retornara una lista.
"""


def longitud_palabras(frase):
    return ' '.join(map(str, map(len, frase.split())))


texto_ejemplo = input("Por favor, ingrese una frase: ")
resultado = longitud_palabras(texto_ejemplo)
print(resultado)
