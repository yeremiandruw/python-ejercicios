import os
os.system("cls")

angulo= int (input("ingrese angulos"))

clasificacion= str

if angulo == 0 :
    clasificacion = "nulo" 
    
elif angulo >0 and angulo <90 :
    clasificacion = "agudo"

elif angulo == 90 :
    clasificacion = "recto"

elif angulo >90 and angulo <180 :
    clasificacion = "obtuso"

elif angulo == 180 :
    clasificacion = "llano"

elif angulo >180 and angulo <360 :
    clasificacion = "cóncavo"

elif angulo == 360 :
    clasificacion = "completo"

print("clasificacion:" ,clasificacion)
print("angulo en grados :" ,angulo,"°")
