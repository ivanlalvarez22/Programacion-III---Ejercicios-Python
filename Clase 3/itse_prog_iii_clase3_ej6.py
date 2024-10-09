"""
Escribir un programa que almacene las asignaturas
de un curso (por ejemplo, Matemáticas, Física,
Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en
cada asignatura y elimine de la lista las
asignaturas aprobadas. Al final el programa debe
mostrar por pantalla las asignaturas que el
usuario tiene que repetir.
"""

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Lista para almacenar las asignaturas a repetir
asignaturas_a_repetir = []

# Pedir al usuario la nota para cada asignatura y eliminar las aprobadas
# Usamos [:] para hacer una copia de la lista
for asignatura in asignaturas[:]:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    if nota >= 6.0:
        asignaturas.remove(asignatura)
    else:
        asignaturas_a_repetir.append(asignatura)

print("Asignaturas a repetir:")
for asignatura in asignaturas_a_repetir:
    print(asignatura)


# nota linea 19:
# Cuando iteras directamente sobre una lista y la
# modificas (como al eliminar elementos), puedes
# encontrarte con comportamientos inesperados, ya
# que la longitud de la lista cambia dinámicamente
# mientras iteras sobre ella. Esto puede llevar a
# que se salten elementos o a bucles infinitos.
# Al hacer una copia de la lista usando
# asignaturas[:], estás iterando sobre una copia
# de la lista original, lo que significa que la
# lista original permanece intacta mientras la
# iteras y haces modificaciones en la copia.
# Esto evita problemas potenciales al modificar
# la lista durante la iteración.
