"""
Escribir un programa que guarde en un diccionario
los precios de las frutas de la tabla, pregunte al
usuario por una fruta, un número de kilos y muestre
por pantalla el precio de ese número de kilos de
fruta. Si la fruta no está en el diccionario debe
mostrar un mensaje informando de ello.

10. Fruta             11. Precio
12. Banana            13. $450 kg
14. Manzana verde     15. $800 kg
16. Pera              17. $550 kg
18. Pomelo            19. $900 kg

"""

# Crear el diccionario de precios de frutas
precios_frutas = {
    "banana": 450,
    "manzana verde": 800,
    "pera": 550,
    "pomelo": 900
}

# Solicitar al usuario la fruta y la cantidad de kilogramos
fruta = input("Ingrese el nombre de la fruta: ").lower()

# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    kilogramos = float(input("Ingrese la cantidad de kilogramos: "))
    precio_total = precios_frutas[fruta] * kilogramos
    print(f"El precio total de {kilogramos} kg de {fruta} es: ${precio_total}")
else:
    print("La fruta ingresada no está en el diccionario de precios.")
