"""
Imagina que vendes pan fresco a 400 pesos el kilo. El pan 
que no es del día tiene un descuento del 60%. Escribe un 
programa que comience leyendo los kilos de pan vendidos que 
no son del día, muestre el precio del pan fresco, el 
descuento que se hace por no serlo y el monto total del 
pan vendido que no es fresco.
"""

# Precio por kilo de pan fresco
PRECIO_FRESCO_KILO = 400

# Leer los kilos de pan vendidos que no son del día
kilos_pan_no_fresco = float(
    input("Ingrese los kilos de pan no fresco vendidos: "))

# Calcular el precio total del pan fresco
precio_total_fresco = kilos_pan_no_fresco * PRECIO_FRESCO_KILO

# Calcular el descuento por no ser pan fresco (60%)
descuento = precio_total_fresco * 0.6

# Calcular el monto total del pan vendido que no es fresco (restando el descuento al precio total)
monto_total_pan_no_fresco = precio_total_fresco - descuento

print(f"Precio del pan fresco por kilo: ${PRECIO_FRESCO_KILO}")
print(f"Descuento por no ser pan fresco: ${descuento}")
print(f"Monto total del pan vendido que no es fresco: ${
      monto_total_pan_no_fresco}")
