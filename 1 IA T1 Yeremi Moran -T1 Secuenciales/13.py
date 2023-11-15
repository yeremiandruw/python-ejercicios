import os
os.system("cls")

catetoa= int(input("Cateto adyacente:"))
catetoo= int(input("Cateto opuesto:"))

c= ((catetoa*catetoa) + (catetoo*catetoo))
hipotenusa= c ** 0.5

print("Hipotenusa:" , format (hipotenusa,".2f" ))

