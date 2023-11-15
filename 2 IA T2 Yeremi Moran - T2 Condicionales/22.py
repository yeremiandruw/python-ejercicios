import os
os.system("cls")

unidadproductoA= int(input("Unidad de producto A:"))
unidadproductoB= int(input("Unidad de producto B:"))
importe= int
descuentoA= int
descuentoB= int 
productoA= 25 * unidadproductoA
productoB= 30 * unidadproductoB

if unidadproductoA > 50 :
    descuentoA= 0.15 * productoA

if unidadproductoB > 60 :
    descuentoB= 0.10 * productoB

totalapagarA= productoA - descuentoA
totalapagarB= productoB - descuentoB

print("ImporteA:" , productoA)
print("ImporteA:" , productoB)
print("DescuentoA:" , descuentoA)
print("DescuentoB:" , descuentoB)
print("Total a pagar del producto A:" , totalapagarA)
print("Total a pagar del producto B:" , totalapagarB)
