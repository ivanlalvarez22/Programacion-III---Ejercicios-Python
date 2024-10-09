"""
Escribir un programa que almacene el abecedario 
en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por 
pantalla la lista resultante.
"""

# consideraremos "a" como la posición 0.
abecedario = list("abcdefghijklmnñopqrstuvwxyz")

# Iteramos sobre la lista en pasos de -3 (de atrás hacia adelante)
for i in range(len(abecedario) - 3, 0, -3):
    # Eliminamos el elemento que ocupa la posición múltiplo de 3
    abecedario.pop(i)

print("Abecedario resultante:", abecedario)
