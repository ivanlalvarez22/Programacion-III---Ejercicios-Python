"""
Escribir un programa que cree un diccionario de 
traducción español-inglés. El usuario introducirá 
las palabras en español e inglés separadas por dos 
puntos, y cada par <palabra>:<traducción> separados 
por comas. El programa debe crear un diccionario 
con las palabras y sus traducciones. Después pedirá 
una frase en español y utilizará el diccionario 
para traducirla palabra a palabra. Si una palabra 
no está en el diccionario debe dejarla sin 
traducir.
"""

diccionario = {}
entrada = input((
    "Introduce las palabras en español e inglés separadas por dos puntos, "
    "y cada par <palabra>:<traducción> separados por comas: "
))

# Dividir la entrada en pares <palabra>:<traducción> y agregar al diccionario
pares = entrada.split(",")
for par in pares:
    clave, valor = par.split(":")
    diccionario[clave.strip()] = valor.strip()

# Pedir al usuario una frase en español
frase_espaniol = input("Introduce una frase en español: ")

# Traducir la frase palabra a palabra utilizando el diccionario
palabras = frase_espaniol.split()
frase_traducida = " ".join(
    diccionario[palabra] if palabra in diccionario else palabra for palabra in palabras)

print("Frase traducida:", frase_traducida)
