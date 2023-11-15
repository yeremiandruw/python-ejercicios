import os
os.system("cls")

base= int(input("Base del rectangulo:"))
altura= int(input("Altura del rectangulo:"))

area= base*altura
perimetro=2*(base+altura)

print("Area del rectangulo:" , area)
print("Perimetro del rectangulo:" , perimetro)