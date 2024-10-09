"""
Escribir un programa que guarde en una variable 
el diccionario {'Euro':'€', 'Dollar':'$', 
'Yen':'¥'}, pregunte al usuario por una divisa 
y muestre su símbolo o un mensaje de aviso si 
la divisa no está en el diccionario.
"""

divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa = input("Ingrese una divisa (Euro - Dollar - Yen): ")

print(divisa)
if divisa in divisas:
    print(f"El símbolo de {divisa} es {divisas[divisa]}.")
else:
    print("La divisa ingresada no está en el diccionario.")
