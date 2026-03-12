#Cafetería: descuento por consumo

total_acumulado = 0
pedido = ""

while pedido != "salir":
    pedido = input("\nProducto (cafe, capuchino, pastel) o 'salir': ").lower()
    
    if pedido != "salir":
        cantidad = int(input("¿Cuántos?: "))
        
    
        if pedido == "cafe": precio = 4000

        elif pedido == "capuchino": precio = 7000

        elif pedido == "pastel": precio = 6000

        else:
            print("Producto no valido")
            continue

        total_cliente = precio * cantidad


        if total_cliente > 20000:

            total_cliente = total_cliente * 0.90
            print("Se aplicó 10% de descuento")

        print(f"Total a pagar: ${total_cliente}")
        total_acumulado += total_cliente

print(f"\nVENTA TOTAL DEL DÍA: ${total_acumulado}")
