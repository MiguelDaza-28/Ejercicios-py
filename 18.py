#Centro de idiomas: evaluación de estudiantes

bajo = 0
medio = 0
alto = 0

print("EVALUACIÓN DE INGLÉS")

continuar = "si"

while continuar == "si":
    nombre = input("\nEstudiante: ")
    
    n1 = float(input("Nota Speaking: "))
    n2 = float(input("Nota Listening: "))
    n3 = float(input("Nota Reading: "))
    
    promedio = (n1 + n2 + n3) / 3
    print(f"Promedio: {promedio:.1f}")

    if promedio < 60:
        bajo += 1

    elif 60 <= promedio < 80:
        medio += 1

    else:
        alto += 1

    continuar = input("¿Otro estudiante? (si/no): ").lower()


print(f"\nBajo: {bajo} | Medio: {medio} | Alto: {alto}")
