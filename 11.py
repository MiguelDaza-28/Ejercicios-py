#Heladería: factura de varios clientes

total_dinero = 0
clientes = 0
c_cono = 0
c_vaso = 0
c_split = 0

producto = ""

while producto != "salir":
    producto = input("Producto (cono, vaso, split) o 'salir': ").lower()

    if producto != "salir":
        cantidad = int(input("¿Cuántos?: "))
        
        if producto == "cono":
            precio = 3000
            c_cono += cantidad

        elif producto == "vaso":
            precio = 4000
            c_vaso += cantidad

        elif producto == "split":
            precio = 9000
            c_split += cantidad

        else:
            print("Producto no valido")
            continue

        total_dinero += (precio * cantidad)
        clientes += 1


print(f"\nTotal: ${total_dinero} | Clientes: {clientes}")

ganador = ""

if clientes == 0:
    ganador = "No hubo ventas"

elif c_cono >= c_vaso and c_cono >= c_split:
    ganador = "Cono"

elif c_vaso >= c_cono and c_vaso >= c_split:
    ganador = "Vaso"

else:
    ganador = "Banana Split"

print(f"El producto estrella es: {ganador}")