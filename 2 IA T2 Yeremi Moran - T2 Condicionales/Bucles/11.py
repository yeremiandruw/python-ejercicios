import os
os.system("cls")

numero= 100
cifra1= int
cifra2= int
cifra3= int

while numero <= 999 :
    
    cifra1= int (numero/100)
    cifra2= int ((numero%100)/10)
    cifra3= (numero %10)
    
    if cifra1 == cifra3:
        print("Numero capicua:" , numero)
        
    numero+=1
    
