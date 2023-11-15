import os
os.system("cls")


sueldobruto= int(input("Sueldo bruto:"))
hijo= int(input("Cantidad de hijos:"))


if hijo > 1 :
    bonificacion = 0.125 * sueldobruto
    bonificacionPorHijo = hijo*40
    totalsueldo=sueldobruto+bonificacion+bonificacionPorHijo

else : 
    bonificacion = 0.10 *sueldobruto
    bonificacionPorHijo = 0
    totalsueldo =sueldobruto +bonificacion


print("Hijo:" , hijo)
print("Bonificacion:" , bonificacion)
print("Bonificacion por hijo:" , bonificacionPorHijo)
print("Sueldo Neto:" , totalsueldo)

