import os
os.system("cls")

producto= input("Codigo de producto:")
unidad= int(input("Cantidad:"))

importe = 0
descuento= 0
precio = 0

if producto == "101" :
    precio = 17
elif producto == "102" :
    precio = 25    
elif producto == "103" :
    precio = 16
elif producto == "104" :
    precio = 27

importe = unidad * precio


if unidad >1 and unidad <10 :
    descuento= importe * 0.05 
elif unidad >11 and unidad <20 :
    descuento= importe * 0.08
elif unidad >21 and unidad <30 :
    descuento= importe * 0.10
elif unidad >=31 :
    descuento=importe * 0.13

totalPagar= importe - descuento

print("Importe de la compra:",importe)
print("Descuento:",descuento)
print("Total a pagar:",totalPagar)
