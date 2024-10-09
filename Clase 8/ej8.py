"""
  Diseñe un sistema de lotería en donde se solicita al usuario que construya un diccionario
donde la clave es el número comprado por la persona y el valor es el nombre de la misma.
La lotería entrega 5 premios:

o 1 premio: Un viaje a Turquía con todo pago
o 2 premio: auto
o 3 premio: una motocicleta
o 4 premio: una notebook
o 5 premio: una bicicleta

  Genere 5 números aleatorios para definir los ganadores teniendo en cuenta que el número
comprado tiene tres dígitos. Por ejemplo: 003, 050, 850.

Finalmente muéstrelos nombres de los ganadores y los premios ganados
"""


import random


def recoger_participantes():
    participantes = {}
    while True:
        numero = input(
            "Ingrese el número comprado (tres dígitos, 000-999): ").zfill(3)
        if numero.isdigit() and 0 <= int(numero) <= 999:
            if numero not in participantes:
                nombre = input(f"Ingrese su nombre para el número {numero}: ")
                participantes[numero] = nombre
            else:
                print("Ese número ya ha sido comprado. Intente con otro número.")
        else:
            print("Número inválido. Intente nuevamente.")

        continuar = input("¿Desea ingresar otro participante? (s/n): ").lower()
        if continuar != 's':
            break

    return participantes


def sortear_ganadores(participantes):
    premios = {
        1: "Un viaje a Turquía con todo pago",
        2: "Un auto",
        3: "Una motocicleta",
        4: "Una notebook",
        5: "Una bicicleta"
    }

    if len(participantes) < 5:
        print("No hay suficientes participantes para realizar el sorteo.")
        return

    numeros_participantes = list(participantes.keys())
    ganadores = random.sample(numeros_participantes, 5)

    print("\n¡Los ganadores son!")
    for i, ganador in enumerate(ganadores, start=1):
        print(f"{participantes[ganador]} ha ganado: {premios[i]}")


def loteria():
    participantes = recoger_participantes()
    sortear_ganadores(participantes)


if __name__ == "__main__":
    loteria()
