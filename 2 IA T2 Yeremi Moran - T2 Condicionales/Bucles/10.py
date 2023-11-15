import os
os.system("cls")

numero= 1000 
cifra1= int
cifra2= int
cifra3= int
cifra4= int

contador=0

while numero >= 1000 and numero <=9999 :
    cifra1= int (numero/1000)
    cifra2= int((numero%1000)/100)
    cifra3= int((numero%100)/10)
    cifra4= (numero%10) 
    
    sumapar= 0
    if cifra1 %2 == 0 :
        sumapar += cifra1     
    if cifra2>0 and cifra2 %2 == 0 :
        sumapar += cifra2 
    if cifra3>0 and cifra3 %2 == 0 :
        sumapar += cifra3
    if cifra4>0 and cifra4 %2 == 0 :
        sumapar += cifra4
        
    sumaimpar= 0
        
    if cifra1 %2 == 1 :
        sumaimpar += cifra1
    if cifra2 %2 == 1 :
        sumaimpar += cifra2    
    if cifra3 %2 == 1 :
        sumaimpar += cifra3
    if cifra4 %2 == 1 :
        sumaimpar += cifra4  
    
    if sumaimpar == sumapar :
        contador=contador+1
        print("Cumple la condicion:" , numero)   
        
    numero+=1
print("Cantidad",contador)    
    