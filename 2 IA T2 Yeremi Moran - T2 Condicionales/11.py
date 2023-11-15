import os
os.system("cls")

numero= int(input("Numero:"))


if numero > 0:
    numeroPositivo= numero
    print ("Numero Positivo")
elif numero < 0:
    numeroNegativo= numero
    print ("Numero Negativo")
elif numero == 0 :
    print ("Numero Cero")

