import os
os.system("cls")

dinerojuan= float(input("Dinero de juan: $"))
dinerorosa= float(input("Dinero de juan: $"))
dinerodaniel= float(input("Dinero de juan: S/."))

dolaresdaniel= dinerodaniel/3
capitaltotal= dinerojuan + dinerorosa + dolaresdaniel
porcentajejuan= (dinerojuan*100)/capitaltotal
porcentajerosa= (dinerorosa*100)/capitaltotal
porcentajedaniel= (dolaresdaniel*100)/capitaltotal

print("El capital total es: $" ,format(capitaltotal,".2f" ))
print("Juan dio el", format (porcentajejuan,".2f"),"%")
print("Rosa dio el", format (porcentajerosa,".2f"),"%")
print("Daniel dio el", format (porcentajedaniel,".2f"),"%")

# cambios a subir