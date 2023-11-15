import os
os.system("cls")

edad= int(input("Edad de la persona:"))
sexo= str (input(" Sexo:"))


if sexo == "Femenino" and edad < 23 :
    categoria= "FA"
elif sexo == "Femenino" and edad > 23 : 
    categoria= "FB"

if sexo == "Masculino" and edad < 25 : 
    categoria= "MA"
elif sexo == "Masculino" and edad > 25 : 
    categoria == "MB"

print("Edad:" , edad)
print("Sexo:" , sexo)
print("Categoria:" , categoria)