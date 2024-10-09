"""
Escribir un programa que pregunte al usuario su 
nombre, edad, dirección y teléfono y lo guarde 
en un diccionario. Después debe mostrar por 
pantalla el mensaje <nombre> tiene 
<edad> años, vive en <dirección> y su número 
de teléfono es <teléfono>.
"""

nombre = input("Por favor, ingrese su nombre: ")
edad = input("Por favor, ingrese su edad: ")
direccion = input("Por favor, ingrese su dirección: ")
telefono = input("Por favor, ingrese su número de teléfono: ")

# Crear un diccionario con la información ingresada por el usuario
datos_usuario = {
    'nombre': nombre,
    'edad': edad,
    'dirección': direccion,
    'teléfono': telefono
}

print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {
      datos_usuario['dirección']} y su número de teléfono es {datos_usuario['teléfono']}.")
