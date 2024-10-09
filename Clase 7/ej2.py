"""
Juego de rol: Crea una jerarquía de clases para modelar un juego de rol.con una
clase base "Personaje" que contenga atributos comunes como puntos de vida,
puntos de ataque y puntos de defensa. Luego, crea clases derivadas como
"Guerrero", "Mago" y "Arquero" que hereden de la clase base y proporcionen
implementaciones específicas para habilidades y características únicas de cada
tipo de personaje.
"""


class Personaje:
    def __init__(self, vida, ataque, defensa):
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa


class Guerrero(Personaje):
    def __init__(self, vida, ataque, defensa, nombre):
        super().__init__(vida, ataque, defensa)
        self.nombre = nombre

    # Habilidad: Furia Berserker
    def furia_berserker(self):
        self.ataque *= 1.2
        return f"¡{self.nombre} activó la Furia Berserker! Su ataque aumentó."

    # Habilidad: Escudo de Acero
    def escudo_de_acero(self):
        self.defensa *= 1.4
        return f"¡{self.nombre} desplegó el Escudo de Acero! Su defensa se fortaleció."

    def __str__(self):
        cadena = f"Nombre: {self.nombre} \n"
        cadena += f"Vida: {self.vida} \n"
        cadena += f"Ataque: {self.ataque} \n"
        cadena += f"Defensa: {self.defensa} \n"
        return cadena


class Mago(Personaje):
    def __init__(self, vida, ataque, defensa, nombre):
        super().__init__(vida, ataque, defensa)
        self.nombre = nombre

    # Habilidad: Rayo Arcano
    def rayo_arcano(self):
        ataque = self.ataque * 1.5
        return f"¡{self.nombre} lanzó un potente Rayo Arcano! Infligió {ataque} de daño."

    # Habilidad: Escudo de Energía
    def escudo_de_energia(self):
        self.defensa *= 1.3
        return f"¡{self.nombre} invocó un Escudo de Energía! Su defensa aumentó."

    def __str__(self):
        cadena = f"Nombre: {self.nombre} \n"
        cadena += f"Vida: {self.vida} \n"
        cadena += f"Ataque: {self.ataque} \n"
        cadena += f"Defensa: {self.defensa} \n"
        return cadena


class Arquero(Personaje):
    def __init__(self, vida, ataque, defensa, nombre):
        super().__init__(vida, ataque, defensa)
        self.nombre = nombre

    # Habilidad: Disparo Preciso
    def disparo_preciso(self):
        ataque = self.ataque * 2
        return f"¡{self.nombre} realizó un Disparo Preciso! Infligió {ataque} de daño."

    # Habilidad: Curación Rápida
    def curacion_rapida(self):
        self.vida += 0.3 * self.vida
        return f"¡{self.nombre} se curó rápidamente! Su vida aumentó."

    def __str__(self):
        cadena = f"Nombre: {self.nombre} \n"
        cadena += f"Vida: {self.vida} \n"
        cadena += f"Ataque: {self.ataque} \n"
        cadena += f"Defensa: {self.defensa} \n"
        return cadena


# Ejemplo de uso
guerrero = Guerrero(500, 350, 400, "Axe")
mago = Mago(350, 550, 250, "Keeper of the Light")
arquero = Arquero(300, 500, 320, "Bullseye")

print(guerrero.furia_berserker())
print(guerrero.escudo_de_acero())
print(guerrero)

print(mago.rayo_arcano())
print(mago.escudo_de_energia())
print(mago)

print(arquero.disparo_preciso())
print(arquero.curacion_rapida())
print(arquero)
