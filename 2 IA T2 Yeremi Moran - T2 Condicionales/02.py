import os
os.system("cls")
 
# ingresar datos al sistema
unidades= int (input("ingrese unidades:")) 
#######5
precio=20
descuento=int
caramelosAdquiridos=int
totalPagar=0

# multiplicacion unidades por precio
importe=unidades * precio

if unidades >=1 and unidades <=50 :
    caramelosAdquiridos=5
elif unidades >=51 and unidades <=100 :
    caramelosAdquiridos=10
elif unidades >100 :
    caramelosAdquiridos=15
      
if importe > 700 :
    descuento=importe*0.16
    
elif importe >= 501 and importe<7000 :
    descuento=importe*0.14
    
elif importe <=500 :
    descuento=importe*0.12
    
    
totalPagar=importe - descuento

print("importe:",importe) 
print("descuento:",descuento) 
print("total a pagar:",totalPagar) 
print("numero de caramelos:",caramelosAdquiridos) 

