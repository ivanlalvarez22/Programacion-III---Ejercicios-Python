"""
Escribir un programa que almacene las asignaturas 
del 3 cuatrimestre del ITSE en una lista y la 
muestre por pantalla.
"""

asignaturas = ["Programación III", "Base de Datos II", "Práctica Profesionalizante II",
               "Ingeniería del Software II", "Sistemas Operativos II", "Estadística"]

for asignatura in asignaturas:
    print(f"\033[92m{asignatura}\033[0m")
