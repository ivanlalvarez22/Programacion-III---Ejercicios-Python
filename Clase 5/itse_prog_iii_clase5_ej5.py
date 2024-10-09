"""
Modelar un sanatorio donde los pacientes tienen los 
siguientes atributos: dni, obra social, nombre, apellido, 
número habitación, estado (habitación común, terapia intermedia, 
terapia intensiva). Implementar métodos que permitan ver 
los datos de los pacientes, ver su estado y cambiar de estado.
"""


class Paciente:
    def __init__(self, dni, obra_social, nombre, apellido, num_habitacion, estado):
        self.dni = dni
        self.obra_social = obra_social
        self.nombre = nombre
        self.apellido = apellido
        self.num_habitacion = num_habitacion
        self.estado = estado

    def ver_datos_paciente(self):
        return f"\033[92mDNI: {self.dni}\nObra Social: {self.obra_social}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNúmero de Habitación: {self.num_habitacion}\nEstado: {self.estado}\033[0m"

    def ver_estado(self):
        return f"\033[92mEstado actual del paciente {self.nombre} {self.apellido}: {self.estado}\033[0m"

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado del paciente {self.nombre} {
              self.apellido} ha sido actualizado a: {self.estado}")


def main():
    pacientes = []
    op = -1

    opciones_estados = {
        "1": "habitación común",
        "2": "terapia intermedia",
        "3": "terapia intensiva"
    }

    while op != 0:

        print("\n--- Menú del Sanatorio ---")
        print("1. Registrar paciente")
        print("2. Ver datos de paciente")
        print("3. Ver estado de paciente")
        print("4. Cambiar estado de paciente")
        print("5. Mostrar todos los pacientes")
        print("0. Cerrar programa")

        op = input("Seleccione una opción: ")

        if op == "1":
            dni = input("Ingrese DNI del paciente: ")
            obra_social = input("Ingrese obra social del paciente: ")
            nombre = input("Ingrese nombre del paciente: ")
            apellido = input("Ingrese apellido del paciente: ")
            num_habitacion = input(
                "Ingrese número de habitación del paciente: ")
            num_habitacion = num_habitacion.zfill(3)  # Ajustar a 3 dígitos
            estado_opcion = ""
            while estado_opcion not in opciones_estados:
                print("Ingrese el estado del paciente:")
                for key, value in opciones_estados.items():
                    print(f"{key}. {value}")
                estado_opcion = input("Seleccione una opción de estado: ")
                if estado_opcion not in opciones_estados:
                    print("\033[91mIngrese un nro de estado válido.\033[0m")
                    input("Por favor, presione ENTER para continuar...")
            estado = opciones_estados[estado_opcion]
            paciente = Paciente(dni, obra_social, nombre,
                                apellido, num_habitacion, estado)
            pacientes.append(paciente)
            print("Paciente registrado con éxito.")

        elif op == "2":
            dni = input("Ingrese DNI del paciente: ")
            paciente_encontrado = False
            for paciente in pacientes:
                if paciente.dni == dni:
                    print(paciente.ver_datos_paciente())
                    paciente_encontrado = True
                    break
            if not paciente_encontrado:
                print("El paciente no está registrado.")

        elif op == "3":
            dni = input("Ingrese DNI del paciente: ")
            paciente_encontrado = False
            for paciente in pacientes:
                if paciente.dni == dni:
                    print(paciente.ver_estado())
                    paciente_encontrado = True
                    break
            if not paciente_encontrado:
                print("El paciente no está registrado.")

        elif op == "4":
            dni = input("Ingrese DNI del paciente: ")
            paciente_encontrado = False
            for paciente in pacientes:
                if paciente.dni == dni:
                    estado_opcion = ""
                    while estado_opcion not in opciones_estados:
                        print("Opciones de estados disponibles:")
                        for key, value in opciones_estados.items():
                            print(f"{key}. {value}")
                        estado_opcion = input(
                            "Seleccione una opción de estado: ")
                        if estado_opcion not in opciones_estados:
                            print(
                                "\033[91mIngrese un nro de estado válido.\033[0m")
                            input("Por favor, presione ENTER para continuar...")
                    nuevo_estado = opciones_estados[estado_opcion]
                    paciente.cambiar_estado(nuevo_estado)
                    paciente_encontrado = True
                    break
            if not paciente_encontrado:
                print("El paciente no está registrado.")

        elif op == "5":
            if pacientes:
                print("\n--- Lista de Pacientes Registrados ---")
                for paciente in pacientes:
                    print(paciente.ver_datos_paciente())
                    print(" ------------------ ")
            else:
                print("No hay pacientes registrados.")

        elif op == "0":
            print("Cerrando programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        input("\nPresione ENTER para continuar: ")


if __name__ == "__main__":
    main()
