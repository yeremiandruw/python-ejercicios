import os
os.system("cls")

numero=int(input("Numero:"))

cifra1= int
cifra2=int
cifra3=int
cifra4=int
mayornumero=int

if numero >= 1000 and numero <=9999 :
    cifra1= int(numero/1000)
    cifra2= int((numero%1000)/100)
    cifra3= int((numero%100)/10)
    cifra4= int(numero%10)

    if cifra1 > cifra2 and cifra1 > cifra3 and cifra1 > cifra4 :
        numeromayor= cifra1
    elif cifra2 > cifra3 and cifra2 > cifra4 :
        numeromayor= cifra2
    elif cifra3 > cifra4 :
        numeromayor= cifra3
    else : numeromayor= cifra4

    if cifra1 < cifra2 and cifra1 < cifra3 and cifra1 < cifra4 :
        numeromenor= cifra1
    elif cifra2 < cifra3 and cifra2 < cifra4 :
        numeromenor= cifra2
    elif cifra3 < cifra4 :
        numeromenor= cifra3
    else : numeromenor= cifra4
    
    mayornumero=  str (numeromayor) + str (numeromenor)
else :
    print("Error") 
    
print("Numero:" , numero)
print("Numero mayor:" , mayornumero)
    

    


