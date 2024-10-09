"""
Crea un sistema de correo electrónico con las clases "Usuario", "Bandeja
de entrada" y "Mensaje". Un objeto "Usuario" puede tener una bandeja de
entrada que contenga una lista de objetos "Mensaje". Puedes implementar
métodos para enviar y recibir mensajes, así como para filtrar mensajes por
categorías como leídos, no leídos, enviados, etc. Definir como atributo
privado el atributo correspondiente al texto del mensaje y definir los
métodos adecuados para leerlo o bien establecer un nuevo valor
"""


class Mensaje:
    def __init__(self, remitente, destinatario, texto):
        self.remitente = remitente
        self.destinatario = destinatario
        self.__texto = texto
        self.leido = False

    def leer_mensaje(self):
        self.leido = True
        return self.__texto

    def establecer_texto(self, nuevo_texto):
        self.__texto = nuevo_texto

    def __str__(self):
        estado = "Leído" if self.leido else "No leído"
        return f"De: {self.remitente}, Para: {self.destinatario}, Estado: {estado}"


class BandejaEntrada:
    def __init__(self):
        self.mensajes = []

    def recibir_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def filtrar_mensajes(self, criterio, usuario_nombre=None):
        if criterio == 'leidos':
            return [msg for msg in self.mensajes if msg.leido]
        elif criterio == 'no leidos':
            return [msg for msg in self.mensajes if not msg.leido]
        elif criterio == 'enviados' and usuario_nombre:
            return [msg for msg in self.mensajes if msg.remitente == usuario_nombre]
        else:
            return self.mensajes

    def __str__(self):
        return "\n".join(str(msg) for msg in self.mensajes)


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bandeja_entrada = BandejaEntrada()

    def enviar_mensaje(self, destinatario, texto):
        nuevo_mensaje = Mensaje(self.nombre, destinatario.nombre, texto)
        destinatario.bandeja_entrada.recibir_mensaje(nuevo_mensaje)

    def __str__(self):
        return f"Usuario: {self.nombre}, Bandeja de entrada:\n{self.bandeja_entrada}"


def mostrar_menu():
    print("\nMenú:")
    print("1. Enviar mensaje")
    print("2. Ver mensajes leídos")
    print("3. Ver mensajes no leídos")
    print("4. Leer un mensaje")
    print("5. Cambiar de usuario")
    print("6. Salir")
    return input("Elige una opción: ")


def main():
    usuarios = {}

    # Crear usuarios
    cantidad_usuarios = int(input("Ingrese la cantidad de usuarios: "))
    for i in range(cantidad_usuarios):
        nombre = input(f"Ingrese el nombre del usuario {i + 1}: ")
        usuarios[nombre] = Usuario(nombre)

    usuario_nombre = input("Ingrese su nombre de usuario: ")
    while usuario_nombre not in usuarios:
        print("Usuario no encontrado.")
        usuario_nombre = input("Ingrese su nombre de usuario: ")
    print("\033[92mUsuario logueado exitosamente...\033[0m")

    while True:
        usuario_actual = usuarios[usuario_nombre]

        opcion = mostrar_menu()

        if opcion == '1':
            destinatario_nombre = input("Ingrese el nombre del destinatario: ")
            if destinatario_nombre not in usuarios:
                print("\033[91mDestinatario no encontrado.\033[0m")
                input("Presione ENTER para continuar...")
                continue
            texto = input("Ingrese el texto del mensaje: ")
            usuario_actual.enviar_mensaje(usuarios[destinatario_nombre], texto)
            print("\033[92m¡Mensaje enviado!\033[0m")

        elif opcion == '2':
            print("\nMensajes leídos:")
            for msg in usuario_actual.bandeja_entrada.filtrar_mensajes('leidos'):
                print(msg)

        elif opcion == '3':
            print("\nMensajes no leídos:")
            for msg in usuario_actual.bandeja_entrada.filtrar_mensajes('no leidos'):
                print(msg)

        elif opcion == '4':
            mensajes_no_leidos = usuario_actual.bandeja_entrada.filtrar_mensajes(
                'no leidos')
            if not mensajes_no_leidos:
                print("No hay mensajes no leídos.")
            else:
                for i, msg in enumerate(mensajes_no_leidos):
                    print(f"{i + 1}. {msg}")

                indice = int(
                    input("Ingrese el número del mensaje que desea leer: ")) - 1
                if 0 <= indice < len(mensajes_no_leidos):
                    mensaje = mensajes_no_leidos[indice]
                    print(f"Contenido del mensaje: {mensaje.leer_mensaje()}")
                else:
                    print("Índice no válido.")

        elif opcion == '5':
            usuario_nombre = input("Ingrese su nombre de usuario: ")
            while usuario_nombre not in usuarios:
                print("Usuario no encontrado.")
                usuario_nombre = input("Ingrese su nombre de usuario: ")
            print("\033[92mUsuario logueado exitosamente...\033[0m")

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

        input("Pulse ENTER para continuar...")


if __name__ == "__main__":
    main()
