import os
os.system("cls")

numero=int(input("Numero:"))
potencia= int(input("Potencia:"))
resultado=1
i= 0

while i < potencia :
    i+=1
    resultado*=numero 

# for i in range(potencia):
#     resultado*=numero

print("resultado:" , resultado)    
