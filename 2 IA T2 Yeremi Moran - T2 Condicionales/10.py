import os
os.system("cls")

nota1= int(input("Nota 1:"))
nota2= int(input("Nota 2:"))
nota3= int(input("Nota 3:"))
nota4= int(input("Nota 4:"))
nota5= int(input("Nota 5:"))

curso=str
promedioAprobatorio= int
totalsumadeNotas= nota1 + nota2 + nota3 + nota4 + nota5

notaMayor= int
notaMenor= int
if nota1 > nota2 and nota1 > nota3 and nota1 > nota4 and nota1 > nota5 :
    notaMayor= nota1
elif nota2 > nota3 and nota2 > nota4 and nota2 > nota5 :
    notaMayor= nota2
elif nota3 > nota4 and nota3 > nota5:
    notaMayor = nota3
elif nota4 > nota5 :
    notaMayor = nota4
else : notaMayor = nota5

if nota5 < nota1 and nota5 < nota2 and nota5 < nota3 and nota5 < nota4 :
    notaMenor= nota5
elif nota4 < nota3 and nota4 < nota2 and nota4 < nota1 :
    notaMenor= nota4
elif nota3 < nota2 and nota3 < nota1 :
    notaMenor= nota3
elif nota2 < nota1 :
    notaMenor= nota2
else : notaMenor= nota1

totalsumadeNotas -= (notaMayor + notaMenor)
promedioAprobatorio = totalsumadeNotas / 3 

print("Nota Menor:" , notaMenor)
print("Nota Mayor:" , notaMayor)
print("promedioAprobatorio:" , promedioAprobatorio)

