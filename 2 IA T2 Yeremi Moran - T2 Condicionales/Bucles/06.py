import os
os.system("cls")

numero= int(input("Ingrese Numero:"))
x= int(input("Desde:"))
y= int(input("Hasta:"))


for i in range(x,y+1):
    resultado= numero * x 
    print(numero , "x", x , "=" , resultado)
    if(x<y):
        x+=1
    
    
    