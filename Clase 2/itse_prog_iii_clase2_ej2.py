"""
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña e imprima por pantalla si la contraseña 
introducida por el usuario coincide con la guardada en 
la variable sin tener en cuenta mayúsculas y minúsculas.
"""

contrasenia_guardada = "1234"
contrasenia_ingresada = input("Ingrese la contraseña: ")

if contrasenia_guardada == contrasenia_ingresada:
    print("\033[92m¡Contraseña correcta!\033[0m")
else:
    print("\033[91m¡Contraseña incorrecta!\033[0m")
