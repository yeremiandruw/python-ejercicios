import os
os.system("cls")

numero=int(input("ingrese numero:"))
array=[]

if numero>=4 :
    for i in range(numero) :
        for x in range(numero*2):
            array.append("*")
        print(array)
        array=[]
