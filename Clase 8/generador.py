"""
Crea un script llamado generador.py que cumpla las siguientes necesidades:

a. Debe incluir una función llamada leer_numero(). Esta función tomará 3 valores: ini,
fin y mensaje. El objetivo es leer por pantalla un número >= que ini y <= que fin.
Además, a la hora de hacer la lectura se mostrará en el input el mensaje enviado a
la función. Finalmente se devolverá el valor. Esta función tiene que devolver un
número, y tiene que repetirse hasta que el usuario no lo escriba bien (lo que incluye
cualquier valor que no sea un número del ini al fin).

b. Una vez la tengas creada, deberás crear una nueva función llamada generador, no
recibirá ningún parámetro. Dentro leerás dos números con la función
leer_numero():

i. El primer número será llamado números, deberá ser entre 1 y 20, ambos
incluidos, y se mostrará el mensaje ¿Cuantos números quieres generar?
[1-20]:

ii. El segundo número será llamado modo y requerirá un número entre 1 y 3,
ambos incluidos. El mensaje que mostrará será: ¿Cómo quieres
redondear los números? [1]Al alza [2]A la baja [3]Normal:.

c. Una vez sepas los números a generar y cómo redondearlos, tendrás que realizar lo
siguiente:

i. Generarás una lista de números aleatorios decimales entre 0 y 100 con
tantos números como el usuario haya indicado.

ii. A cada uno de esos números deberás redondearlos en función de lo que el
usuario ha especificado en el modo.

iii. Para cada número muestra durante el redondeo, el número normal y
después del redondeo.

d. Finalmente devolverás la lista de números redondeados.
"""

import random


def leer_numero(ini, fin, mensaje):
    """
    Lee un número desde la entrada estándar entre ini y fin,
    mostrando el mensaje dado, y devuelve el número leído.
    """
    while True:
        try:
            numero = int(input(mensaje))
            if ini <= numero <= fin:
                return numero
            else:
                print(f"Por favor, ingresa un número entre {ini} y {fin}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


def generador():
    """
    Genera una lista de números aleatorios redondeados según las preferencias del usuario.
    """
    # Leer la cantidad de números a generar
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")

    # Leer el modo de redondeo
    modo = leer_numero(
        1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    # Generar la lista de números aleatorios
    numeros_generados = [random.uniform(0, 100) for _ in range(numeros)]

    # Redondear los números según el modo especificado
    numeros_redondeados = []
    for numero in numeros_generados:
        if modo == 1:
            numero_redondeado = round(numero)
        elif modo == 2:
            numero_redondeado = int(numero)
        else:
            numero_redondeado = round(numero, 1)
        numeros_redondeados.append(numero_redondeado)

        print(f"Número original: {
              numero}, Número redondeado: {numero_redondeado}")

    return numeros_redondeados


if __name__ == "__main__":
    generador()
