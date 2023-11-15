import os
os.system("cls")

donaciobenefica= int(input("Donacion Benefica:"))
monto= donaciobenefica
centrodesalud= 0
comedordeniños= 0
bolsa= 0
if monto >=10000 :
    centrodesalud= monto * 0.30 
    comedordeniños= monto * 0.50
    bolsa = monto-(centrodesalud + comedordeniños)
else :
    centrodesalud= monto * 0.25 
    comedordeniños= monto * 0.60
    bolsa = monto-(centrodesalud + comedordeniños)

# otra forma
# if monto >=10000 :
#     centrodesalud= monto * 0.30 
#     comedordeniños= monto * 0.50
#     bolsa = monto-(centrodesalud + comedordeniños)
# elif monto<10000 :
#     centrodesalud= monto * 0.25 
#     comedordeniños= monto * 0.60
#     bolsa = monto-(centrodesalud + comedordeniños)  

print("Donacion benefica:" , donaciobenefica)
print("Centro de salud:" , centrodesalud)
print("Comedor de niños:" , comedordeniños)
print("Bolsa:" , bolsa)
