import os
os.system("cls")

numeroA= int(input("Numero A:"))
numeroB= int(input("Numero B:"))
numeroC= int(input("Numero C:")) 

resultado=str

if numeroA < numeroB and numeroB < numeroC :
    resultado="ascendente"
elif numeroA > numeroB and numeroB > numeroC :
    resultado= "descendente"
    
else : resultado="desorden"

print ("Resultado:" , resultado)
