"""
Escribir un programa que pregunte al usuario por el número de 
horas trabajadas y el coste por hora. 
Después debe mostrar por consola la paga que le corresponde.
"""

horas_trabajadas = int(input("Ingrese el nro de horas trabajadas: "))
coste = float(input("Ingrese el coste: "))
paga = horas_trabajadas * coste
print(f"La paga es: ${paga}")
