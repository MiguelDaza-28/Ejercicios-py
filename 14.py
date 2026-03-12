# Cine: control de sala

capacidad = int(input("¿Cuál es la capacidad de la sala?: "))
ingresados = 0
niños = 0
adolescente = 0
adultos = 0
mayores = 0

continuar = "si"

while ingresados < capacidad and continuar == "si":
    print(f"\nAsiento {ingresados + 1} de {capacidad}")
    edad = int(input("Ingrese la edad de la persona: "))

    if edad <= 0:
        print("Error: la persona no existe")
        continue

    elif edad <= 11:
        print("Clasificación: Niño")
        niños += 1

    elif 12 <= edad <= 17:
        print("Clasificación: Adolescente")
        adolescente += 1

    elif 18 <= edad <= 59:
        print("Clasificación: Adulto")
        adultos += 1

    else:
        print("Clasificación: Adulto mayor")
        mayores += 1


    ingresados += 1

    if ingresados < capacidad:
        continuar = input("¿Ingresa otra persona? (si/no): ").lower()

    else:
        print("\n¡SALA LLENA!")

print("\n" + "="*30)
print(f"Total personas en sala: {ingresados}")
print(f"Niños: {niños} | Adultos: {adultos} | Mayores: {mayores}")


if ingresados == capacidad:
    print("Estado: La sala se llenó por completo.")
else:
    print(f"Estado: Quedaron {capacidad - ingresados} asientos libres.")
print("="*30)