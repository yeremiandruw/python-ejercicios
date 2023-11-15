import os
os.system("cls")

numeroA = int(input("Numero A:"))
mensaje= str
cifra1= int
cifra2= int
cifra3= int
if numeroA >=100 and numeroA <=999 :
    cifra1= int(numeroA/100)
    cifra2= int((numeroA%100)/10)
    cifra3= int(numeroA%10)
  
    if ((cifra2 == cifra1 + 1 and cifra3 == cifra2 + 1) or (cifra2 == cifra1 - 1 and cifra3 == cifra2 -1) ):
        mensaje= "Las cifras son consecutivas"
    else :
        mensaje= "Las cifras no son consecutivas"


else :  
    mensaje= "Ingresar numero positivo de 3 cifras"

print (mensaje)