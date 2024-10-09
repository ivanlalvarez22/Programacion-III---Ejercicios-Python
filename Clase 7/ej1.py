"""
Sistema de reservas de vuelos: Crea una jerarquía de clases para modelar un
sistema de reservas de vuelos. Existe clase base "Vuelo" que contiene información
común como número de vuelo, origen y destino. Luego, crea clases derivadas
como "VueloNacional" y "VueloInternacional" que hereden de la clase base y
proporcionen implementaciones específicas, como métodos para verificar
requisitos de pasaporte y calcular el precio del vuelo.
"""


class Vuelo:
    def __init__(self, numero_vuelo, origen, destino):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino

    def mostrar_informacion(self):
        info = f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino}"
        return info


class VueloNacional(Vuelo):
    def __init__(self, numero_vuelo, origen, destino, tasa_nacional=50):
        super().__init__(numero_vuelo, origen, destino)
        self.tasa_nacional = tasa_nacional  # Tasa fija para vuelos nacionales

    def calcular_precio(self, tarifa_base):
        # Supongamos que el precio del vuelo es la tarifa base más una tasa fija
        return tarifa_base + self.tasa_nacional


class VueloInternacional(Vuelo):
    def __init__(self, numero_vuelo, origen, destino, tasa_internacional=100):
        super().__init__(numero_vuelo, origen, destino)
        # Tasa fija para vuelos internacionales
        self.tasa_internacional = tasa_internacional

    def verificar_requisitos_pasaporte(self, pasaporte_valido):
        # Verifica si el pasaporte es válido para el vuelo internacional
        return pasaporte_valido

    def calcular_precio(self, tarifa_base):
        # Supongamos que el precio del vuelo es la tarifa base más una tasa fija
        return tarifa_base + self.tasa_internacional


# Ejemplo de uso:
vuelo_nacional = VueloNacional("NA123", "Madrid", "Barcelona")
vuelo_internacional = VueloInternacional("IN456", "Madrid", "Nueva York")

print(vuelo_nacional.mostrar_informacion())
print("Precio del vuelo nacional:", vuelo_nacional.calcular_precio(200))

print(vuelo_internacional.mostrar_informacion())
print("Requisitos de pasaporte válidos:",
      vuelo_internacional.verificar_requisitos_pasaporte(True))
print("Precio del vuelo internacional:",
      vuelo_internacional.calcular_precio(600))
