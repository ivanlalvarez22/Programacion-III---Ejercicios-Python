"""
Crea un sistema de almacén con clases "Producto" y "Proveedor". Un
objeto "Almacén" puede contener una lista de objetos "Producto", y cada
"Producto" puede tener un objeto "Proveedor" asociado. Implementar
métodos para: agregar productos al almacén, agregar proveedores al
almacén, mostrar los productos que venden al almacén los proveedores y
gestionar el inventario del almacén (altas de productos y modificaciones de
precio y listado de productos sin stock).
"""


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre


class Producto:
    def __init__(self, nombre, precio, proveedor):
        self.nombre = nombre
        self.precio = precio
        self.proveedor = proveedor
        self.stock = 0  # Agregamos un atributo para el stock inicial


class Almacen:
    def __init__(self):
        self.productos = []
        self.proveedores = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)

    def mostrar_productos_proveedor(self, proveedor):
        productos_proveedor = [
            producto.nombre for producto in self.productos if producto.proveedor == proveedor]
        if productos_proveedor:
            print(f"Productos del proveedor {proveedor.nombre}:")
            for producto in productos_proveedor:
                print(producto)
        else:
            print(f"No hay productos del proveedor {
                  proveedor.nombre} en el almacén.")

    def alta_producto(self, nombre, precio, proveedor):
        nuevo_producto = Producto(nombre, precio, proveedor)
        self.agregar_producto(nuevo_producto)

    def modificar_precio(self, nombre_producto, nuevo_precio):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.precio = nuevo_precio
                print(f"El precio del producto {
                      nombre_producto} ha sido modificado a ${nuevo_precio}.")

    def listar_productos_sin_stock(self):
        productos_sin_stock = [
            producto.nombre for producto in self.productos if producto.stock == 0]
        if productos_sin_stock:
            print("Productos sin stock:")
            for producto in productos_sin_stock:
                print(producto)
        else:
            print("No hay productos sin stock en el almacén.")

    def gestionar_inventario(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.stock += cantidad
                print(f"Se agregaron {cantidad} unidades del producto {
                      nombre_producto} al inventario.")
                return
        print(f"No se encontró el producto {
              nombre_producto} en el inventario.")

# Ejemplo de uso


# Crear proveedores
proveedor1 = Proveedor("Proveedor A")
proveedor2 = Proveedor("Proveedor B")

# Crear almacén
almacen = Almacen()

# Agregar proveedores al almacén
almacen.agregar_proveedor(proveedor1)
almacen.agregar_proveedor(proveedor2)

# Agregar productos al almacén
almacen.alta_producto("Producto 1", 10, proveedor1)
almacen.alta_producto("Producto 2", 15, proveedor2)
almacen.alta_producto("Producto 3", 20, proveedor1)

# Modificar el precio de un producto
almacen.modificar_precio("Producto 1", 12)

# Mostrar los productos de un proveedor en el almacén
almacen.mostrar_productos_proveedor(proveedor1)

# Gestionar inventario (ejemplo de uso)
almacen.gestionar_inventario("Producto 1", 5)
almacen.gestionar_inventario("Producto 2", 15)
almacen.gestionar_inventario("Producto 2", 17)
almacen.gestionar_inventario("Producto 3", 55)

# Listar productos sin stock
almacen.listar_productos_sin_stock()

for prod in almacen.productos:
    print(f"Nombre: {prod.nombre}, Precio: {prod.precio}, Proveedor: {
          prod.proveedor.nombre}, Stock: {prod.stock}")
