import os
os.system("cls")

metro= int(input("Digite un numero:"))

centimetros= metro *100
pulgada= centimetros/2.54
pies= pulgada/12
yarda= pies/3

print("Centimetro:",format(centimetros,".2f"))
print("Pulgada:",format (pulgada,".2f"))
print("Pies:",format (pies,".2f"))
print("Yarda:", format(yarda,".2f"))