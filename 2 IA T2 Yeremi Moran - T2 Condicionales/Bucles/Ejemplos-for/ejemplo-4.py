import random

texto=" YEREMI TIENE 17AÑOS "

print("1:",texto)
print("2:",texto[18])
print("3:",texto.replace(" ",""))
print("4:",texto.strip())
print("5:",texto.lstrip())
print("6:",texto.rstrip())
print("7:",texto.upper())
print("8:",texto.lower())
print("9:",texto.index("O"))
print("10:",random.randrange(100))

i=0
while i< len(texto):
    print(texto[-i],end="")
    i+=1