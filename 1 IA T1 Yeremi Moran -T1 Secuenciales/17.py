import os
os.system("cls")

donacion= int(input("Ingrese monto de la donacion:"))

centrodesalud= donacion*0.25
comedorinfantil= donacion*0.35
escuelainfantil= donacion*0.25
asiloancianos= donacion*0.15

print("El centro de salud recibe S/.", format(centrodesalud,".2f"))
print("El comedor infantil recibe S/.", format(comedorinfantil,".2f"))
print("La escuela infantil recibe S/.", format(escuelainfantil,".2f"))
print("El asilo de ancianos recibe S/.", format(asiloancianos,".2f"))