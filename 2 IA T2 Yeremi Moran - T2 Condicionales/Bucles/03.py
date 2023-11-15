import os
os.system("cls")

numero = int(input("Numero:"))

rpta= "1,"
divisor= 2
divisores= 2

fin= numero // 2 if numero % 2 == 0 else numero // 3

while divisor <= fin :
    if numero % divisor == 0 :
        divisores +=1
        rpta += str(divisor) + ("," if divisor < fin else "")
    divisor +=1 

rpta += "," + str(numero)
print("Divisores:" , rpta)
print("Cantidad de divisores:" , divisores)