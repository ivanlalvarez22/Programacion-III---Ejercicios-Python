"""
Diseñe un diccionario que tome como entrada un texto de al menos diez líneas y 
muestre un listado de las 10 palabras más frecuentes 
(use la función collections-counter)
"""

from collections import Counter


def contar_palabras(texto_entrada):
    """
    Función que cuenta la frecuencia de palabras en un texto.
    """
    # Dividir el texto en palabras y convertirlas a minúsculas
    palabras = texto_entrada.lower().split()

    # Contar la frecuencia de cada palabra
    frec_palabras = Counter(palabras)

    return frec_palabras


def palabras_mas_frecuentes(frecuencia_palabras_entrada, n=10):
    """
    Función que muestra las n palabras más frecuentes de un diccionario de frecuencia de palabras.
    """
    # Obtener las n palabras más frecuentes
    mas_frecuentes = frecuencia_palabras_entrada.most_common(n)

    # Mostrar las n palabras más frecuentes
    print("Las {} palabras más frecuentes son:".format(n))
    for palabra, frecuencia in mas_frecuentes:
        print(f"{palabra}: {frecuencia} veces")


if __name__ == "__main__":
    texto = """
    Python es un lenguaje de programación poderoso y fácil de aprender. 
    Tiene estructuras de datos eficientes y de alto nivel, así como un enfoque simple 
    pero efectivo de la programación orientada a objetos. Python es elegante y fácil de leer, 
    lo que lo convierte en un gran lenguaje para principiantes. Sin embargo, también es 
    utilizado por muchos profesionales en una amplia variedad de campos. Python tiene una 
    gran biblioteca estándar y una comunidad activa que continúa mejorando el lenguaje. 
    Además, Python es compatible con múltiples plataformas y sistemas operativos, 
    lo que lo hace versátil y portátil.
    """

    # Contar la frecuencia de palabras en el texto
    frecuencia_palabras = contar_palabras(texto)

    # Mostrar las 10 palabras más frecuentes
    palabras_mas_frecuentes(frecuencia_palabras, 10)
