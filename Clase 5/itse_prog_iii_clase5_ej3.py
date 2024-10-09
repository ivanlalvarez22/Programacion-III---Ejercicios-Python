"""
Realizar una clase que administre una agenda.
Se debe almacenar para cada contacto el nombre, el teléfono
y el email. Además, deberá mostrar un menú con las
siguientes opciones

* Añadir contacto
* Lista de contactos
* Buscar contacto
* Editar contacto
* Cerrar agenda
"""

import re


class Agenda:
    def __init__(self) -> None:
        self.contactos = []

    def validar_nombre(self, nombre):
        return bool(nombre.strip())

    def validar_telefono(self, telefono):
        return bool(re.match(r'^\d{7,}$', telefono))

    def validar_email(self, email):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

    def agregar_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        while not self.validar_nombre(nombre):
            nombre = input(
                "Nombre inválido. Por favor, ingrese un nombre válido: ")

        telefono = input("Ingrese el teléfono del contacto: ")
        while not self.validar_telefono(telefono):
            telefono = input(
                "Teléfono inválido. Por favor, ingrese un teléfono válido: ")

        email = input("Ingrese el email del contacto: ")
        while not self.validar_email(email):
            email = input(
                "Email inválido. Por favor, ingrese un email válido: ")

        self.contactos.append(
            {"nombre": nombre, "telefono": telefono, "email": email})
        print("Contacto añadido con éxito.")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            # \033[92m establece el color verde
            print("\033[92m--- Lista de Contactos ---\033[0m")
            for contacto in self.contactos:
                print("\033[92mNombre:\033[0m", contacto["nombre"])
                print("\033[92mTeléfono:\033[0m", contacto["telefono"])
                print("\033[92mEmail:\033[0m", contacto["email"])
                print("\033[92m-------------------------\033[0m")

    def buscar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto["nombre"].lower() == nombre.lower():
                print("\033[92mContacto encontrado:\033[0m")
                print("\033[92mNombre:\033[0m", contacto["nombre"])
                print("\033[92mTeléfono:\033[0m", contacto["telefono"])
                print("\033[92mEmail:\033[0m", contacto["email"])
                encontrado = True
                break
        if not encontrado:
            print("\033[91mEl contacto no se encuentra en la agenda.\033[0m")

    def editar_contacto(self):
        nombre = input("Ingrese el nombre del contacto a editar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto["nombre"] == nombre:
                print("Contacto encontrado:")
                print("Nombre:", contacto["nombre"])
                print("Teléfono:", contacto["telefono"])
                print("Email:", contacto["email"])
                nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
                nuevo_telefono = input(
                    "Ingrese el nuevo teléfono del contacto: ")
                nuevo_email = input("Ingrese el nuevo email del contacto: ")
                contacto["nombre"] = nuevo_nombre
                contacto["telefono"] = nuevo_telefono
                contacto["email"] = nuevo_email
                print("Contacto editado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print("El contacto no se encuentra en la agenda.")


def main():
    agenda = Agenda()
    op = -1
    while op != 0:

        print("\n--- Menú de Agenda ---")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("0. Cerrar agenda")

        op = int(input("Seleccione una opción: "))

        if op == 1:
            agenda.agregar_contacto()
        elif op == 2:
            agenda.listar_contactos()
        elif op == 3:
            agenda.buscar_contacto()
        elif op == 4:
            agenda.editar_contacto()
        elif op == 0:
            print("Cerrando agenda...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        input("\nPresione ENTER para continuar: ")


if __name__ == "__main__":
    main()
