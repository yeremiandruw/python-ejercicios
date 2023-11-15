import os
os.system("cls")

dinero= int(input("Ingrese la cantidad de dinero:"))

billetes200= dinero//200
billetes100= (dinero%200)//100
billetes50= (dinero%200)%100//50
billetes20= (((dinero%200)%100)%50)//20
billetes10= ((((dinero%200)%100)%50)%20)//10
moneda5= ((((dinero%200)%100)%50)%20)%10//5
moneda2= ((((((dinero%200)%100)%50)%20)%10)%5)//2
moneda1= (((((((dinero%200)%100)%50)%20)%10)%5)%2)

print("Billetes de 200 soles:" , billetes200)
print("Billetes de 100 soles:" , billetes100)
print("Billetes de 50 soles:" , billetes50)
print("Billetes de 20 soles:" , billetes20)
print("Billetes de 10 soles:" , billetes10)
print("Monedas de 5 soles:" , moneda5)
print("Monedas de 2 soles:" , moneda2)
print("Monedas de 1 sole:" , moneda1)