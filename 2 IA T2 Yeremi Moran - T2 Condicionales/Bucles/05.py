import os
os.system("cls")

numero= int(input("Ingrese numero:"))

x= 0
for i in range(1,12 +1):
    x+= 1
    resultado= numero*x
    print(numero,"x", x , "=", resultado)