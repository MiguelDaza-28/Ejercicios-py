#Gimnasio: promedio de rendimiento semanal


bajo = 0
medio = 0
alto = 0

print("REGISTRO DE RENDIMIENTO SEMANAL")


for i in range(5):
    print(f"\nRegistro de la persona #{i + 1}:")

    nombre = input("Nombre: ")

    dias = int(input("Días asistidos en la semana: "))
    
    minutos = int(input("Minutos promedio por día: "))

    if dias < 3:
        print(f"{nombre} tiene: Bajo compromiso")
        bajo = bajo + 1

    elif dias >= 3 and dias <= 4:
        print(f"{nombre} tiene: Compromiso medio")
        medio = medio + 1

    else:
        print(f"{nombre} tiene: Compromiso alto")
        alto = alto + 1

print("\n" + "="*30)
print("RESUMEN DE LA SEMANA")
print(f"Personas con Bajo compromiso: {bajo}")
print(f"Personas con Compromiso medio: {medio}")
print(f"Personas con Compromiso alto: {alto}")
print("="*30)