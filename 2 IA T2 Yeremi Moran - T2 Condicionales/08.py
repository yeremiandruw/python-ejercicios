import os
os.system("cls")

examen1 = int(input("Examen 1:")) 
examen2 = int(input("Examen 2:"))
examen3 = int(input("Examen 3:"))

propinaMensual = 20

if examen1 > 11 :
    propinaMensual += 5

if examen2 > 11 :
    propinaMensual += 5

if examen3 > 11 : 
    propinaMensual += 5

total= propinaMensual 

print("Propina mensual:" , propinaMensual)

