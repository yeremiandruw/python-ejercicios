import os
os.system("cls")

montodelacompra=int(input(" Monto de la compra:"))
docenasdelproducto=int(input("Numero de docenas:"))
montodeldescuento=0
unidadesdeobsequio=0
totalapagar=0
resultadoDivision=int

if docenasdelproducto > 6 :
    montodeldescuento= montodelacompra * 0.15
else : montodeldescuento= 0.10

if docenasdelproducto >= 30 :
    resultadoDivision=docenasdelproducto/3
    unidadesdeobsequio=resultadoDivision*2


totalapagar= montodelacompra - montodeldescuento

print("Monto de la compra:" , montodelacompra)
print("Monto del descuento:" , montodeldescuento)
print("Unidades de obsequio:" , int(unidadesdeobsequio))
print("Total a pagar:" , totalapagar)





