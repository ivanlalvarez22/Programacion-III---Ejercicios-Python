"""
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla el número de veces que 
contiene cada vocal.
"""

palabra = input("Por favor, ingresa una palabra: ")

# Inicializar un diccionario para contar las vocales
conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Recorrer cada letra de la palabra
for letra in palabra:
    # Convertir la letra a minúscula para hacer coincidir con las vocales
    letra = letra.lower()
    # Verificar si la letra es una vocal y actualizar el conteo
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

for vocal, conteo in conteo_vocales.items():  # devuelve una vista de los pares clave-valor en el diccionario
    print(f"La vocal {vocal} aparece {conteo} veces en la palabra.")
