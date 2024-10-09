"""
Desarrolla un sistema de música con clases como "Canción" con atributos:
nombre, autor y duración, "Artista" con atributos: nombre artístico y un
identificador y "Álbum" con atributos: nombre de álbum, artista, año de
lanzamiento y productor. Un objeto "Álbum" puede contener una lista de
objetos "Canción", mientras que un objeto "Artista" puede tener una lista de
objetos "Álbum" que ha lanzado. Puedes implementar métodos para
agregar canciones a los álbumes y para buscar canciones de un artista
específico.
"""


class Cancion:
    def __init__(self, nombre, autor, duracion):
        self.nombre = nombre
        self.autor = autor
        self.duracion = duracion

    def __str__(self):
        return f"{self.nombre} por {self.autor}, duración: {self.duracion} minutos"


class Artista:
    def __init__(self, nombre_artistico, identificador):
        self.nombre_artistico = nombre_artistico
        self.identificador = identificador
        self.albumes = []

    def agregar_album(self, album):
        self.albumes.append(album)

    def buscar_canciones(self):
        canciones = []
        for album in self.albumes:
            canciones.extend(album.canciones)
        return canciones

    def __str__(self):
        return f"Artista: {self.nombre_artistico}, ID: {self.identificador}"


class Album:
    def __init__(self, nombre_album, artista, año_lanzamiento, productor):
        self.nombre_album = nombre_album
        self.artista = artista
        self.año_lanzamiento = año_lanzamiento
        self.productor = productor
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def __str__(self):
        return f"Álbum: {self.nombre_album} por {self.artista.nombre_artistico}, lanzado en {self.año_lanzamiento}, producido por {self.productor}"


# Ejemplo de uso
# Crear canciones
cancion1 = Cancion("Canción 1", "Autor 1", 3.5)
cancion2 = Cancion("Canción 2", "Autor 2", 4.0)
cancion3 = Cancion("Canción 3", "Autor 1", 2.5)

# Crear artista
artista = Artista("Nombre Artístico", "12345")

# Crear álbum
album = Album("Nombre del Álbum", artista, 2021, "Productor 1")

# Agregar canciones al álbum
album.agregar_cancion(cancion1)
album.agregar_cancion(cancion2)

# Agregar álbum al artista
artista.agregar_album(album)

# Crear otro álbum
album2 = Album("Segundo Álbum", artista, 2023, "Productor 2")
album2.agregar_cancion(cancion3)
artista.agregar_album(album2)

# Imprimir información del artista y sus álbumes
print(artista)
for album in artista.albumes:
    print(album)
    for cancion in album.canciones:
        print(f"  - {cancion}")

# Buscar todas las canciones del artista
canciones_artista = artista.buscar_canciones()
print("\nTodas las canciones del artista:")
for cancion in canciones_artista:
    print(cancion)
