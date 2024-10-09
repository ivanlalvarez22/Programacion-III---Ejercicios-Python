"""
Una juguetería tiene mucho éxito en dos de sus productos: 
payasos y muñecas. Suele hacer venta por correo y la 
empresa de logística les cobra por peso de cada paquete así 
que deben calcular el peso de los payasos y muñecas que 
saldrán en cada paquete a demanda. Cada payaso pesa 112g 
y cada muñeca 75 g. Escribir un programa que lea el número 
de payasos y muñecas vendidos en el último pedido y calcule 
el peso total del paquete que será enviado.
"""

PESO_PAYASO = 112
PESO_MUNIECA = 75

num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muniecas = int(input("Ingrese el número de muñecas vendidas: "))

peso_total = (num_payasos * PESO_PAYASO) + (num_muniecas * PESO_MUNIECA)

print(f"El peso total del paquete que será enviado es: {peso_total} gramos.")
