"""
Escribir un programa que almacene las asignaturas 
de un curso en una lista, pregunte al usuario la 
nota que ha sacado en cada asignatura, y después 
las muestre por pantalla con el mensaje En 
<asignatura> has sacado <nota> donde 
<asignatura> es cada una de las asignaturas 
de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario
"""

asignaturas = ["Matemáticas", "Física", "Química", "Lengua", "Inglés"]

# Lista para almacenar las notas
notas = []

# Pedir al usuario la nota para cada asignatura
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    while nota < 0 or nota > 10:  # validar nota
        nota = float(input(f"Ingrese una nota válida de {
                     asignatura} (0 - 10): "))
    notas.append(nota)

# Mostrar las asignaturas y sus notas por pantalla
print("Notas del curso:")
for i, asignatura in enumerate(asignaturas):
    print(f"En {asignatura} has sacado {notas[i]}")
