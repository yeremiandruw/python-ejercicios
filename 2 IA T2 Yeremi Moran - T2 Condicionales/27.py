import os
os.system("cls")

sueldobruto=int(input("Suelo bruto:"))
montovendido= int(input("Monto vendido:"))
empresa= int
obsequio=0

comision = montovendido*0.15

if sueldobruto > 1800 :
    descuento= sueldobruto * 0.10
else : descuento= sueldobruto * 0.05

if montovendido > 1000 :
    obsequio += 3
else: obsequio += 1

sueldoneto= (sueldobruto - descuento) + comision


print("Total:" , sueldoneto)
print("Obsequio:" , obsequio)