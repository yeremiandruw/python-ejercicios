import os
os.system("cls")

radio= float(input("Ingrese el radio del cilindro:"))
altura= float(input("Ingrese la altura de cilindro:"))

areatotal= 2*3.14*radio*(radio+altura)
volumen=3.14*(radio*radio)*altura

print("Area total del cilindro:" ,format(areatotal,".2f"))
print("Volumen del cilindro:" ,format(volumen,".2f"))