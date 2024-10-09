"""
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla el número de veces que 
contiene cada vocal.
"""

palabra = input("Ingrese una palabra: ")

conteo_vocales = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}

for letra in palabra:
    letra.lower()
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

for vocal, conteo in conteo_vocales.items():
    print(f"La vocal {vocal} aparece {conteo} veces en la palabra {palabra}")
