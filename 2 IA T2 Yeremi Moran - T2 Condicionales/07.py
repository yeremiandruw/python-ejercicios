import os
os.system("cls")

numero1 = int(input("Numero 1:"))
numero2 = int(input("Numero 2:"))
numero3 = int(input("Numero 3:"))

numerointermedio= 0

if numero1 < numero2 < numero3 :
    numerointermedio = numero2

elif numero2 < numero1 < numero3 :
    numerointermedio = numero1

else : numerointermedio = numero3

print("numero intermedio:" , numerointermedio)