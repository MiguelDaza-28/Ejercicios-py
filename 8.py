#Tienda deportiva: contar productos caros

caros = 0 

for i in range(6):
    precio = int(input("precio: "))

    if precio > 100000:
        caros +=1

print("productos caros:", caros)