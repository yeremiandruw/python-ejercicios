import os
os.system("cls")

numero= int(input("Numero:"))
cifra1=int
cifra2=int
cifra3=int
cifra4=int
estadocivil= str
genero= str

if numero >=1000 and numero <=9999 :
    cifra1= int(numero/1000)
    cifra2= int((numero%1000)/100)
    cifra3= int((numero%100)/10)
    cifra4= int(numero%10)

    if cifra1 == 1 : estadocivil = "soltero"
    elif cifra1 == 2 : estadocivil = "casado"
    elif cifra1 == 3 : estadocivil = "divorciado"
    elif cifra1 == 4 : estadocivil = "viudo"
    else : estadocivil= "error"
    
    # edad= cifra2 , cifra3 456
    edad = str(cifra2) + str(cifra3)
    if cifra4 == 1 : genero = "Masculino"
    elif cifra4 == 2 : genero = "Femenino"
    else : genero= "Error"
    
else :
    print("No ingreso numero de 4 cifras")

    

print("Cifra 1:" , cifra1)
print("Cifra 2:" , cifra2)
print("Cifra 3:" , cifra3)
print("Cifra 4:" , cifra4)
print("Genero:" , genero)
print("Edad:" , edad)
print("Estado civil:" , estadocivil)