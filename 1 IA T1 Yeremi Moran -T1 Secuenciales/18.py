import os
os.system("cls")

cantidadproducto= int(input("Ingrese la cantidad adquirida:"))
precioproducto= float(input("Ingrese el precio del articulo:"))

importecompra= precioproducto*cantidadproducto
descuento= importecompra-(importecompra*0.15)
importeapagar= descuento-(descuento*0.15)

print("El importe de la compra S/.", format(importecompra,".2f"))
print("El primer descuento fue de S/.", format(importecompra*0.15,".2f"))
print("El segundo descuento fue de S/.", format(descuento*0.15,".2f"))
print("El importe a pagar es de S/.", format(importeapagar,".2f"))