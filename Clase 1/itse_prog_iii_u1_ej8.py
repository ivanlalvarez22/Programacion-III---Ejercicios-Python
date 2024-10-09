"""
Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión.
"""

# Pedir al usuario la cantidad a invertir, el interés anual y el número de años
cantidad = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (en porcentaje): "))
num_anios = int(input("Ingrese el número de años: "))

# Convertir el interés anual de porcentaje a decimal
# Calcular el capital obtenido en la inversión considerando el interés compuesto
interes_decimal = interes_anual / 100
capital_obtenido = cantidad * (1 + interes_decimal) ** num_anios

# Mostrar el capital obtenido por pantalla
print(f"El capital obtenido después de {num_anios} será: ${capital_obtenido:.2f}")
