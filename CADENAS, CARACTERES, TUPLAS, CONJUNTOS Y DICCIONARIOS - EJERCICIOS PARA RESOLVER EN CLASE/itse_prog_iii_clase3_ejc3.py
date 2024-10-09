"""
Escribir un programa que pida al usuario que introduzca 
una frase en la consola y muestre por pantalla la frase 
invertida.
"""

frase = input("Por favor, introduce una frase: ")

# Invertir la frase utilizando indexación inversa
frase_invertida = frase[::-1]

print(f"Frase invertida: \033[92m{frase[::-1]}\033[0m")
