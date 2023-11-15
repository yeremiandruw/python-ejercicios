import os
os.system("cls")

numero= int(input("Ingrese Numero de 4 cifras:"))

cifra1= int(numero/1000)
cifra2= int((numero%1000)/100)
cifra3= int((numero%100)/10)
cifra4= numero%10

print("El numero al reves es:" ,(cifra4*1000) + (cifra3*100) + (cifra2*10) + (cifra1*1))