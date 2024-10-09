"""
Los teléfonos de una empresa tienen el siguiente 
formato prefijo-9-codigo de área-extensión-número 
donde el prefijo es el código del país +n 34, y 
la extensión tiene dos dígitos (15) y el código 
de area (385). Escribir un programa que pregunte 
por un número de teléfono con este formato y 
muestre por pantalla el número de teléfono sin 
el prefijo sin el 9 y sin extensión.
"""

telefono = input(
    "Por favor, ingrese el número de teléfono con el formato prefijo-9-codigo de área-extensión-número: ")

# Dividir el número de teléfono en partes utilizando "-" como separador
partes = telefono.split("-")

# Seleccionar solo las partes relevantes (código de área y número)
codigo_area = partes[2]
numero = partes[-1]

# Mostrar el número de teléfono sin el prefijo, el 9 y la extensión
print("Número de teléfono sin prefijo, sin el 9 y sin extensión:",
      codigo_area + "-" + numero)
