#Tienda de mascotas: ventas por categoría

total_alimento = 0
total_juguete = 0
total_accesorio = 0

print("REGISTRO DE VENTAS: TIENDA DE MASCOTAS")


for i in range(10):
    print(f"\nVenta #{i + 1}")
    categoria = input("Categoría (alimento, juguete, accesorio): ").lower()
    valor = int(input("Valor de la venta: $"))

    
    if categoria == "alimento":
        total_alimento = total_alimento + valor

    elif categoria == "juguete":
        total_juguete = total_juguete + valor

    elif categoria == "accesorio":
        total_accesorio = total_accesorio + valor

    else:
        print("Categoría no válida, el valor no se sumará.")


print("\n" + "="*30)
print(f"Total Alimento: ${total_alimento}")
print(f"Total Juguetes: ${total_juguete}")
print(f"Total Accesorios: ${total_accesorio}")


if total_alimento > total_juguete and total_alimento > total_accesorio:
    ganador = "Alimento"
elif total_juguete > total_alimento and total_juguete > total_accesorio:
    ganador = "Juguete"
else:
    ganador = "Accesorio"

print(f"La categoría con más ventas fue: {ganador}")
print("="*30)
