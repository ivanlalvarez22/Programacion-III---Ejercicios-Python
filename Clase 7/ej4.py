"""
Sistema de cálculo de impuestos: Crea una jerarquía de clases para representar
diferentes tipos de contribuyentes, como "PersonaFísica", "PersonaJurídica" y
"PersonaExtranjera". Cada clase debe tener un método llamado
"calcular_impuesto()" que calcule el impuesto correspondiente para ese tipo de
contribuyente. Luego, crea una función llamada "calcular_impuesto_total()" que
tome una lista de contribuyentes y calcule el impuesto total utilizando el
polimorfismo.
"""

from abc import ABC, abstractmethod


class Contribuyente(ABC):
    def __init__(self, nombre, ingreso_anual):
        self.nombre = nombre
        self.ingreso_anual = ingreso_anual

    @abstractmethod
    def calcular_impuesto(self):
        pass


class PersonaFísica(Contribuyente):
    def calcular_impuesto(self):
        # Supongamos que la tasa de impuesto para persona física es del 15%
        tasa_impuesto = 0.15
        impuesto = self.ingreso_anual * tasa_impuesto
        return impuesto


class PersonaJurídica(Contribuyente):
    def calcular_impuesto(self):
        # Supongamos que la tasa de impuesto para persona jurídica es del 30%
        tasa_impuesto = 0.30
        impuesto = self.ingreso_anual * tasa_impuesto
        return impuesto


class PersonaExtranjera(Contribuyente):
    def calcular_impuesto(self):
        # Supongamos que la tasa de impuesto para persona extranjera es del 20%
        tasa_impuesto = 0.20
        impuesto = self.ingreso_anual * tasa_impuesto
        return impuesto


def calcular_impuesto_total(lista_contribuyentes):
    total_impuesto = 0
    for contribuyente in lista_contribuyentes:
        total_impuesto += contribuyente.calcular_impuesto()  # uso del polimorfismo
    return total_impuesto


# Ejemplo de uso:
persona_fisica = PersonaFísica("Juan Pérez", 50000)
persona_juridica = PersonaJurídica("Empresa S.A.", 200000)
persona_extranjera = PersonaExtranjera("John Doe", 80000)

print(f"Impuesto persona física: {persona_fisica.calcular_impuesto()}")
print(f"Impuesto persona jurídica: {persona_juridica.calcular_impuesto()}")
print(f"Impuesto persona extranjera: {persona_extranjera.calcular_impuesto()}")

contribuyentes = [persona_fisica, persona_juridica, persona_extranjera]
impuesto_total = calcular_impuesto_total(contribuyentes)

print(f"Impuesto total recaudado: ${impuesto_total:.2f}")
