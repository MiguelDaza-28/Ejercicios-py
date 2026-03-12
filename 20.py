#Club recreativo: control de membresías

basico, premium, familiar = 0, 0, 0
total_dinero = 0

cantidad = int(input("¿Cuántas personas registrarás?: "))

for i in range(1, cantidad + 1):
    nombre = input(f"\n({i}) Nombre: ")
    
    v_edad = input(f"Edad de {nombre}: ")
    
    edad = int(v_edad) if v_edad.isdigit() else 0

    if edad < 18: print(">> Registro juvenil")

    elif edad >= 60: print(">> Beneficio senior")

    print("Planes: 1-Básico (50k), 2-Premium (90k), 3-Familiar (130k)")
    plan = input("Selecciona plan (1/2/3): ")

    if plan == "1":
        total_dinero += 50000
        basico += 1

    elif plan == "2":
        total_dinero += 90000
        premium += 1

    else:
        total_dinero += 130000
        familiar += 1



ventas = {"Básico": basico, "Premium": premium, "Familiar": familiar}
mas_vendido = max(ventas, key=ventas.get)

print(f"\n--- REPORTE FINAL ---")
print(f"Total recaudado: ${total_dinero}")
print(f"Ventas = Básico: {basico} | Premium: {premium} | Familiar: {familiar}")
print(f"El plan más vendido fue: {mas_vendido}")
