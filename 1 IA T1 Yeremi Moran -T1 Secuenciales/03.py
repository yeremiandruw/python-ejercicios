import os
os.system("cls")

kilometro= float(input("Longitud del primer tramo:"))
pies= float(input("Longitud del segundo tramo:"))
millas= float(input("Longitud del tercer tramo:"))

primertramo= kilometro*1000
segundotramo= pies/3.2808
tercertramo= millas*1609
totalmetro= primertramo + segundotramo + tercertramo
totalyarda= ((totalmetro*3.2808)/3)

print("Total metro:" , format (totalmetro,".2f"))
print("Total yarda:" , format(totalyarda,".2f"))
