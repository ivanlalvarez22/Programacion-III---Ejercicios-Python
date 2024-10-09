"""
Sistema de lectura de archivos: Crea una jerarquía de clases para representar
diferentes tipos de archivos, como "ArchivoTexto", "ArchivoPDF" y
"ArchivoImagen". Cada clase debe tener un método llamado "leer()" que muestre el
contenido del archivo en la consola. Luego, crea una función llamada
"leer_archivos()" que tome una lista de archivos y los lea uno por uno utilizando el
polimorfismo.
"""

from abc import ABC, abstractmethod


class Archivo(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def leer(self):
        pass


class ArchivoTexto(Archivo):
    def leer(self):
        print(f"Contenido del archivo de texto '{
              self.nombre}': [Contenido simulado de texto]")


class ArchivoPDF(Archivo):
    def leer(self):
        print(f"Contenido del archivo PDF '{
              self.nombre}': [Contenido simulado de PDF]")


class ArchivoImagen(Archivo):
    def leer(self):
        print(f"Contenido del archivo de imagen '{
              self.nombre}': [Contenido simulado de imagen]")


def leer_archivos(lista_archivos):
    for archivo in lista_archivos:
        archivo.leer()


# Ejemplo de uso:
archivo_texto = ArchivoTexto('archivo.txt')
archivo_pdf = ArchivoPDF('documento.pdf')
archivo_imagen = ArchivoImagen('imagen.jpg')

archivos = [archivo_texto, archivo_pdf, archivo_imagen]
leer_archivos(archivos)
