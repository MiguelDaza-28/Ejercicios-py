#Cafetería: total de una compra sencilla

precio_café = 4000
precio_té = 3500
precio_jugo = 5000

print("Bienvenido a la cafetería, por favor seleccione su bebida:")

pedido = input("¿Qué bebida desea comprar? (café, té, jugo): ")

cantidad = int(input("¿Cuántas unidades desea comprar? "))

if pedido == "café":
    total = precio_café * cantidad
    print(f"El total de su compra es: ${total}")

elif pedido == "té":
    total = precio_té * cantidad
    print(f"El total de su compra es: ${total}")

elif pedido == "jugo":
    total = precio_jugo * cantidad
    print(f"El total de su compra es: ${total}")

else:
    print("Bebida no válida.")