"""
Crea un sistema de reserva de hotel con clases “Hotel", "Habitación" y
"Reserva". Un objeto "Hotel" puede tener una lista de objetos "Habitación",
y un objeto "Reserva" se relaciona con un objeto "Habitación". Implementar
métodos para buscar habitaciones disponibles, realizar reservas y mostrar
detalles de las reservas realizadas. Definir como atributo privado el estado
de la habitación y definir los métodos adecuados para leerlo o bien
establecer un nuevo valor.
"""
from datetime import datetime


class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.__estado = "Disponible"  # Estado privado: "Disponible" u "Ocupada"

    # Método para leer el estado de la habitación
    def obtener_estado(self):
        return self.__estado

    # Método para establecer un nuevo valor al estado de la habitación
    def establecer_estado(self, estado):
        if estado in ["Disponible", "Ocupada"]:
            self.__estado = estado

    def __str__(self):
        return f"Habitación {self.numero}: {self.tipo} - ${self.precio} - {self.obtener_estado()}"


class Reserva:
    def __init__(self, habitacion, huesped, fecha_inicio, fecha_fin):
        self.habitacion = habitacion
        self.huesped = huesped
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y')
        self.fecha_fin = datetime.strptime(fecha_fin, '%d/%m/%Y')
        habitacion.establecer_estado("Ocupada")

    def __str__(self):
        return (f"Reserva de: {self.huesped} en: {self.habitacion} "
                f"desde: {self.fecha_inicio.strftime('%d/%m/%Y')} "
                f"hasta: {self.fecha_fin.strftime('%d/%m/%Y')}")


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def buscar_habitaciones_disponibles(self):
        disponibles = [
            hab for hab in self.habitaciones if hab.obtener_estado() == "Disponible"]
        return disponibles

    def realizar_reserva(self, habitacion_numero, huesped, fecha_inicio, fecha_fin):
        habitacion = next(
            (hab for hab in self.habitaciones if hab.numero == habitacion_numero), None)
        if habitacion and habitacion.obtener_estado() == "Disponible":
            reserva = Reserva(habitacion, huesped, fecha_inicio, fecha_fin)
            self.reservas.append(reserva)
            return reserva
        else:
            return None

    def mostrar_reservas(self):
        return "\n".join(str(reserva) for reserva in self.reservas)

# Ejemplo de uso


def menu():
    hotel = Hotel("Hotel ITSE")

    # Agregar algunas habitaciones por defecto
    hotel.agregar_habitacion(Habitacion(101, "Simple", 100))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 150))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 200))

    while True:
        print("\n--- Menú del Hotel ---")
        print("1. Ver habitaciones disponibles")
        print("2. Realizar una reserva")
        print("3. Mostrar todas las reservas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\n\033[92mHabitaciones disponibles:\033[0m")
            disponibles = hotel.buscar_habitaciones_disponibles()
            if disponibles:
                for hab in disponibles:
                    print(hab)
            else:
                print("No hay habitaciones disponibles.")

        elif opcion == '2':
            try:
                numero = int(input("Ingrese el número de la habitación: "))
                huesped = input("Ingrese el nombre del huésped: ")
                fecha_inicio = input(
                    "Ingrese la fecha de inicio (DD/MM/YYYY): ")
                fecha_fin = input("Ingrese la fecha de fin (DD/MM/YYYY): ")

                reserva = hotel.realizar_reserva(
                    numero, huesped, fecha_inicio, fecha_fin)
                if reserva:
                    print("\n\033[92mReserva realizada con éxito:\033[0m")
                    print(reserva)
                else:
                    print(
                        "\nNo se pudo realizar la reserva. Verifique la disponibilidad de la habitación.")
            except ValueError:
                print("Entrada no válida. Intente nuevamente.")

        elif opcion == '3':
            print("\nDetalles de las reservas:")
            reservas = hotel.mostrar_reservas()
            if reservas:
                print(reservas)
            else:
                print("No hay reservas.")

        elif opcion == '0':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

        input("Presione ENTER para continuar...")


menu()
