import os
os.system("cls")

montototal= int(input("Monto de la compra:"))
prestamo= int
diferencia=int

if montototal > 5000:
    prestamo = 0.30 * montototal
else : prestamo= 0.20 * montototal 

tazadeinteres= prestamo * 0.10
diferencia= montototal - prestamo

print("Cuanto tendra que pagar empresa:" , diferencia)
print("Prestamo:" , prestamo)
print("Taza de interes:" , tazadeinteres)