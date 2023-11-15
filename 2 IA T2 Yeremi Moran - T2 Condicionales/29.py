import os
os.system("cls")

horatrabajada= int(input("Horas Trabajadas:"))
sueldobruto= int(input("Sueldo Bruto:"))


tarifa= int
horaextra= 0
descuento=0

if horatrabajada>48 :    
    horaextra= 0.20 * sueldobruto 

if sueldobruto > 1500 :
        descuento= 0.11 * sueldobruto

totalapagar= (sueldobruto - descuento )+horaextra


print("Pago por hora extra:" , horaextra)
print("Descuento:" , descuento)
print("Total a pagar:" , totalapagar)
