import os
os.system("cls")

hora= int(input("Hora:"))
horaam= float
horapm= float

if hora > 12  :
    horapm = hora -2
    dig1=int((horapm%100)/10)
    dig2=int(horapm%10)
    if(dig1==2):
        resultado="1"+str(dig2)
        print("Hora ",resultado,"PM")
    elif dig1==1:
        resultado=str(dig2)
        print("Hora ",resultado,"PM")    
elif hora < 12 : 
    horaam = hora
    print("Hora",horaam,"AM")

else : print ("error") 


