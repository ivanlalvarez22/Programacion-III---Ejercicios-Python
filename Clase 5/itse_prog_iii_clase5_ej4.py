"""
Realizar un programa que modele una cuenta corriente. 
Cada cliente se identifica con un nro. de cuenta, CBU, nombre y 
monto total. Las operaciones permitidas para la cuenta son: 
ver saldo, ver datos de la cuenta, realizar extracciones y realizar
depósitos
"""


class CuentaCorriente:
    def __init__(self, numero_cuenta, cbu, nombre_cliente, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.cbu = cbu
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo_inicial

    def ver_saldo(self):
        return f"\033[92m${self.saldo}\033[0m"

    def ver_datos_cuenta(self):
        return f"\033[92mNúmero de cuenta: {self.numero_cuenta}\nCBU: {self.cbu}\nNombre del cliente: {self.nombre_cliente}\033[0m"

    def realizar_deposito(self, monto):
        if monto > 0:
            self.saldo += monto
            print("Depósito realizado exitosamente")
            return True
        else:
            print("El monto del depósito debe ser mayor que cero.")
            return False

    def realizar_extraccion(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print("Extracción realizada exitosamente")
            return True
        else:
            print("Monto inválido o saldo insuficiente para realizar la extracción.")
            return False


def main():
    cuentas = []
    op = -1
    while op != 0:

        print("\n--- Menú de Cuentas Corrientes ---")
        print("1. Crear cuenta corriente")
        print("2. Ver datos de cuenta")
        print("3. Ver saldo")
        print("4. Realizar depósito")
        print("5. Realizar extracción")
        print("0. Cerrar programa")

        op = int(input("Seleccione una opción: "))

        if op == 1:
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cbu = input("Ingrese el CBU: ")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cuenta = CuentaCorriente(
                numero_cuenta, cbu, nombre_cliente, saldo_inicial)
            cuentas.append(cuenta)
            print("Cuenta corriente creada con éxito.")

        elif op == 2:
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cuenta_encontrada = False
            for cuenta in cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    print(cuenta.ver_datos_cuenta())
                    cuenta_encontrada = True
                    break
            if not cuenta_encontrada:
                print("La cuenta no existe.")

        elif op == 3:
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cuenta_encontrada = False
            for cuenta in cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    print("Saldo actual:", cuenta.ver_saldo())
                    cuenta_encontrada = True
                    break
            if not cuenta_encontrada:
                print("La cuenta no existe.")

        elif op == 4:
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cuenta_encontrada = False
            for cuenta in cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    monto = float(input("Ingrese el monto del depósito: "))
                    cuenta.realizar_deposito(monto)
                    cuenta_encontrada = True
                    break
            if not cuenta_encontrada:
                print("La cuenta no existe.")

        elif op == 5:
            numero_cuenta = input("Ingrese el número de cuenta: ")
            cuenta_encontrada = False
            for cuenta in cuentas:
                if cuenta.numero_cuenta == numero_cuenta:
                    monto = float(input("Ingrese el monto de la extracción: "))
                    cuenta.realizar_extraccion(monto)
                    cuenta_encontrada = True
                    break
            if not cuenta_encontrada:
                print("La cuenta no existe.")

        elif op == 0:
            print("Cerrando programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

        input("\nPresione ENTER para continuar: ")


if __name__ == "__main__":
    main()
