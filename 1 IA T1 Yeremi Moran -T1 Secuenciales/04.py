import os
os.system("cls")

pies= float(input("Pies:"))
pulgadas= float(input("Pulgadas:"))

estatura= (((pies*12)+pulgadas)*2.54)/100

print("Estatura en metros:" ,format (estatura,".2f"))
