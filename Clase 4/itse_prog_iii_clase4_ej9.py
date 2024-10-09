"""
Escribir una función que reciba un diccionario con las asignaturas 
y las notas de un alumno y devuelva otro diccionario con las 
asignaturas en mayúsculas y las calificaciones correspondientes 
a las notas aprobadas.
"""


def evaluar_asignaturas(notas):
    calificaciones = {}
    for asignatura, nota in notas.items():
        if nota >= 6:
            calificaciones[asignatura.upper()] = "Aprobado"
        else:
            calificaciones[asignatura.upper()] = "Desaprobado"
    return calificaciones


# Ejemplo de uso:
notas_alumno = {"Matemáticas": 8, "Ciencias": 5, "Historia": 7, "Inglés": 6}
calificaciones_asignaturas = evaluar_asignaturas(notas_alumno)
print(calificaciones_asignaturas)
