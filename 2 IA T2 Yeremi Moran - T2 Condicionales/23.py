import os
os.system("cls")

notaMatematica= int(input("Nota de Matematica:"))
notaFisica= int(input("Nota de fisica:"))
promedio= int
propina= int
propinadematematica= float
propinafisica=float


if notaMatematica > 17 :
    propinadematematica = 3
else : propinadematematica = 1

if notaFisica > 15 :
    propinafisica = 2
else: propinafisica = 0.5

propina= propinafisica + propinadematematica

if notaFisica > 16 and notaMatematica > 16 :
    obsequio= "reloj"
else: obsequio = "Sin obsequio"    

promedio= (notaFisica + notaMatematica) / 2

print("Nota de Matematica:" , notaMatematica)
print("Nota de Fisica:" , notaFisica)
print("Promedio:" , promedio)
print("Propina: S/" , propina)
print("Obsequio:" , obsequio)