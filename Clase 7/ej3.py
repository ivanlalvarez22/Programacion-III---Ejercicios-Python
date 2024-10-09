"""
Sistema de ventas en línea: Crea una jerarquía de clases para modelar un sistema
de ventas en línea. Con una clase base "Producto" que contenga atributos
comunes como nombre, precio y disponibilidad. Luego, crea clases derivadas
como "Electrodomestico", "Ropa" y "Juguete" que hereden de la clase base y
proporcionen implementaciones específicas para características y métodos
relacionados con cada tipo de producto.
"""


class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad  # True si está disponible, False si no

    def mostrar_informacion(self):
        disponibilidad_str = "Disponible" if self.disponibilidad else "No disponible"
        info = f"Producto: {self.nombre}, Precio: ${
            self.precio:.2f}, Disponibilidad: {disponibilidad_str}"
        return info

    def aplicar_descuento(self, porcentaje_descuento):
        descuento = self.precio * (porcentaje_descuento / 100)
        self.precio -= descuento
        return f"Nuevo precio de {self.nombre} después de aplicar {porcentaje_descuento}% de descuento: ${self.precio:.2f}"


class Electrodomestico(Producto):
    def __init__(self, nombre, precio, disponibilidad, garantia):
        super().__init__(nombre, precio, disponibilidad)
        self.garantia = garantia  # Garantía en años

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        info = f"{info_base}, Garantía: {self.garantia} años"
        return info


class Ropa(Producto):
    def __init__(self, nombre, precio, disponibilidad, talla, material):
        super().__init__(nombre, precio, disponibilidad)
        self.talla = talla  # Talla de la prenda
        self.material = material  # Material de la prenda

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        info = f"{info_base}, Talla: {self.talla}, Material: {self.material}"
        return info


class Juguete(Producto):
    def __init__(self, nombre, precio, disponibilidad, edad_recomendada):
        super().__init__(nombre, precio, disponibilidad)
        self.edad_recomendada = edad_recomendada  # Edad recomendada para el juguete

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        info = f"{info_base}, Edad recomendada: {self.edad_recomendada} años"
        return info


# Ejemplo de uso:
electrodomestico = Electrodomestico("Licuadora", 120.00, True, 2)
ropa = Ropa("Camiseta", 20.00, True, "M", "Algodón")
juguete = Juguete("Lego", 35.00, False, 7)

print(electrodomestico.mostrar_informacion())
print(ropa.mostrar_informacion())
print(f"{juguete.mostrar_informacion()}\n")

print(electrodomestico.aplicar_descuento(10))
print(ropa.aplicar_descuento(15))
