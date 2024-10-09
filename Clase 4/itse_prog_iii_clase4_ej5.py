"""
Escribir una función que convierta un número decimal 
en binario y otra que convierta un número binario 
en decimal.
"""


def es_binario(numero):
    """
    Validar número binario
    """
    for bit in numero:
        if bit not in '01':
            return False
    return True


def decimal_a_binario(numero):
    """
    Recibe un valor de tipo int
    """
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario


def binario_a_decimal(binario):
    """
    Recibe un valor de tipo string
    """
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        if binario[i] == '1':
            decimal += 2**(longitud - 1 - i)
    return decimal


# Ejemplos de uso:
numero_decimal = int(input("Ingrese un número del sistema decimal: "))
numero_binario = input("Ingrese un número del sistema binario: ")
while not es_binario(numero_binario):
    numero_binario = input("Ingrese un número binario válido: ")

resultado_binario = decimal_a_binario(numero_decimal)
resultado_decimal = binario_a_decimal(numero_binario)

print(f"Número decimal {numero_decimal} en binario: {resultado_binario}")
print(f"Número binario {numero_binario} en decimal: {resultado_decimal}")
