"""
El fichero cotización.csv contiene las cotizaciones de las empresas del IBEX35 con
las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción
al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), Mínimo
(precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de
bolsa), Efectivo (capitalización al cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con
los datos del fichero por columnas.

Construir una función que reciba el diccionario devuelto por la función anterior y cree
un fichero en formato csv con el mínimo, el máximo y la media de dada columna
"""


import csv

# Función para leer el archivo CSV y convertirlo en un diccionario


def leer_cotizaciones(fichero):
    with open(fichero, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        datos_por_columnas = {}
        for row in reader:
            for column, value in row.items():
                if column not in datos_por_columnas:
                    datos_por_columnas[column] = []
                datos_por_columnas[column].append(value)
    return datos_por_columnas

# Función para calcular el mínimo, máximo y promedio de cada columna y guardar estos datos en un nuevo archivo CSV


def calcular_estadisticas_y_guardar(datos, fichero_salida):
    estadisticas = {}

    for columna, valores in datos.items():
        if columna == "Nombre":
            continue

        valores_numericos = list(map(float, valores))
        minimo = min(valores_numericos)
        maximo = max(valores_numericos)
        promedio = sum(valores_numericos) / len(valores_numericos)

        estadisticas[columna] = {
            "Mínimo": minimo,
            "Máximo": maximo,
            "Promedio": promedio
        }

    with open(fichero_salida, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Columna", "Mínimo", "Máximo", "Promedio"])

        for columna, stats in estadisticas.items():
            writer.writerow([columna, stats["Mínimo"],
                            stats["Máximo"], stats["Promedio"]])


# Ejemplo de uso
if __name__ == "__main__":
    fichero_entrada = 'cotizacion.csv'
    nombre_fichero_salida = 'estadisticas.csv'

    # Leer cotizaciones y convertir a diccionario
    datos_diccionario = leer_cotizaciones(fichero_entrada)

    # Calcular estadísticas y guardar en nuevo archivo CSV
    calcular_estadisticas_y_guardar(datos_diccionario, nombre_fichero_salida)
