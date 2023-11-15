import os
os.system("cls")

numero=int(input("Numero:"))

multiplo= 0
i= 1
x= 0
arraymultiplo3=[]
arraymultiplo3ynode5=[]
rpta=0

while i <= numero:
    
    mul3=i*3
    arraymultiplo3.append(mul3)
    i+=1

while x < len(arraymultiplo3):
    
    if arraymultiplo3[x]%5!=0 :
        rpta+=arraymultiplo3[x]
        arraymultiplo3ynode5.append(arraymultiplo3[x])
    x+=1
    
print("Suma:",rpta)
print("multiplos de 3 :",arraymultiplo3)
print("multiplos de 3 y no de 5:",arraymultiplo3ynode5)



