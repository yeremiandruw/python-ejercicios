import os
os.system("cls")

numero1= int(input("Numero de 3 cifras:"))
numero2= int(input("Numero de 3 cifras:"))

numero1cifra1= int(numero1/100)
numero1cifra2= int((numero1%100)/10)
numero1cifra3= int(numero1%10)

numero2cifra1= int(numero2/100)
numero2cifra2= int((numero2%100)/10)
numero2cifra3= int(numero2%10)

print("Numero cambiado")
print("Primer numero:" , (numero2cifra3*100) + (numero1cifra2*10) + (numero2cifra1))
print("Segundo numero:" , (numero1cifra3*100) + (numero2cifra2*10) + (numero1cifra1))