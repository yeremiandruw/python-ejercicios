import os
os.system("cls")

varones= int(input("Varones:"))
mujeres= int(input("Mujeres:"))

total= varones + mujeres
porcentajedevarones= int(varones*100/total) 
porcentajedemujeres= int(mujeres*100/total)

print("Porcentaje de varones:" , porcentajedevarones, "%")
print("Porcentaje de mujeres:" , porcentajedemujeres, "%")