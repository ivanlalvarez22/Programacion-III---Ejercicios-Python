"""
Escribir una función que calcule el total de una factura tras 
aplicarle el IVA. La función debe recibir la cantidad sin IVA 
y el porcentaje de IVA a aplicar, y devolver el total de la 
factura. Si se invoca la función sin pasarle el porcentaje de
IVA, deberá aplicar un 21%.
"""


def calcular_iva(precio_factura, porcentaje_iva=21):
    return precio_factura * (1 + porcentaje_iva / 100)


print(calcular_iva(2000, 40))
print(calcular_iva(1000))
