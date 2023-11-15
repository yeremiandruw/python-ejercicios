import os
os.system("cls")

diapago=int(input("ingrese dia que pago:"))
cuotamensual= int(input("Cuota Mensual:"))

primermes= int
cliente= int
descuento= 0
recargo=0

if diapago <= 10 :
    porcentajeCuota=cuotamensual*0.02 #10
    if porcentajeCuota>5:
        descuento=porcentajeCuota #10
    else :
        descuento=5        
elif diapago>10 :
    porcentajeCuota=cuotamensual*0.03
    if porcentajeCuota>10:
        recargo=porcentajeCuota
    else :
        recargo=10
total=(cuotamensual-descuento)+recargo

print("total pago por mes:" ,total)         

    
