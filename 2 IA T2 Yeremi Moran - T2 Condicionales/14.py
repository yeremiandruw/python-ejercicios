import os
os.system("cls")

numero= int(input("Numero de la tarjeta:"))
importe= int(input("Importe de la compra:"))
descuento= int

if numero %2 == 0 and numero > 100 :
    descuento= 0.15 * importe
else : descuento = 0.05 * importe 

totalapagar= importe - descuento

print ("Numero:" , numero)
print ("importe:" , importe)
print ("Descuento:" , descuento)
print ("Total a pagar:" , totalapagar)

