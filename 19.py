#Tienda de ropa deportiva: inventario crítico

agotado, bajo, normal = 0, 0, 0
i = 1

while i <= 10:
    nombre = input(f"\n{i}. Producto: ")

    valor = input(f"Cantidad de {nombre}: ")

    if not valor.isdigit():
        print("Error: La cantidad debe ser numérica Intenta de nuevo.")
        continue

    cant = int(valor)

    if cant == 0:
        agotado += 1

    elif cant <= 5:
        bajo += 1

    else:
        normal += 1
    
    i += 1

print(f"\nProductos agotados: {agotado}")
print(f"Productos con inventario bajo: {bajo}")
print(f"Productos con inventario normal: {normal}")