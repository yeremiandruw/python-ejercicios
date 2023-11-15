import os
os.system("cls")

radio= float(input("Radio de un cilindro:"))
altura= float(input("Altura de un cilindro:"))

areabase= 3.1416*(radio*radio)
arealateral= 2*3.1416*radio*altura
areatotal=2*areabase*arealateral

print("Area de la base:" ,format (areabase, ".2f"))
print("Area lateral :" , format (arealateral,".2f"))
print("Area total:" ,format (areatotal,".2f"))