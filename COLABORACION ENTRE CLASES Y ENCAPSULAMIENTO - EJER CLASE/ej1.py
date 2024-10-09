"""
Plantear una clase Club y otra clase Socio. La clase Socio debe tener los
siguientes atributos: nombre y la antigüedad en el club (en años).
La clase Club debe tener como atributos 3 objetos de la clase Socio. Definir
un método para imprimir el nombre del socio con mayor antigüedad en el
club. Definir como atributo privado la antigüedad en la institución y los
métodos adecuados para leer o bien establecer un nuevo valor
"""


class Socio:
    def __init__(self, nombre, antiguedad):
        self.nombre = nombre
        self.__antiguedad = antiguedad  # Atributo privado __

    def obtener_antiguedad(self):
        return self.__antiguedad

    def establecer_antiguedad(self, nueva_antiguedad):
        if nueva_antiguedad >= 0:
            self.__antiguedad = nueva_antiguedad
        else:
            print("La antigüedad no puede ser negativa.")


class Club:
    def __init__(self, socio1, socio2, socio3):
        self.socios = [socio1, socio2, socio3]

    def socio_con_mayor_antiguedad(self):
        mayor_antiguedad = -1
        socio_con_mayor_antiguedad = None
        for socio in self.socios:
            if socio.obtener_antiguedad() > mayor_antiguedad:
                mayor_antiguedad = socio.obtener_antiguedad()
                socio_con_mayor_antiguedad = socio
        return socio_con_mayor_antiguedad.nombre


s1 = Socio("Juan", 5)
s2 = Socio("María", 10)
s3 = Socio("Pedro", 3)

club = Club(s1, s2, s3)
print(f"El socio con mayor antigüedad es: {club.socio_con_mayor_antiguedad()}")
