import os
os.system("cls")

numero= int(input("Numero:"))
multiplos= int(input("Multiplo:"))

rpta= ""
i= 0

while i <= multiplos:
    rpta+= str(numero*i) + ("," if i < multiplos else "")
    i += 1

rpta = ""
for i in range (1, multiplos +1) :
    rpta += str(numero* i) + ("," if i < multiplos else "")

print(f"Los multiplos de:{numero}" )
print("Respuesta:" , rpta)