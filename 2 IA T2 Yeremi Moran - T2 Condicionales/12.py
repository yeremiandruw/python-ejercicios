import os
os.system("cls")

# variables
numero= int(input("Numero:"))
dia=str


# logica
if numero== 1 :
     dia="lunes"
elif numero==2 :
     dia= "martes"
elif numero==3 :
     dia= "miercoles"
elif numero==4 :
     dia= "jueves"
elif numero==5 :
     dia= "viernes"
elif numero==6 :
     dia= "sabado"
elif numero==7 :
     dia= "domingo"
else :dia="dia ingresado no existe"

# def calcularDia(numDia):
#     if numDia== 1 :
#         return "lunes"
#     elif numDia==2 :
#         return "martes"
#     elif numDia==3 :
#         return "miercoles"
#     elif numDia==4 :
#         return "jueves"
#     elif numDia==5 :
#         return "viernes"
#     elif numDia==6 :
#         return "sabado"
#     elif numDia==7 :
#         return "domingo"
#     else :return"dia ingresado no existe"

# print("Calculo con una funcion: ",calcularDia(numero))    

print("Numero:", numero)
print("Dia:" , dia)