import os
os.system("cls")

multiplicado= int(input("Multiplicando:"))
multiplicador= int(input("Multiplicador:"))

respuesta = 0

for i in range(multiplicador) :
    respuesta += multiplicado
print("Respuesta:" , respuesta)