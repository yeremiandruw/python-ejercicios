import os
os.system("cls")

dividendo = int(input("Dividendo:"))
divisor = int(input("Divisor:"))

cociente = 0

while dividendo >= divisor :
    dividendo -= divisor
    cociente += 1

print("Cociente:" , cociente)
print("Residuo:" , dividendo)