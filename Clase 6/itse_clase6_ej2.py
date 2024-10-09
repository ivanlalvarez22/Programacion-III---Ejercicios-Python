"""
Crea un sistema de tienda en línea con clases como "Producto", "Carrito" y
"Cliente". Un objeto "Carrito" puede contener una lista de productos que el
cliente ha agregado, y el objeto "Cliente" puede tener un objeto "Carrito"
asociado. Implementar métodos para agregar clientes a la tienda, agregar
productos al carrito, calcular el total de la compra y procesar el pago.
"""


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def vaciar_carrito(self):
        self.productos = []


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

    def agregar_producto_al_carrito(self, producto):
        self.carrito.agregar_producto(producto)

    def calcular_total_compra(self):
        return self.carrito.calcular_total()

    def procesar_pago(self, monto):
        total_compra = self.calcular_total_compra()
        if monto >= total_compra:
            cambio = monto - total_compra
            self.carrito.vaciar_carrito()
            return f"Compra realizada. Su cambio es: ${cambio:.2f}"
        else:
            return "El monto ingresado es insuficiente para realizar la compra."


# Crear productos
producto1 = Producto("Camisa", 25)
producto2 = Producto("Pantalón", 40)
producto3 = Producto("Zapatos", 30)

# Crear cliente
cliente1 = Cliente("Juan")

# Agregar productos al carrito del cliente
cliente1.agregar_producto_al_carrito(producto1)
cliente1.agregar_producto_al_carrito(producto2)
cliente1.agregar_producto_al_carrito(producto3)

# Calcular total de la compra
total_a_pagar = cliente1.calcular_total_compra()
print(f"Total de la compra para {cliente1.nombre}: ${total_a_pagar:.2f}")

# Procesar el pago
monto_ingresado = 100
mensaje_pago = cliente1.procesar_pago(monto_ingresado)
print(mensaje_pago)
