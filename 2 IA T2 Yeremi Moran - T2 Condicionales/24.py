import os
os.system("cls")

monto= int(input("Monto del vendedor:"))
venta= int
sueldo= monto * 0.10
 
if monto > 5000 :
    venta = monto/500  
    bono=venta * 25
    total=sueldo+bono
else : print("Error")
    
    
print("Sueldo:" , total)    

