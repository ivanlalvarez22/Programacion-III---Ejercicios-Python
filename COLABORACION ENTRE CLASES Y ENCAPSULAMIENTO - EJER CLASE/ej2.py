"""
Define una clase Cliente que almacena un código de cliente y un nombre.
En la clase Cliente define un atributo de clase de tipo lista que almacene
todos los clientes con sus cuentas corrientes suspendidas. Imprimir por
pantalla todos los datos de clientes y el estado en que se encuentra su
cuenta corriente. Definir como atributo privado el DNI y número de cuenta.
Definir los métodos adecuados para leerlo o bien establecer un nuevo
valor.
"""


class Cliente:
    # Atributo de clase para almacenar clientes con cuentas suspendidas
    clientes_suspendidos = []

    def __init__(self, codigo_cliente, nombre, dni, numero_cuenta):
        self.codigo_cliente = codigo_cliente
        self.nombre = nombre
        self.__dni = dni  # Atributo privado
        self.__numero_cuenta = numero_cuenta  # Atributo privado
        self.cuenta_suspendida = False  # Estado de la cuenta corriente

    def obtener_dni(self):
        return self.__dni

    def establecer_dni(self, nuevo_dni):
        self.__dni = nuevo_dni

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

    def establecer_numero_cuenta(self, nuevo_numero_cuenta):
        self.__numero_cuenta = nuevo_numero_cuenta

    def suspender_cuenta(self):
        self.cuenta_suspendida = True
        Cliente.clientes_suspendidos.append(self)

    def activar_cuenta(self):
        self.cuenta_suspendida = False
        if self in Cliente.clientes_suspendidos:
            Cliente.clientes_suspendidos.remove(self)

    def imprimir_datos(self):
        estado_cuenta = "Suspendida" if self.cuenta_suspendida else "Activa"
        print(f"Código Cliente: {self.codigo_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.obtener_dni()}")
        print(f"Número de Cuenta: {self.obtener_numero_cuenta()}")
        print(f"Estado de la Cuenta: {estado_cuenta}")


cliente1 = Cliente("001", "Juan Perez", "12345678A", "1001")
cliente2 = Cliente("002", "María López", "87654321B", "1002")
cliente3 = Cliente("003", "Pedro Gómez", "11223344C", "1003")

cliente1.suspender_cuenta()
cliente3.suspender_cuenta()

print("Datos de los clientes:")
cliente1.imprimir_datos()
print()
cliente2.imprimir_datos()
print()
cliente3.imprimir_datos()

print("\nClientes con cuentas suspendidas:")
for cliente in Cliente.clientes_suspendidos:
    print(f"Código Cliente: {
          cliente.codigo_cliente}, Nombre: {cliente.nombre}")
