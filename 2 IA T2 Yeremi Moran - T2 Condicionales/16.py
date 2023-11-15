import os
os.system("cls")

ingreso= int(input("Ingreso: "))
cuotaInicial= int
costoCasa= ingreso
cuotaMensual= int

if ingreso < 1250 : 
    cuotaInicial = 0.15 * costoCasa  
    cuotaMensual = (costoCasa - cuotaInicial) / 120

elif ingreso >= 1250 : 
    cuotaInicial = 0.30 * costoCasa 
    cuotaMensual = ( costoCasa - cuotaInicial) / 75

print("Cuota Inicial:" , cuotaInicial)
print("Cuota Mensual:" , cuotaMensual)
