#Peluquería: agenda de atención

recaudo_total = 0
cortes = 0
cepillados = 0
tinturas = 0

print("REGISTRO DE PELUQUERÍA (7 CLIENTES)")

for i in range(1, 8):
    print(f"\nCliente #{i}:")

    nombre = input("Nombre del cliente: ")
    servicio = input("Servicio (corte, cepillado, tintura): ").lower()

    if servicio == "corte":
        cortes += 1
        precio = 1

    elif servicio == "cepillado":
        cepillados += 1
        precio = 1

    elif servicio == "tintura":
        tinturas += 1
        precio = 1

    else:
        print("Servicio no reconocido.")
        continue

    valor = int(input("Valor pagado: $"))
    recaudo_total += valor

print("-" * 30)
print(f"RECAUDO TOTAL DEL DÍA: ${recaudo_total}")
print(f"Cortes: {cortes} | Cepillados: {cepillados} | Tinturas: {tinturas}")