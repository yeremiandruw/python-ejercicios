import os
os.system("cls")

numero= int(input("Ingrese Numero de 4 cifras:"))


cifra1= int(numero/1000)
cifra2= int((numero%1000)/100)
cifra3= int((numero%100)/10)
cifra4= numero%10

print("Suma de los digitos:" , cifra1+cifra2+cifra3+cifra4)