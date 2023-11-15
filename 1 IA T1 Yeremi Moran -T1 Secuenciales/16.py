import os
os.system("cls")

horastrabajadas=float(input("Ingrese las horas trabajadoras:"))
tarifahoraria=float(input("Ingrese la tarifa horaria:"))

sueldobasico= tarifahoraria*horastrabajadas
bonificacion= sueldobasico*0.20
sueldobruto= sueldobasico + bonificacion
descuento= sueldobruto*0.10
sueldoneto=sueldobruto-descuento

print("Sueldo basico: S/.", format(sueldobasico,".2f"))
print("Sueldo bruto: S/.", format(sueldobruto,".2f"))
print("Sueldo neto: S/.", format(sueldoneto,".2f"))