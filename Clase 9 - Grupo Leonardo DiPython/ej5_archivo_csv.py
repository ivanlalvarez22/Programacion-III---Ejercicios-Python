"""
El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso
se realizaron dos exámenes parciales de teoría y un examen de prácticas. Los
alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo
en la al final del curso (convocatoria ordinaria). Escribir un programa que contenga
las siguientes funciones:

Una función que reciba el fichero de calificaciones y devuelva una lista de
diccionarios, donde cada diccionario contiene la información de los exámenes y la
asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

Una función que reciba una lista de diccionarios como la que devuelve la función
anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso
de cada parcial de teoría en la nota final es de un 30% mientras que el peso del
examen de prácticas es de un 40%.

Una función que reciba una lista de diccionarios como la que devuelve la función
anterior y devuelva dos listas, una con los alumnos aprobados y otra con los
alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual
que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y
la nota final mayor o igual que 5.

* Los archivos calificaciones.scv y cotización.scv se encuentran adjunto a esta tarea
"""


import csv
import os


def leer_calificaciones(archivo):
    """
    Lee el archivo de calificaciones y devuelve una lista de diccionarios
    donde cada diccionario contiene la información de un alumno.
    """
    if not os.path.exists(archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {archivo}")

    with open(archivo, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        lista_alumnos = [row for row in reader]

    # Ordenar la lista de alumnos por apellidos
    lista_alumnos.sort(key=lambda x: x['apellidos'])

    return lista_alumnos


def calcular_nota_final(alumnos):
    """
    Añade a cada diccionario de la lista de alumnos un nuevo par con la nota final
    del curso, basada en los pesos dados para los exámenes parciales y prácticas.
    """
    for alumno in alumnos:
        try:
            parcial1 = float(alumno['parcial1']) if alumno['parcial1'] else 0.0
            parcial2 = float(alumno['parcial2']) if alumno['parcial2'] else 0.0
            practicas = float(alumno['practicas']
                              ) if alumno['practicas'] else 0.0

            parcial1_ordinario = float(
                alumno['parcial1_ordinario']) if alumno['parcial1_ordinario'] else parcial1
            parcial2_ordinario = float(
                alumno['parcial2_ordinario']) if alumno['parcial2_ordinario'] else parcial2
            practicas_ordinario = float(
                alumno['practicas_ordinario']) if alumno['practicas_ordinario'] else practicas

            mejor_parcial1 = max(parcial1, parcial1_ordinario)
            mejor_parcial2 = max(parcial2, parcial2_ordinario)
            mejor_practicas = max(practicas, practicas_ordinario)

            nota_final = (mejor_parcial1 * 0.3) + \
                (mejor_parcial2 * 0.3) + (mejor_practicas * 0.4)
            alumno['nota_final'] = nota_final
        except ValueError as e:
            print(f"Error en los datos del alumno {alumno['apellidos']}: {e}")
            alumno['nota_final'] = 0.0


def clasificar_alumnos(alumnos):
    """
    Clasifica a los alumnos en dos listas: aprobados y suspendidos.
    """
    aprobados = []
    suspendidos = []

    for alumno in alumnos:
        try:
            asistencia = float(alumno['asistencia']
                               ) if alumno['asistencia'] else 0.0
            parcial1 = float(alumno['parcial1']) if alumno['parcial1'] else 0.0
            parcial2 = float(alumno['parcial2']) if alumno['parcial2'] else 0.0
            practicas = float(alumno['practicas']
                              ) if alumno['practicas'] else 0.0
            nota_final = alumno['nota_final']

            if (asistencia >= 75 and parcial1 >= 4 and parcial2 >= 4 and practicas >= 4 and nota_final >= 5):
                aprobados.append(alumno)
            else:
                suspendidos.append(alumno)
        except ValueError as e:
            print(f"Error en los datos del alumno {alumno['apellidos']}: {e}")
            suspendidos.append(alumno)

    return aprobados, suspendidos


def main():
    archivo = 'calificaciones.csv'

    try:
        lista_alumnos = leer_calificaciones(archivo)
        calcular_nota_final(lista_alumnos)
        aprobados, suspendidos = clasificar_alumnos(lista_alumnos)

        print("Alumnos aprobados:")
        for alumno in aprobados:
            print(alumno)

        print("\nAlumnos suspendidos:")
        for alumno in suspendidos:
            print(alumno)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
