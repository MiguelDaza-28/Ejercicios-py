#Parqueadero: control de vehículos

recaudo_total = 0
carros = 0
motos = 0
pago_maximo = 0
placa_maxima = ""

i = 1

print("CONTROL DE PARQUEADERO (8 VEHÍCULOS)")

while i <= 8:
    print(f"\nVehículo #{i}:")
    
    placa = input("Ingrese la placa: ")
    tipo = input("¿Es carro o moto?: ").lower()
    
    if tipo == "carro":
        horas = int(input("¿Cuántas horas estuvo?: "))
        cobro = horas * 4000
        carros += 1
        print(f"El cobro para el carro es: ${cobro}")

    elif tipo == "moto":
        horas = int(input("¿Cuántas horas estuvo?: "))
        cobro = horas * 2000
        motos += 1
        print(f"El cobro para la moto es: ${cobro}")

    else:
        print("Vehículo no permitido. Intente de nuevo con 'carro' o 'moto'.")
        continue 

    recaudo_total += cobro
    
    if cobro > pago_maximo:
        pago_maximo = cobro
        placa_maxima = placa
        
    i += 1 

print("-" * 30)
print(f"Recaudo total: ${recaudo_total}")
print(f"Cantidad de carros: {carros}")
print(f"Cantidad de motos: {motos}")
print(f"El vehículo que más pagó fue {placa_maxima} con ${pago_maximo}")