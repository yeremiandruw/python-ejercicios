import os
os.system("cls")

gigabytes= int(input("Ingrese capacidad del disco:"))

megabytes=gigabytes*1024
kilobytes=megabytes*1024
bytes=megabytes*1024

print("Capacidad en gigabytes:" , gigabytes, "GB")
print("Capacidad en megabytes:" , megabytes, "MB")
print("Capacidad en kilobytes:" , kilobytes, "KB")
print("Capacidad en bytes:" , bytes, "B")