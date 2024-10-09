"""
Escribir una función reciba una lista de notas y devuelva 
la lista de calificaciones correspondientes a esas notas.
"""

lista_notas = [10, 11, 5, -1, 6, 8, 9, 2, 1, 0, 3]


def asignar_etiqueta(nota):
    """
    Etiqueta según puntaje dado.
    """
    if nota >= 6 and nota <= 10:
        return "Aprobado"
    elif nota >= 0 and nota <= 5:
        return "Desaprobado"
    else:
        return "Nota inválida"


resultados = list(map(asignar_etiqueta, lista_notas))

print(resultados)
