import os
os.system("cls")

monto=int(input("Monto:"))
categoria= int(input("Categoria:"))
sueldo= int(input("Sueldo:"))

sueldobruto=sueldo
sueldoneto= int
descuento= int
comisionaplicada= int

if sueldo>=1025 :
    if sueldo > 3500 : descuento = 0.15 * sueldo 
    else : descuento= 0.08 * sueldo

    if monto < 5000 : 
        comisionaplicada= 0.05 * monto
    elif monto > 5000 and monto < 10000 :
        comisionaplicada= 0.10 * monto
    elif monto > 10000 and monto < 20000 :
        comisionaplicada= 0.12 * monto
    elif monto >20000 :
        comisionaplicada= 0.15 * monto

    if categoria == 1 :
        bonificacion = 0.05 * sueldo
    elif categoria == 2 :
        bonificacion = 0.10 * sueldo
    elif categoria == 3 : 
        bonificacion = 0.12 * sueldo
    elif categoria == 4 :
        bonificacion = 0.15 * sueldo

    totalapagar= (sueldo - descuento) + (comisionaplicada + bonificacion)
else : print("es menor que el sueldo basico")    

print("Sueldo bruto:" , sueldobruto)
print("Descuento:" , descuento)
print("Comision aplicada:" , comisionaplicada)
print("Bonificacion:" , bonificacion)
print("Total a pagar:" , totalapagar)





