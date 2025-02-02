"""
Una inmobiliaria de una ciudad maneja una lista de inmuebles como 
la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año':
1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},{'año': 2005,
'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},{'año': 2015,
'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en 
función de un presupuesto dado. La función recibirá como entrada 
la lista de inmuebles y un precio, y devolverá otra lista con 
los inmuebles cuyo precio sea menor o igual que el dado. Los 
inmuebles de la lista que se devuelva deben incorporar un nuevo 
par a cada diccionario con el precio del inmueble, donde el precio 
de un inmueble se calcula con la siguiente fórmula en función de 
la zona:
• Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje *
15000) * (1-antiguedad/100)
• Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje *
15000) * (1-antiguedad/100) * 1.5
"""

import datetime


def buscar_inmuebles(lista_inmuebles, presupuesto):
    inmuebles_encontrados = []
    for inmueb in lista_inmuebles:
        precio = calcular_precio(inmueb)
        if precio <= presupuesto:
            inmueble_con_precio = inmueb.copy()
            inmueble_con_precio['precio'] = precio
            inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados


def calcular_precio(inmueble):
    precio_base = inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + \
        inmueble['garaje'] * 15000
    antiguedad = datetime.datetime.now().year - inmueble['año']  # año actual
    if inmueble['zona'] == 'A':
        precio = precio_base * (1 - antiguedad / 100)
    else:
        precio = precio_base * (1 - antiguedad / 100) * 1.5
    return precio


# Ejemplo de uso:
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

presup = int(input("Por favor, ingrese el presupuesto: "))

inmuebles_disponibles = buscar_inmuebles(inmuebles, presup)
for propiedad in inmuebles_disponibles:
    print(propiedad)
